#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/28 10:47
# @File    : temp.py
# @Software: Basebit
# @Description:
import pandas as pd
from shutil import copyfile


def move_files():
    """
    将本批次依赖的原始html迁移到该文件夹下
    :return:
    """
    datas = pd.read_excel('../template_disease_map.xlsx', sheet_name='Sheet1', engine='openpyxl', dtype=str)
    for file in datas['file_name']:
        copyfile('/Users/jeremy.li/Basebit/Documents/develop/smart/20211013-瑞金门急诊模板配置/20211220-门诊660/{}'.format(file),
                 file)


if __name__ == '__main__':
    move_files()
