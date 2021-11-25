#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/22 16:27
# @File    : constant.py
# @Software: Basebit
# @Description: 针对pdf2text的常量
import os

BASE_PATH = os.path.abspath(os.path.dirname(__file__))

# 书本结构化的参数
LEFT_MIN_PIXEL = 150  # 文字左侧距离纸张的最小值
RIGHT_MAX_PIXEL = 1800  # 文字右侧的最大值
TOP_MIN_PIXEL = 295  # 文字上沿距离纸张的最小值
BOTTOM_MAX_PIXEL = 2810  # 文字下沿的最大值
SPACE_MIN_PIXEL = 53  # 超过该值，中间则插入空格
Y_ALLOW_FLOAT_PIXEL = 20  # y坐标允许浮动的值，在该范围内，视为同一行，否则换行
VALID_PAGES = {
    range(173 - 1, 237): '西医',
    range(269 - 1, 300): '中西医',
}

TITLES = [
    '病史',
    '体格检查',
    '专科情况',
    '辅助检查'
]

PRETREATMENT_PATTS = [
    {
        'patt': '无 有',
        'repl': '无|有*补全*',
    },
    {
        'patt': '无 有',
        'repl': '无|有*补全*',
    },

]