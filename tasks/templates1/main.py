#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/15 2:25 下午
# @File    : main.py
# @Software: Basebit
# @Description:
import os

from services.excel2mysql import Excel2Mysql
from services.extract_core import ExtractCore
from services.manual_check_service import ManualCheck
from services.pandas2excel import record2excel
import tasks.templates1.task_constant as cons


def code_extract():
    """
    代码解析
    :return:
    """
    g = os.walk(cons.RAW_TEMPLATES_PATH)

    result = []
    for path, _, file_list in g:
        for ind, file in enumerate(file_list):
            # file = '4280000-门诊推拿科-门诊病历(初诊)-腰肌筋膜炎-门诊病历(初诊).html'

            extract = ExtractCore(path, file)
            if extract.is_continue():
                print('文件不满足要求，不处理<{}>：{}'.format(ind, file))
                continue

            print('开始处理<{}>：{}'.format(ind, extract.file_path))
            file_result = extract.extract()
            result.extend(file_result)

    return result


def main():
    """
    1、通过代码解析模板信息
    2、人工校验模板信息
    3、数据入库
    :return:
    """
    reload = input('是否重新根据原始模板提取（y or n）：')
    # reload = 'y'
    if reload == 'y':
        # 提取信息
        datas = code_extract()
        # 保存到Excel中
        record2excel(cons.EXCEL_RESULT_FOR_CHECK_PATH, datas)
    elif reload == 'n':
        pass
    else:
        raise ValueError('请输入正确的指令')

    # 人工校验本次提取结果
    manual_check = ManualCheck(
        cons.EXCEL_RESULT_FOR_CHECK_PATH,
        cons.EXTRACT_TEMPLATE_FILES,
        cons.EXCEL_STANDARD_FILE_PATH)
    manual_check.check_recent_segments()
    # 与之前的结果进行对比
    manual_check.contrast_segments()
    # 数据入库
    Excel2Mysql(
        cons.TEMPLATE_DISEASE_FILE_PATH,
        cons.EXCEL_RESULT_FOR_CHECK_PATH,
        cons.PRESENT_FILE_PATH
    ).excel2mysql()


if __name__ == '__main__':
    main()
