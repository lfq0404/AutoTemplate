#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/15 3:27 下午
# @File    : constant.py
# @Software: Basebit
# @Description:
from string import punctuation as cn_punc
from zhon.hanzi import punctuation as zh_punc
import os

BASE_PATH = os.path.abspath(os.path.dirname(__file__))

# 暂时不需要抓取的段落
NOT_EXTRACT_PARAGRAPHS = '(现病史|主诉)'

PRESENT_NAME = '现病史'
PHYSICAL_NAME = '查体'
PAST_NAME = '既往史'
FAMILY_NAME = '家族史'
ALLERGY_NAME = '药物过敏史'
PERSONAL_NAME = '个人史'
MARRIAGEBIRTH_NAME = '婚育史'
MENSTRUAL_NAME = '月经史'
CUSTOM_NAME = '其他'

# 已知的分类，不在该map中的，统一放在custom中
KNOWN_CATEGORY_MAP = {
    PHYSICAL_NAME: 'PHYSICAL',
    PAST_NAME: 'PAST',
    FAMILY_NAME: 'FAMILY',
    ALLERGY_NAME: 'ALLERGY',
    PERSONAL_NAME: 'PERSONAL',
    MARRIAGEBIRTH_NAME: 'MARRIAGEBIRTH',
    MENSTRUAL_NAME: 'MENSTRUATION',
    PRESENT_NAME: 'PRESENT',
}

TABLE_PHYSICAL_SEGMENT = ['PHYSICAL']
TABLE_MEDICAL_HISTORY_SEGMENT = ['PAST', 'FAMILY', 'ALLERGY', 'PERSONAL', 'MARRIAGEBIRTH', 'MENSTRUATION']
TABLE_CUSTOM_SEGMENT = ['CUSTOM']
PACKAGE_COL_CATEGORY_MAP = {
    'PHYSICAL': 'physical_temp_id',
    'PAST': 'past_temp_id',
    'FAMILY': 'family_temp_id',
    'ALLERGY': 'allergy_temp_id',
    'PERSONAL': 'personal_temp_id',
    'MARRIAGEBIRTH': 'marriage_birth_temp_id',
    'MENSTRUATION': 'menstruation_temp_id',
    'CUSTOM': 'custom_temp_id',
    'PRESENT': 'present_temp_id',
}
# 用户自定义的文本块，直接返回text
CUSTOM_BLOCKS = [CUSTOM_NAME]

# 所有中英文的标点符号
PUNCTUATION = cn_punc + zh_punc

AG_DEL = 'del'  # 需要被删除的词性
AG_OPTION = 'option'  # 作为选项的词，与jiebadict的option一致
AG_TEXT = 'text'  # 作为自定义文本的词，与jiebadict的option一致
AG_MERGE_OPTION = 'mergge_option'  # 需要合并的option
AG_DISPLAY = 'display'  # 直接用于展示的内容
SPLIT_TEXT = '$'  # option之间的分隔符，找一个冷门的字符串。注：只能是一个字符
UNKNOW = 'unknow'  # 不知道怎么写，预填的值
OPTION_FORMAT = '{{{}}}'.format(AG_OPTION)

# segment的各种key
KEY_LABEL = 'label'
KEY_TYPE = 'type'
KEY_VALUE = 'value'
KEY_OPTIONS = 'options'
KEY_DISPLAY = 'display'
KEY_PROPS = 'props'
KEY_COLOR = 'color'
KEY_ADDITION = 'addition'
KEY_FREETEXTPOSTFIX = 'freetextPostfix'  # 在text框后面显示的内容
KEY_FREETEXTPREFIX = 'freetextPrefix'  # 在text框前面显示的内容
KEY_PLACEHOLDER = 'placeholder'
KEY_VALIDATION = 'validation'
KEY_REGEX = 'regex'
KEY_MESSAGE = 'message'

# segment的各种value
VALUE_TYPE_TEXT = 'TEXT'
VALUE_TYPE_RADIO = 'RADIO'
VALUE_TYPE_CHECKBOX = 'CHECKBOX'
VALUE_CUSTOM_TEXT = '自定义文本'

# 原始模板地址
RAW_TEMPLATES_PATH = '/Users/jeremy.li/Basebit/Documents/develop/smart/20211013-瑞金门急诊模板配置/rawTemplates'
# 输出的Excel
EXCEL_FILE_PATH = '{}/rj_templates.xlsx'.format(BASE_PATH)
EXCEL_CHECK_FILE_PATH = '{}/rj_check_templates.xlsx'.format(BASE_PATH)
EXCEL_STANDARD_FILE_PATH = '{}/rj_standard_templates.xlsx'.format(BASE_PATH)  # 人工判读后的标准数据
PRESENT_FILE_PATH = '{}/现病史解析记录.xlsx'.format(BASE_PATH)
TEMPLATE_DISEASE_FILE_PATH = '{}/近1年门诊常用科室模板与disease.xlsx'.format(BASE_PATH)
SHEET_NAME = '模板'

# DB配置
HOST = '172.18.0.114'
USER = 'generator'
PASSWORD = 'Generator@123'
DB_NAME = 'aiwizard_test'

HOST = 'localhost'
USER = 'root'
PASSWORD = 'a5300328'
DB_NAME = 'aiwizard_test'

