#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/15 2:25 下午
# @File    : main.py
# @Software: Basebit
# @Description:
import os

from services.extract_core import RJExtract
from services.manual_check_service import check_recent_segments, contrast_segments
from services.pandas2excel import record2excel
import tasks.templates2_660.task_constant as cons


def code_extract(batch):
    """
    代码解析
    :return:
    """
    g = os.walk(cons.TEMPLATE_PATH)

    result = []
    for path, _, file_list in g:
        for ind, file in enumerate(file_list):
            # file = '门诊病历(初诊)-咯血(4100200)门诊病历(初诊)8b933a9b-f0ed-459f-8974-ce2e07d44568.html'
            extract = RJExtract(path, file, cons.TEMPLATE_BATCHES[batch])
            if extract.is_continue():
                print('文件不满足要求，不处理<{}>：{}'.format(ind, file))
                continue

            print('开始处理<{}>：{}'.format(ind, extract.file_path))
            file_result = extract.extract()
            result.extend(file_result)

    return result


def main(batch):
    """
    1、通过代码解析模板信息
    2、人工校验模板信息
    3、数据入库
    :return:
    """
    # reload = input('是否重新根据原始模板提取（y or n）：')
    reload = 'y'
    if reload == 'y':
        # 提取信息
        datas = code_extract(batch)
        # 保存到Excel中
        record2excel(cons.EXCEL_RESULT_FOR_LOOK_PATH, datas, cons.EXCEL_RESULT_FOR_CHECK_PATH)
    elif reload == 'n':
        pass
    else:
        raise ValueError('请输入正确的指令')

    # # 人工校验本次提取结果
    # check_recent_segments()
    # # 与之前的结果进行对比
    # contrast_segments()
    # # 数据入库
    # excel2mysql.main()


if __name__ == '__main__':
    batch = 1
    main(batch)
