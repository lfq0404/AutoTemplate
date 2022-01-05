#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/21 11:40 上午
# @File    : pandas2excel.py
# @Software: Basebit
# @Description:
import json
import re

import pandas as pd
import more_itertools as mit
import constant as cons


def record2excel(output_file_path, datas: list):
    """
    将解析的数据放在Excel中
    可以按需要合并单元格
    :param output_file_path: 供后续程序读取的Excel路径
    :param datas:
    :return:
    """
    # 需要合并单元格的配置
    merge_cols = [
        {
            'col_name': '文件名',
            'col_num': 0
        },
        {
            'col_name': 'display',
            'col_num': 1
        },
        {
            'col_name': '原始段落',
            'col_num': 5
        },

    ]
    file_col = []
    display_col = []
    type_col = []  # 用于展示属于什么史
    label_col = []
    content_col = []
    sentence_text_col = []
    raw_text_col = []
    new_label_col = []
    new_content_col = []
    for file, paragraph_display, segments, raw_text in datas:
        type_name, display = re.findall('<b>(.*?)[:：]([\s\S]*?)</b>', paragraph_display)[0]
        if segments:
            for segment, sentence_text in segments:
                file_col.append(file)
                display_col.append(display)
                type_col.append(type_name)
                label_col.append(segment['label'])
                content_col.append(json.dumps(segment, ensure_ascii=False))
                sentence_text_col.append(sentence_text)
                raw_text_col.append(raw_text)
                new_label_col.append(None)
                new_content_col.append(None)
        else:
            # 如果没有segments，则表示直接原样返回模板的文本，不需要segment
            file_col.append(file)
            display_col.append(display)
            type_col.append(type_name)
            label_col.append('')
            content_col.append('')
            sentence_text_col.append('')
            raw_text_col.append(raw_text)
            new_label_col.append(None)
            new_content_col.append(None)

    df = pd.DataFrame({
        '文件名': file_col,
        'display': display_col,
        'label': label_col,
        'content': content_col,
        '原始短句': sentence_text_col,
        '原始段落': raw_text_col,
        '所属类型': type_col,
        'new_label': new_label_col,
        'new_content': new_content_col,
    })

    # 用于校验的
    df[['label', 'content', '原始短句']].drop_duplicates().to_excel(
        output_file_path.replace('.xlsx', 'distinct.xlsx'), sheet_name=cons.SHEET_NAME, index=False)
    # 用于查看的
    writer = pd.ExcelWriter(output_file_path, engine='xlsxwriter')
    df.to_excel(writer, sheet_name=cons.SHEET_NAME, index=False)
    workbook = writer.book
    worksheet = writer.sheets[cons.SHEET_NAME]

    file_format = workbook.add_format({
        'bold': True,
        'border': 1,  # 边框宽度
        'text_wrap': True,  # 自动换行
        'align': 'center',  # 水平居中
        'valign': 'vcenter',  # 垂直居中
        'fg_color': '#D7E4BC',  # 颜色填充
    })

    display_format = workbook.add_format({
        'bold': True,
        'align': 'center',
        'valign': 'top',
        'text_wrap': True,
        'border': 1,
        'fg_color': '#ADFAFE',
    })
    content_format = workbook.add_format({
        'bold': True,
        'align': 'left',
        'valign': 'top',
        'text_wrap': True,
        'border': 1
    })

    label_format = workbook.add_format({
        'align': 'left',
        'valign': 'top',
        'text_wrap': True,
        'border': 1
    })

    for merge_col in merge_cols:
        col_name = merge_col['col_name']
        col_num = merge_col['col_num']
        for car in df[col_name].unique():
            u = df.loc[df[col_name] == car].index.values + 1

            if len(u) >= 2:
                # 只merge连续表格
                for ut in [list(group) for group in mit.consecutive_groups(u)]:
                    if len(ut) > 1:
                        worksheet.merge_range(ut[0], col_num, ut[-1], col_num, df.loc[ut[0], col_name])

    worksheet.set_column('A:A', 50, file_format)
    worksheet.set_column('B:B', 50, display_format)
    worksheet.set_column('C:C', 20, label_format)
    worksheet.set_column('D:D', 75, content_format)
    worksheet.set_column('E:E', 50, content_format)
    worksheet.set_column('F:F', 50, content_format)
    worksheet.set_column('G:G', 50, content_format)

    writer.save()


if __name__ == '__main__':
    record2excel(
        'merge_test.xlsx',
        [
            ['脑病-气虚血瘀证(初诊)模板(4090100)脑病-气虚血瘀证(初诊)5d4d170e-6212-463e-aade-b123b2ec85a1.html',
             '<b>既往史：</b>',
             [],
             ''],
            ['脑病-气虚血瘀证(初诊)模板(4090100)脑病-气虚血瘀证(初诊)5d4d170e-6212-463e-aade-b123b2ec85a1.html',
             '<b>个人史：{平素体质}，{烟酒}</b>',
             [[{'label': '平素体质',
                'type': 'RADIO',
                'value': ['0'],
                'options': [{'label': '良好',
                             'display': '平素体质良好',
                             'props': {'color': 'green'},
                             'value': '0',
                             'addition': None},
                            {'label': '一般',
                             'display': '平素体质一般',
                             'props': {'color': 'red'},
                             'value': '1',
                             'addition': None}]},
               '平素体质一般'],
              [{'label': '烟酒',
                'type': 'RADIO',
                'value': ['0'],
                'options': [{'label': '无',
                             'display': '无烟，酒等不良嗜好',
                             'props': {'color': 'green'},
                             'addition': None,
                             'value': '0'},
                            {'label': '烟',
                             'display': '吸烟：时长{时长}年，频率{频率}支/天',
                             'props': {'color': 'red'},
                             'addition': [{'label': '时长',
                                           'type': 'TEXT',
                                           'value': '',
                                           'freetextPrefix': '',
                                           'freetextPostfix': '',
                                           'placeholder': ''},
                                          {'label': '频率',
                                           'type': 'TEXT',
                                           'value': '',
                                           'freetextPrefix': '',
                                           'freetextPostfix': '',
                                           'placeholder': ''}],
                             'value': '1'},
                            {'label': '酗酒',
                             'display': '酗酒：时长{时长}年，酒量{酒量}ml/天',
                             'props': {'color': 'red'},
                             'addition': [{'label': '时长',
                                           'type': 'TEXT',
                                           'value': '',
                                           'freetextPrefix': '',
                                           'freetextPostfix': '',
                                           'placeholder': ''},
                                          {'label': '酒量',
                                           'type': 'TEXT',
                                           'value': '',
                                           'freetextPrefix': '',
                                           'freetextPostfix': '',
                                           'placeholder': ''}],
                             'value': '2'}]},
               '有无烟、酒等不良嗜好']],
             '平素体质一般，无烟酒等特殊嗜好'],
        ]
    )
