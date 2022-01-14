#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/14 10:36
# @File    : get_test_package.py
# @Software: Basebit
# @Description:
import json
from shutil import copyfile
import pandas as pd
import os
from services.excel2mysql import cur

test_file1 = """
import os

import pandas as pd
from selenium import webdriver
import time
import re

check_files = """
test_file2 = """

def manual_check(server):
    '''
    测试流程
    按文件依次模拟点击
    需要在https://sites.google.com/chromium.org/driver/下载驱动
    :return:
    '''
    datas = pd.read_excel('template_disease_map.xlsx', sheet_name='Sheet1', engine='openpyxl', dtype=str)
    browser = webdriver.Chrome()
    browser.set_window_position(**{'x': -1255, 'y': -2135})
    browser.set_window_size(**{'width': 1200, 'height': 2000})
    time.sleep(1)
    browser2 = webdriver.Chrome()
    browser2.set_window_position(**{'x': -54, 'y': -2135})
    browser2.set_window_size(**{'width': 1200, 'height': 2000})
    time.sleep(1)

    for line in datas.itertuples():
        type_ = line.type_  # 初诊、复诊
        disease_id = line.disease_id_eg
        disease_code = line.disease_code_eg
        disease_name = line.disease_name_eg
        depart_code = line.depart_code
        file_name = line.file_name

        if file_name not in check_files:
            continue

        if type_ == '初诊':
            _type = 'INITIAL'
        elif type_ == '复诊':
            _type = 'SUBSEQUENT'
        else:
            _type = 'MEDICINE'

        with open('aiwizard.html', 'r') as f:
            html = f.read()
        html = re.sub('deptCode: "(\d+)"', 'deptCode: "{}"'.format(depart_code), html)
        html = re.sub('tplType: "(.+)"', 'tplType: "{}"'.format(_type), html)
        html = re.sub('"name": "(.+)"', '"name": "{}"'.format(disease_name), html)
        html = re.sub('"code": "(.+)"', '"code": "{}"'.format(disease_code), html)
        html = re.sub('"id": "(.+)"', '"id": "{}"'.format(disease_id), html)
        html = re.sub('height="(\d+)px"', 'height="{}px"'.format(1200), html)
        html = re.sub(
            'src="http.*',
            'src="http://{}/?type=iframe&visitId=707010491&orgCode=00000002&patientId=1646184620231"'.format(server),
            html)
        with open('aiwizard.html', 'w') as f:
            f.write(html)

        # 对比
        browser.get('file:///' + os.path.abspath('aiwizard.html'))
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/div[1]/button[1]').click()
        time.sleep(2)
        browser2.get('file:///' + os.path.abspath(file_name))
        time.sleep(2)

        # 等待人工校验
        next_ = input('直接输入回车继续，否则任意键退出：')
        if next_ != '':
            break

    browser.close()
    browser2.close()


if __name__ == '__main__':
    server = '172.18.0.76:8116'
    manual_check(server)

"""


def get_test_package(path_name):
    """
    将本批次依赖的原始html迁移到该文件夹下
    :return:
    """
    check_files = []
    file_path = './{}'.format(path_name)
    test_package_path = '{}/test_package'.format(file_path)

    # 创建test_package文件夹
    folder = os.path.exists(test_package_path)
    if not folder:
        os.makedirs(test_package_path)

    # 迁移本周相关的HTML，以及disease_map
    datas = pd.read_excel(
        './{}/template_disease_map.xlsx'.format(path_name), sheet_name='Sheet1', engine='openpyxl', dtype=str)
    for num, line in enumerate(datas.itertuples()):
        file_name = line.file_name
        copyfile(
            '/Users/jeremy.li/Basebit/Documents/develop/smart/20211013-瑞金门急诊模板配置/20211220-门诊660/{}'.format(file_name),
            '{}/{}'.format(test_package_path, file_name))

        if pd.isna(file_name) or '-' not in file_name:
            continue
        check_files.append(file_name)
        icd_codes = [] if pd.isna(line.icd_codes) else line.icd_codes.split(',')
        icd_code = icd_codes[0] if icd_codes else None

        disease_id, disease_code, disease_name = '24022', 'K50.900', '克罗恩病'  # 随便找一个冷门的作为通用
        if line.common != '通用':
            sql = 'select id, code, name from {} where code like "{}%" and source_id = 2 and status = 1'.format(
                'disease_v2', icd_code)
            cur.execute(sql)
            row = cur.fetchone()
            if row:
                disease_id, disease_code, disease_name = row

        datas.loc[num, 'disease_id_eg'] = disease_id
        datas.loc[num, 'disease_code_eg'] = disease_code
        datas.loc[num, 'disease_name_eg'] = disease_name

    datas.to_excel('{}/template_disease_map.xlsx'.format(test_package_path), index=False)

    # 添加demo页面
    copyfile(
        '/Users/jeremy.li/Basebit/Projects/smart-frontend/demo/iframe/aiwizard.html',
        '{}/aiwizard.html'.format(test_package_path)
    )
    copyfile(
        '/Users/jeremy.li/Basebit/Projects/smart-frontend/demo/iframe/jquery-1.8.3.min.js',
        '{}/jquery-1.8.3.min.js'.format(test_package_path)
    )

    # 添加test文件
    with open('{}/check.py'.format(test_package_path), 'w') as f:
        f.write(test_file1 + json.dumps(check_files, ensure_ascii=False) + test_file2)


if __name__ == '__main__':
    get_test_package('templates660_20220104_3')
