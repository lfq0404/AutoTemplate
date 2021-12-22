#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/15 2:26 下午
# @File    : myUtils.py
# @Software: Basebit
# @Description:
import re
import pandas

from regex import regex
from html.parser import HTMLParser
from bs4 import BeautifulSoup

import constant as cons
import config as conf


def read_excel(file_path, sheet_name):
    """
    读取Excel
    :param file_path:
    :param sheet_name:
    :return:
    """
    datas = pandas.read_excel(file_path, sheet_name=sheet_name, header=None, engine='openpyxl')
    return datas


def department_statistics():
    """
    根据科室进行统计
    :return:
    """
    datas = read_excel(cons.EXCEL_RESULT_FOR_LOOK_PATH, cons.SHEET_NAME)
    result = {}
    files = set()
    for line in datas.itertuples():
        file_name = line._1
        if '-' not in file_name:
            continue
        files.add(file_name)
    for file_name in files:
        department = re.findall('.+?-(.+?)-', file_name)[0]
        tmp = result.get(department)
        if not tmp:
            result[department] = {
                '总数': 0,
                '初诊': 0,
                '复诊': 0,
                '配药': 0,
                '其他': 0,
            }
        if '初诊' in file_name:
            result[department]['初诊'] += 1
        elif '复诊' in file_name:
            result[department]['复诊'] += 1
        elif '配药' in file_name:
            result[department]['配药'] += 1
        else:
            result[department]['其他'] += 1
        result[department]['总数'] += 1

    print(result)


def reverse_delete_sqls():
    """
    将SQL顺序反转打印
    """
    text = """delete from department where id = 4090100;
delete from virtual_department where id = 209;
delete from department_mapping where id = 505;
"""
    sqls = text.split(';')
    for sql in sqls[::-1]:
        if sql:
            print(sql.replace('\n', ''), ';')
