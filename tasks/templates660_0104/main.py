#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/29 15:22
# @File    : main.py
# @Software: Basebit
# @Description:
from services.manual_check_service import ManualCheck
from tasks.task_main import task_main
import tasks.templates660_0104.task_constant as cons


def only_check():
    manual_check = ManualCheck(
        cons.EXCEL_RESULT_FOR_CHECK_PATH,
        cons.EXTRACT_TEMPLATE_FILES,
        cons.EXCEL_STANDARD_FILE_PATH,
        cons.TEMPLATE_DISEASE_FILE_PATH
    )
    manual_check.manual_check_package()


if __name__ == '__main__':
    # task_main(
    #     template_disease_file_path=cons.TEMPLATE_DISEASE_FILE_PATH,
    #     excel_check_file_path=cons.EXCEL_RESULT_FOR_CHECK_PATH,
    #     present_file_path=cons.PRESENT_FILE_PATH,
    #     extract_template_files=cons.EXTRACT_TEMPLATE_FILES,
    #     standard_file_path=cons.EXCEL_STANDARD_FILE_PATH,
    #     template_path=cons.TEMPLATE_PATH,
    # )

    only_check()
