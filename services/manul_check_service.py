#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/30 15:10
# @File    : manul_check_service.py
# @Software: Basebit
# @Description:
import json
import pandas

import constant as cons
from myUtils import read_excel


def check_segments(template_files=None):
    """check_segments
    获取人工修改后的segments
    :return:
    """
    update_segments = {}
    temp_repeat_labels = {}
    need_update = False
    not_care_labels = ['delete']

    datas = read_excel(cons.EXCEL_CHECK_FILE_PATH, cons.SHEET_NAME)
    for num, line in enumerate(datas.itertuples()):
        num += 1
        # 如果没有模板信息，则不管
        raw_content = line._4
        if pandas.isna(raw_content) or type(raw_content) is not str or '{' not in raw_content:
            continue
        # 只提取需要的文件
        if template_files and line._1 not in template_files:
            continue

        raw_label = line._3
        update_label = '' if pandas.isna(line._8) else line._8
        update_content = '' if pandas.isna(line._9) else line._9

        update_segments[raw_content] = {
            'raw_label': raw_label,
            'update_label': update_label,
            'update_content': update_content,
        }

        label = update_label or raw_label
        content = (update_content or raw_content).replace('\n', '').replace(' ', '')
        temp_repeat_labels.setdefault(label, [])
        for lines, v in temp_repeat_labels[label]:
            if content == v:
                lines.append(num)
                break
        else:
            temp_repeat_labels[label].append([[num], content])

    # 人工判读功能，与控制台交互
    for label, contents in temp_repeat_labels.items():
        if label in not_care_labels:
            continue
        if len(contents) > 1:
            need_update = True
            # {'[1, 3, 4]': content}
            line_infos = {}
            print('label = "{}"还存在多个segment：'.format(label))
            for i in contents:
                lines, c = i
                lines_text = json.dumps(lines)
                line_infos[lines_text] = c
                print(lines_text, c)
            print('------------------')
            update = False
            right_lines = input('请输入正确的行号们（没有请直接回车）：')
            if right_lines:
                for lines_text, _ in line_infos.items():
                    if lines_text == right_lines:
                        continue
                    for n in json.loads(lines_text):
                        datas.loc[n - 1][8] = line_infos[right_lines]
                print('label = "{}"合并成功1'.format(label))
                update = True
            else:
                right_content = input('请输入正确的内容（没有请直接回车）：')
                if right_content:
                    for lines_text in line_infos:
                        for n in json.loads(lines_text):
                            datas.loc[n - 1][8] = right_content
                    print('label = "{}"合并成功2'.format(label))
                    update = True

            if update:
                datas.to_excel(cons.EXCEL_CHECK_FILE_PATH, sheet_name=cons.SHEET_NAME, index=False, header=False)
            else:
                not_care_labels.append(label)

    not_care_labels.remove('delete')
    print('\n需要人工处理的labels：{}'.format(not_care_labels))
    if need_update:
        raise ValueError('请再次检查check_excel中的label与segment')

    return update_segments
