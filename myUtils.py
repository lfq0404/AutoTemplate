#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/15 2:26 下午
# @File    : myUtils.py
# @Software: Basebit
# @Description:
import re
import pandas

from regex import regex
from urllib.request import urlopen
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

    # 特殊替换 todo
    text = re.sub('有无\n', '有无', text)
    text = re.sub('\n地点', '地点', text)
    text = re.sub('\n四诊摘要', '四诊摘要', text)
    text = re.sub('个人史：流行病学史：', '个人史：\n流行病学史：', text)

    return text


def get_blocks_by_type(raw_text) -> dict:
    """
    将原始病例根据模块拆解
    :param raw_text:
    :return: {'现病史': text, '个人史': text, ……}
    """
    raw_text = raw_text.replace('\n{', '{')
    result = {}
    # 末尾加回车，是为了保证能匹配到最后一行
    # 只要后面不是跟着 .*[:：] ，就继续匹配
    blocks = re.findall('(.*?[:：][\s\S]*?)\n(?=[\u4e00-\u9fa5]+[:：])', raw_text + '\n')

    # '^(既往史|个人史|……)[:：]?([\s\S]*)'
    # patt = '^({})[:：]?([\s\S]*)'.format('|'.join(cons.TAKE_BLOCKS))
    for block in blocks:
        # 某些文本满足“只要后面不是跟着 .*[:：] ，就继续匹配”的规则，但实际是不需要的，删除
        # 由于有断言，不能用自带的re模块
        block = regex.sub('|'.join(conf.ERROR_MATCH_TEXTS), '', block)

        # 由于用BeautifulSoup将HTML转成文本，可能会存在多余的换行
        # # 只要在一个段落中，默认不换行
        # block = block.replace('\n', ' ')
        # 只获取需要的文本块
        temp = re.findall('^([\u4e00-\u9fa5]+)[:：]?([\s\S]*)', block)
        if temp and not re.search('(SPAN>|emr_reference)', temp[0][1]) and not re.search('(现病史|主诉)', temp[0][0]):
            temp = temp[0]
            result[temp[0]] = temp[1]

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
