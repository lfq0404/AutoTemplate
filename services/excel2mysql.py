#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/26 3:06 下午
# @File    : excel2mysql.py
# @Software: Basebit
# @Description:

import copy
import datetime
import json
import re
import time
import traceback

import pandas
import pymysql
import six
from pymysql.converters import escape_string

import constant as cons

from myUtils import read_excel, get_check_file_datas

# 114中，瑞金的机构信息，正式部署的时候不会用到该值
rj_organization_code = '00000002'
rj_organization_id = '2'
source_id = 2

connection = pymysql.connect(host=cons.HOST,  # host属性
                             user=cons.USER,  # 用户名
                             password=cons.PASSWORD,  # 此处填登录数据库的密码
                             db=cons.DB_NAME  # 数据库名
                             )

cur = connection.cursor()

DELETE_LOGS = []


class Excel2Mysql:
    def __init__(self, template_disease_file_path, excel_check_file_path, present_file_path, extract_template_files):
        self.template_disease_file_path = template_disease_file_path
        self.excel_check_file_path = excel_check_file_path
        self.present_file_path = present_file_path
        self.extract_template_files = extract_template_files

    def get_package_diseases_map(self):
        """
        获取疾病与package的映射关系
        :return:
        """
        # 医疗团队产出的映射关系
        package_diseases_map = {}
        datas = read_excel(self.template_disease_file_path, 'Sheet1')
        for line in datas.itertuples():
            file_name = line._3
            if pandas.isna(file_name) or '-' not in file_name:
                continue
            depart_code = line._4
            depart_name = line._5
            icd_codes = line._7
            icd_codes = [] if pandas.isna(icd_codes) else icd_codes.split(',')
            disease_names = line._8
            disease_names = [] if pandas.isna(disease_names) else disease_names.split(',')
            remark = line._9
            conditions = line._10
            is_depart = not pandas.isna(remark)  # 是否是科室通用
            disease_ids = []
            for icd_code in icd_codes:
                sql = 'select id from {} where code like "{}%" and source_id = {}'.format('disease_v2', icd_code,
                                                                                          source_id)
                cur.execute(sql)
                diseases_temp = cur.fetchall()
                disease_ids.extend([i[0] for i in diseases_temp])

            package_diseases_map[file_name] = {
                'depart_name': depart_name,
                'depart_code': depart_code,
                'icd_codes': icd_codes,
                'disease_names': disease_names,
                'disease_ids': disease_ids,  # disease_v2对应的主键id
                'is_depart': is_depart,
                'conditions': conditions,  # 扩展信息，年龄、性别限制等
            }

        return package_diseases_map

    def get_package_infos(self):
        """
        获取完整的package信息
        :return:
        {
        file_name: {
            template_type: {
                'segments': {
                    label: segment,
                    label: segment,
                },
                'template_content': '<b>婚育史：{婚}，{育}。'
                }
            },
            'PRESENT': 'feature'
        }
        """
        package_infos = {}

        # 先获取原始的Excel数据
        datas = get_check_file_datas(self.excel_check_file_path)

        # 第二次，拼接json
        valid_files = set()
        for _, line in enumerate(datas.itertuples()):
            file_name = line._1
            template_content = line._2
            label = line._3
            segment_content = line._4
            category_text = line._7
            # template_category = cons.KNOWN_CATEGORY_MAP.get(category_text)
            if self.extract_template_files and file_name not in self.extract_template_files:
                continue
            if pandas.isna(segment_content):
                continue

            valid_files.add(file_name)
            package = package_infos.get(file_name)
            if not package:
                package_infos[file_name] = {}

            template = package_infos[file_name].get(category_text)
            if not template:
                package_infos[file_name][category_text] = {'segments': {}}

            package_infos[file_name][category_text]['template_content'] = template_content
            package_infos[file_name][category_text]['segments'][label] = segment_content

        print('无效的文件为：')
        for i in set(self.extract_template_files) - valid_files:
            print(i)

        # 附加现病史的内容
        datas = read_excel(self.present_file_path, '4.现病史可解析')
        # 先根据new_label修改template_content
        for _, line in enumerate(datas.itertuples()):
            file_name = line._1
            feature = line._3
            package_info = package_infos.get(file_name)
            if not package_info:
                if file_name in self.extract_template_files:
                    package_infos[file_name] = {}
                else:
                    continue

            package_infos[file_name][cons.PRESENT_NAME] = feature

        return package_infos

    def format_sql(self, value):
        """
        格式化sql中的各种格式
        比如防止单引号等等
        :param value:
        :return:
        """
        return value if isinstance(value, (datetime.datetime, float, int, datetime.date)) else escape_string(value)

    def get_insert_sql(self, table_name, infos: dict, sign=1):
        """
        拼接insert的sql语句
        :param table_name:
        :param infos:
        :param sign: 0直接插入数据，不忽略报错；1利用新数据更新老数据；2如果存在相同数据，则以老数据为准
        :return:
        """
        sign = int(sign)
        col_str = ''
        row_str = ''
        for key in infos.keys():
            if infos[key] is not None:
                col_str = col_str + " " + key + ","
                row_str = "{}'{}',".format(row_str, self.format_sql(infos[key]))
                sql = "INSERT INTO {} ({}) VALUES ({}) ".format(table_name, col_str[1:-1],
                                                                row_str[:-1])
        if sign == 1:
            # 如果要以新的数据更新老数据，则拼接update语句
            sql += 'ON DUPLICATE KEY UPDATE '
            for (key, value) in six.iteritems(infos):
                if value is not None:
                    sql += "{} = '{}', ".format(key, self.format_sql(value))
            sql = sql[:-2]
        elif sign == 2:
            # 如果以老的数据为准，则ignore
            sql = sql.replace('INSERT INTO', 'INSERT IGNORE INTO')
        else:
            pass
        return sql

    def inert_into_mysql(self, package_infos, package_diseases_map, departments):
        """
        数据入库
        :param package_infos:
        :param package_diseases_map:
        :return:
        """

        def insert_segment(table, data):
            """
            创建segment
            :param data:
            :return:
            """
            sql = self.get_insert_sql(table, data, sign=1)
            segment_id = self.exec_insert_sql(sql)

            return segment_id

        def insert_template(data):
            """
            创建template
            :param data:
            :return:
            """
            # # 由于content没办法加唯一索引，需要事先判断下
            # sql = '''select id from {} where category='{}' and content='{}' and type='{}' and attr='{}' '''.format(
            #     'template',
            #     data['category'],
            #     data['content'],
            #     data['type'],
            #     data['attr']
            # )
            # item = cur.execute(sql)
            # if item:
            #     template_id = cur.fetchone()[0]
            # else:
            #     sql = get_insert_sql('template', data)
            #     template_id = exec_insert_sql(sql)

            # 可能儿科的咳嗽和呼吸科的咳嗽模板不一样，即使一样也是他们分开各自管理各自的
            # 所以每次都要新建template
            sql = self.get_insert_sql('template', data, sign=0)
            tp_id = self.exec_insert_sql(sql)

            return tp_id

        def insert_package(package_info):
            """
            新建package
            :param package_info:
            :return:
            """
            ids = {}
            # "其他"的content是数组
            custom_infos = []

            for category_text, template in package_info.items():
                template_category = cons.KNOWN_CATEGORY_MAP.get(category_text) or 'CUSTOM'
                if template_category == 'PRESENT':
                    # 现病史不需要创建segment
                    template_content = json.loads(template)
                else:
                    # 其余类型的创建segment
                    template_content = {
                        'display': template['template_content'],
                        'segments': []
                    }
                    for label, segment in template['segments'].items():
                        template_content['segments'].append(json.loads(segment))
                        # segment级别
                        if template_category in cons.TABLE_PHYSICAL_SEGMENT:
                            table = 'physical_segment_v2'
                        elif template_category in cons.TABLE_MEDICAL_HISTORY_SEGMENT:
                            table = 'medical_history_segment_v2'
                        else:
                            # 其余的全部归在custom下
                            table = 'custom_segment_v2'
                            template_content['title'] = category_text
                        # 1、创建最明细的segment
                        segment_id = insert_segment(
                            table,
                            {
                                'label': label,
                                'content': segment
                            })

                # 2.1、创建template
                if template_category == 'CUSTOM':
                    custom_infos.append(template_content)
                else:
                    template_id = insert_template({
                        'category': template_category,
                        'content': json.dumps(template_content, ensure_ascii=False),
                        'type': 'SEG_FORMAT_V4',
                        'attr': 'SYSTEM'
                    })
                    ids[template_category] = template_id
            else:
                # 2.2、由于custom的content为list，单独创建相关的的template
                if custom_infos:
                    template_id = insert_template({
                        'category': 'CUSTOM',
                        'content': json.dumps(custom_infos, ensure_ascii=False),
                        'type': 'SEG_FORMAT_V4',
                        'attr': 'SYSTEM'
                    })
                    ids['CUSTOM'] = template_id

            # 3、新建package
            # 后台以后是分科室疾病管理的，未来还会涉及科室权限，统一管理业务上不太合适，要分开建一下
            # 所以每次都新建一个package
            infos = {}
            for k, v in ids.items():
                infos[cons.PACKAGE_COL_CATEGORY_MAP[k]] = v
            sql = self.get_insert_sql('package', infos, sign=0)
            pk_id = self.exec_insert_sql(sql)

            return pk_id

            # 由于package表没有唯一索引，先查询一遍保证不重复
            # infos = {}
            # select_sql = ''
            # for k, v in ids.items():
            #     infos[cons.PACKAGE_COL_CATEGORY_MAP[k]] = v
            #     select_sql += ' and {}={} '.format(cons.PACKAGE_COL_CATEGORY_MAP[k], v)

            # select_sql = 'select id from {} where {}'.format('package', select_sql[4:])
            # item = cur.execute(select_sql)
            # if item:
            #     package_id = cur.fetchone()[0]
            # else:
            #     sql = get_insert_sql('package', infos)
            #     package_id = exec_insert_sql(sql)

        def insert_disease_package(disease_id, department_code, package_id, _type, conditions):
            """
            新建desease_package的映射关系
            :param disease_id:
            :param department_code:
            :param package_id:
            :param _type:
            :return:
            """
            sql = 'select id from {} where code = {} and org_code = {}'.format('department', department_code,
                                                                               rj_organization_code)
            try:
                cur.execute(sql)
            except:
                print()
            department = cur.fetchall()
            sql = self.get_insert_sql(
                'disease_package_v2',
                {
                    'owner_type': 'department',
                    'owner_id': department[0][0],
                    'disease_id_type': 'DISEASE',
                    'disease_id': disease_id,
                    'package_id': package_id,
                    'status': 1,
                    'type': _type
                },
                sign=0)
            self.exec_insert_sql(sql)

        def insert_virtual_department_package(data):
            """
            新建virtual_department_package映射关系
            :param data:
            :return:
            """
            sql = self.get_insert_sql('virtual_department_package_v2', data, sign=0)
            self.exec_insert_sql(sql)

        num = 0
        for file_name, disease_info in package_diseases_map.items():
            num += 1
            package_info = package_infos.get(file_name)
            if not package_info:
                print('该模板为空，不入库：{}！！！'.format(file_name))
                continue
            print('[{}]开始处理：{}'.format(num, file_name))
            depart_code = disease_info['depart_code']
            depart_name = disease_info['depart_name']
            if '初诊' in file_name:
                _type = 'INITIAL'
            elif '复诊' in file_name:
                _type = 'SUBSEQUENT'
            else:
                _type = 'MEDICINE'

            if disease_info['is_depart']:
                package_id = insert_package(package_info)
                # 4.1、通用模板，与virtual_department关联
                virtual_department_id = departments[depart_name]['virtual_department_id']
                insert_virtual_department_package(
                    {
                        'virtual_department_id': virtual_department_id,
                        'package_id': package_id,
                        'type': _type
                    })
            else:
                conditions = None if pandas.isna(disease_info['conditions']) else disease_info['conditions']
                for disease_id in disease_info['disease_ids']:
                    # 一个疾病对应一个模板
                    package_id = insert_package(package_info)
                    # 4.2、与疾病相关的模板
                    insert_disease_package(disease_id, depart_code, package_id, _type, conditions)

    def init_datas(self):
        """
        初始化MySQL数据
        添加department、virtual_department信息
        :return:
        {
        department_name: {
            'department_id': department_id,
            'virtual_department_id': virtual_department_id
            }
        }
        """
        departments = {}
        datas = read_excel(self.template_disease_file_path, 'Sheet1')
        for line in datas.itertuples():
            file_name = line._3
            if pandas.isna(file_name) or '-' not in file_name:
                continue
            department_code = line._4
            depart_name = line._5
            virtual_name = 'rj_{}'.format(depart_name)
            sql = 'select id from {} where code = {} and org_code = {}'.format('department', department_code,
                                                                               rj_organization_code)
            item = cur.execute(sql)
            if not item:
                sql = self.get_insert_sql(
                    'department',
                    {
                        'org_code': rj_organization_code,
                        'code': department_code,
                        'name': depart_name
                    })
                department_id = self.exec_insert_sql(sql)
            else:
                department_id = cur.fetchall()[0][0]

            # 完善virtual_department配置
            sql = 'select id from {} where name="{}"'.format('virtual_department', virtual_name)
            item = cur.execute(sql)
            if not item:
                sql = self.get_insert_sql('virtual_department', {
                    'name': virtual_name,
                    'description': virtual_name,
                    'source_id': source_id,
                    'auto_update': 1,
                    'disabled': 0
                })
                virtual_department_id = self.exec_insert_sql(sql)
                sql = self.get_insert_sql(
                    'department_mapping',
                    {
                        'virtual_department_id': virtual_department_id,
                        'department_id': department_id
                    })
                mapping_id = self.exec_insert_sql(sql)
            else:
                rows = cur.fetchall()
                virtual_department_id = rows[0][0]

            departments[depart_name] = {
                'department_id': department_id,
                'virtual_department_id': virtual_department_id
            }

        return departments

    def exec_insert_sql(self, sql):
        """
        执行insert，并返回id
        :param sql:
        :return:
        """
        cur.execute(sql)
        _id = connection.insert_id()
        table_name = re.findall('into (.*?) ', sql, re.I)[0]
        if _id:
            DELETE_LOGS.append('delete from {} where id = {}'.format(table_name, _id))
            print('{}-新id为：{}'.format(table_name, _id))
        else:
            print('{}-未更新，SQL为：{}'.format(table_name, sql))
        connection.commit()
        return _id

    def record_delete_log(self):
        """
        记录delete日志
        :return:
        """
        with open('delete_log_{}.sql'.format(time.strftime("%Y%m%d-%H%M%S", time.localtime())), 'w') as f:
            for line in DELETE_LOGS[::-1]:
                f.write(line)
                f.write(';\n')

    def db_localhost(self):
        """
        判断目前的数据库配置是否为本地
        :return:
        """
        return cons.HOST in ('localhost', '127.0.0.1')

    def excel2mysql(self):
        """
        前提：人工判读完成 get_update_segments 不报错

        选出能映射到疾病的模板
        选出模板的template与对应的segment
        判断同名segment，不能处理则添加文件名标识
        将数据写入数据库
        :return:
        """
        # 初始化机构、部门数据
        departments = self.init_datas()
        # 获取package的完整数据
        package_infos = self.get_package_infos()
        # 获取package与disease的关系
        package_diseases_map = self.get_package_diseases_map()
        # 数据入库
        try:
            self.inert_into_mysql(package_infos, package_diseases_map, departments)
        except:
            traceback.print_exc()
        # 记录log
        self.record_delete_log()
