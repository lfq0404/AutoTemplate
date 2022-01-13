#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/29 15:15
# @File    : task_main.py
# @Software: Basebit
# @Description:

import os

from myUtils import get_check_file_datas
from services.excel2mysql import Excel2MysqlAppointID
from services.extract_core import RJExtract
from services.manual_check_service import ManualCheck
from services.pandas2excel import record2excel


def _code_extract(extract_template_files, template_path):
    """
    代码解析
    :return:
    """
    g = os.walk(template_path)

    result = []
    for path, _, file_list in g:
        for ind, file in enumerate(file_list):
            # file = '门诊病历(初诊)-咯血(4100200)门诊病历(初诊)8b933a9b-f0ed-459f-8974-ce2e07d44568.html'
            extract = RJExtract(path, file, extract_template_files)
            if extract.is_continue():
                print('文件不满足要求，不处理<{}>：{}'.format(ind, file))
                continue

            print('开始处理<{}>：{}'.format(ind, extract.file_path))
            file_result = extract.extract()
            result.extend(file_result)

    return result


def task_main(template_disease_file_path, excel_check_file_path, present_file_path, extract_template_files,
              standard_file_path, template_path, autocommit):
    """
    1、通过代码解析模板信息
    2、人工校验模板信息
    3、数据入库
    :return:
    """
    e2m = Excel2MysqlAppointID(
        template_disease_file_path,
        excel_check_file_path,
        present_file_path,
        extract_template_files,
        autocommit=autocommit
    )
    manual_check = ManualCheck(
        excel_check_file_path,
        extract_template_files,
        standard_file_path,
        template_disease_file_path
    )
    # manual_check.manual_check_package()

    reload = input('是否重新根据原始模板提取（y or n）：')
    if reload == 'y':
        # 提取信息
        datas = _code_extract(extract_template_files, template_path)
        # 保存到Excel中
        record2excel(excel_check_file_path, datas)
        raise ValueError('\n可查看{}查看效果，并修改。\n完成后，请在此运行，且reload=n'.format(excel_check_file_path))
    elif reload == 'n':
        pass
    else:
        raise ValueError('请输入正确的指令')

    # 人工处理本次自动化提取后，冲突的数据
    manual_check.check_recent_segments()
    # 与之前的结果进行对比
    manual_check.contrast_segments(e2m)
    # 数据入库
    e2m.excel2mysql()

    if autocommit:
        raise ValueError('需要手动执行新生成的insert_log文件！！！')


def get_doccano_datas(extract_template_files, template_path, output_text):
    """
    获取doccano的数据集
    :return:
    """

    def get_lines():
        g = os.walk(template_path)

        lines = []
        for path, _, file_list in g:
            for ind, file in enumerate(file_list):
                # file = '门诊病历(初诊)-咯血(4100200)门诊病历(初诊)8b933a9b-f0ed-459f-8974-ce2e07d44568.html'
                extract = RJExtract(path, file, extract_template_files)
                if extract.is_continue():
                    print('文件不满足要求，不处理<{}>：{}'.format(ind, file))
                    continue

                print('开始处理<{}>：{}'.format(ind, extract.file_path))
                file_result = extract.paragraphs()
                for i in file_result:
                    if not i[1]:
                        continue
                    l = '{}：{}'.format(i[0], i[1])
                    if l not in lines:
                        yield l
                        lines.append(l)

    with open(output_text, 'w') as f:
        for line in get_lines():
            f.write(line + '\n')
