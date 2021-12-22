#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/21 17:50
# @File    : constant.py
# @Software: Basebit
# @Description:

from constant import *

# 原始模板地址
RAW_TEMPLATES_PATH = '/Users/jeremy.li/Basebit/Documents/develop/smart/20211013-瑞金门急诊模板配置/rawTemplates'
TASK_PATH = '{}/tasks/templates1'.format(BASE_PATH)

# 输出的Excel
EXCEL_RESULT_FOR_LOOK_PATH = '{}/rj_templates.xlsx'.format(TASK_PATH)
EXCEL_RESULT_FOR_CHECK_PATH = '{}/rj_check_templates.xlsx'.format(TASK_PATH)
PRESENT_FILE_PATH = '{}/现病史解析记录.xlsx'.format(TASK_PATH)
TEMPLATE_DISEASE_FILE_PATH = '{}/近1年门诊常用科室模板与disease.xlsx'.format(TASK_PATH)
