#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/15 2:26 下午
# @File    : myUtils.py
# @Software: Basebit
# @Description:
import re
import pandas

from regex import regex
from html.parser import HTMLParser
from bs4 import BeautifulSoup

import constant as cons
import config as conf


class _DeHTMLParser(HTMLParser):
    """
    利用HTMLParser提取网页纯文本
    """

    def __init__(self):
        HTMLParser.__init__(self)
        self.__text = []

    def handle_data(self, data):
        text = data.strip()
        if len(text) > 0:
            text = re.sub('[ \t\r\n]+', ' ', text)
            self.__text.append(text + ' ')

    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            self.__text.append('\n\n')
        elif tag == 'br':
            self.__text.append('\n')
        elif tag == 'div':
            self.__text.append('\n')

    def handle_startendtag(self, tag, attrs):
        if tag == 'br':
            self.__text.append('\n\n')

    def text(self):
        return ''.join(self.__text).strip()


def beautifulsoup_extract(text):
    """
    利用BeautifulSoup提取网页纯文本
    :param text:
    :return:
    """
    soup = BeautifulSoup(text, features="html.parser")
    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()  # rip it out

    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip()
              for line in lines
              for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join("".join(chunk.split()) for chunk in chunks if chunk)

    return text


def html2text(html_file):
    """
    将HTML转为纯文本
    :param html_file:
    :return:
    """
    with open(html_file, 'r') as f:
        text = f.read()

    try:
        parser = _DeHTMLParser()
        parser.feed(text)
        parser.close()
        text = parser.text()
    except:
        soup = BeautifulSoup(text, 'html.parser')
        text = soup.text

    # 特殊替换
    for i in conf.HTML2TEXT_REPLACE:
        text = re.sub(i['pat'], i['repl'], text)

    return text


def get_blocks_by_type(raw_text) -> list:
    """
    将原始病例根据模块拆解
    :param raw_text:
    :return: [['现病史', text], ['个人史', text]]
    """
    raw_text = raw_text.replace('\n{', '{')
    result = {}
    # 末尾加回车，是为了保证能匹配到最后一行
    # 只要后面不是跟着 .*[:：] ，就继续匹配
    blocks = re.findall('(.*?[:：][\s\S]*?)\n(?=[\u4e00-\u9fa5]+[:：])', raw_text + '\n')

    # '^(既往史|个人史|……)[:：]?([\s\S]*)'
    # patt = '^({})[:：]?([\s\S]*)'.format('|'.join(cons.TAKE_BLOCKS))
    for ind, block in enumerate(blocks):
        # 某些文本满足“只要后面不是跟着 .*[:：] ，就继续匹配”的规则，但实际是不需要的，删除
        # 由于有断言，不能用自带的re模块
        block = regex.sub('|'.join(conf.ERROR_MATCH_TEXTS), '', block)

        # 只获取需要的文本块
        temp = re.findall('^([\u4e00-\u9fa5]+)[:：]?([\s\S]*)', block)
        if temp and not re.search('(SPAN>|emr_reference)', temp[0][1]) and not re.search('(现病史|主诉)', temp[0][0]):
            temp = temp[0]
            result[(ind, temp[0])] = temp[1]

    # 如果某些未知的分类夹杂在已知分类中，需要与上一个分类合并
    # ----
    # 个人史：
    # 流行病学史：xxx
    # 婚育史：
    # ---
    # 则需要把“流行病学史”放在“个人史”后
    last_known_sign = False
    del_keys = []
    need_merge_keys = []
    for key in sorted([i for i in result.keys()], key=lambda x: x[0], reverse=True):
        _, category_name = key
        if category_name in cons.KNOWN_CATEGORY_MAP:
            last_known_sign = True
        if last_known_sign and category_name not in cons.KNOWN_CATEGORY_MAP:
            # 记录待合并的key
            need_merge_keys.append(key)
        if last_known_sign and category_name in cons.KNOWN_CATEGORY_MAP and need_merge_keys:
            # 分类合并
            for need_merge_key in need_merge_keys:
                result[key] += '\n{}：{}'.format(need_merge_key[1], result[need_merge_key])
            del_keys.extend(need_merge_keys)
            need_merge_keys = []

    result = {k: v for k, v in result.items() if k not in del_keys}
    result = sorted([[k[1], v] for k, v in result.items()], key=lambda x: x[0])
    return result


def read_excel(file_path, sheet_name):
    """
    读取Excel
    :param file_path:
    :param sheet_name:
    :return:
    """
    datas = pandas.read_excel(file_path, sheet_name=sheet_name, header=None, engine='openpyxl')
    return datas


def department_statistics():
    """
    根据科室进行统计
    :return:
    """
    datas = read_excel(cons.EXCEL_FILE_PATH, cons.SHEET_NAME)
    result = {}
    files = set()
    for line in datas.itertuples():
        file_name = line._1
        if '-' not in file_name:
            continue
        files.add(file_name)
    for file_name in files:
        department = re.findall('.+?-(.+?)-', file_name)[0]
        tmp = result.get(department)
        if not tmp:
            result[department] = {
                '总数': 0,
                '初诊': 0,
                '复诊': 0,
                '配药': 0,
                '其他': 0,
            }
        if '初诊' in file_name:
            result[department]['初诊'] += 1
        elif '复诊' in file_name:
            result[department]['复诊'] += 1
        elif '配药' in file_name:
            result[department]['配药'] += 1
        else:
            result[department]['其他'] += 1
        result[department]['总数'] += 1

    print(result)


def reverse_delete_sqls():
    """
    将SQL顺序反转打印
    """
    text = """delete from department where id = 4090100;
delete from virtual_department where id = 209;
delete from department_mapping where id = 505;
"""
    sqls = text.split(';')
    for sql in sqls[::-1]:
        if sql:
            print(sql.replace('\n', ''), ';')
