#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/10 11:00
# @File    : doccano_datas.py
# @Software: Basebit
# @Description: 准备为doccano的数据集
import tasks.templates660_20220111_4.task_constant as cons
import tasks.templates660_20220104_3.task_constant as cons0104
from tasks.task_main import get_doccano_datas

if __name__ == '__main__':
    get_doccano_datas(
        cons.EXTRACT_TEMPLATE_FILES,
        cons.TEMPLATE_PATH,
        '{}/doccano_0111.txt'.format(cons.TASK_PATH)
    )
