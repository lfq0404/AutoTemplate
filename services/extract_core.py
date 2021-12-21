#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/5 21:19
# @File    : extract_core.py
# @Software: Basebit
# @Description:
import json
import re

from html.parser import HTMLParser

import regex
from bs4 import BeautifulSoup

import config as conf
import constant as cons
from services.block_service import get_block_extract_instance
from services.raw_text_service import get_raw_text_extract_instance
from services.sentence_service import get_sentence_extract_instance


class ExtractCore:
    """
    针对文件的解析
    """

    def __init__(self, path, file_name):
        self.path = path  # 文件夹路径
        self.file_name = file_name  # HTML文件名
        self.file_path = '{}/{}'.format(path, file_name)

    def extract(self) -> list:
        """
        文件解析的入口函数
        :return:
        """
        result = []
        # 遍历各种史，提取信息
        for type_name, paragraph_text in self.paragraphs():
            paragraph_display = ''  # 既往史：{鼻腔}。{鼻中隔}。{间接鼻咽镜检查}。
            segments = []
            # 粗分句，且针对特殊内容预处理
            blocks = get_raw_text_extract_instance(type_name, paragraph_text).extract_blocks()
            for block in blocks:
                # 精分句，拆分成具有完整语义的句子
                sentences = get_block_extract_instance(block).extract_sentences()
                for sentence in sentences:
                    # 通过sentence获取segment，及前后标点符号
                    sgmts = get_sentence_extract_instance(sentence).extract_segments()
                    for sgmt in sgmts:
                        # 拼接segments
                        segment, before_punctuation, after_punctuation, sentence_text, display = sgmt
                        paragraph_display += '{}{}{}'.format(before_punctuation, display, after_punctuation)
                        if segment:
                            segments.append([segment, sentence_text])

            paragraph_display = '<b>{}：{}</b>'.format(type_name, paragraph_display)
            print(paragraph_display)
            print(json.dumps(segments, ensure_ascii=False))
            print()
            result.append([self.file_name, paragraph_display, segments, paragraph_text])

        return result

    def html_text(self):
        """
        HTML的纯文本内容
        """
        if True:
            # 可针对不同的文件添加不同的解析函数
            return HtmlParse(self.file_path).html2text()

    def paragraphs(self) -> list:
        """
        该文件的所有段落
        个人史、婚育史……为一个段落
        :return: [['现病史', text], ['个人史', text]]
        """
        html_text = self.html_text().replace('\n{', '{')
        result = {}
        # 末尾加回车，是为了保证能匹配到最后一行
        # 只要后面不是跟着 .*[:：] ，就继续匹配
        paragraphs = re.findall('(.*?[:：][\s\S]*?)\n(?=[\u4e00-\u9fa5]+[:：])', html_text + '\n')

        for ind, paragraph in enumerate(paragraphs):
            # 由于有较为灵活的断言，不能用自带的re模块
            for patt in conf.ERROR_MATCH_TEXTS:
                paragraph = regex.sub(patt, '', paragraph)

            # 只获取需要的文本块
            temp = re.findall('^([\u4e00-\u9fa5]+)[:：]?([\s\S]*)', paragraph)
            if temp and not re.search('(SPAN>|emr_reference)', temp[0][1]) and not re.search(
                    cons.NOT_EXTRACT_PARAGRAPHS, temp[0][0]):
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

    def is_continue(self):
        """
        是否继续下一个文件（跳过该文件）
        :return:
        """
        # 如果文件不是以HTML结尾，则忽略
        if not re.findall('^\d.*html', self.file_name):
            return True

        # 如果文件不在此次范围内，则忽略
        if conf.EXTRACT_TEMPLATE_FILES is not None and self.file_name not in conf.EXTRACT_TEMPLATE_FILES:
            return True


class HtmlParse(HTMLParser):
    def __init__(self, file_path):
        HTMLParser.__init__(self)
        self.__text = []
        self.file_path = file_path

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

    def html2text(self):
        """
        将HTML转为纯文本
        :return:
        """
        with open(self.file_path, 'r') as f:
            text = f.read()

        try:
            # 利用HTMLParser提取网页纯文本
            self.feed(text)
            self.close()
            text = self.text()
        except:
            # 利用bs提取
            text = self.beautifulsoup_extract(text)

        # 特殊替换
        for i in conf.HTML2TEXT_REPLACE:
            text = re.sub(i['pat'], i['repl'], text)

        return text

    @staticmethod
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


class BookExtractCore:
    """
    针对文件的解析
    """

    def __init__(self, path, file_name):
        self.path = path  # 文件夹路径
        self.file_name = file_name  # HTML文件名
        self.file_path = '{}/{}'.format(path, file_name)

    def extract(self) -> list:
        """
        文件解析的入口函数
        :return:
        """
        result = []
        with open(self.file_path, 'r') as f:
            for line in f.readlines():
                paragraph_display = ''
                segments = []
                # 精分句，拆分成具有完整语义的句子
                sentences = get_block_extract_instance(line).extract_sentences()
                for sentence in sentences:
                    # 通过sentence获取segment，及前后标点符号
                    sgmts = get_sentence_extract_instance(sentence).extract_segments()
                    for sgmt in sgmts:
                        # 拼接segments
                        segment, before_punctuation, after_punctuation, sentence_text, display = sgmt
                        paragraph_display += '{}{}{}'.format(before_punctuation, display, after_punctuation)
                        if segment:
                            segments.append([segment, sentence_text])
        # # 遍历各种史，提取信息
        # for type_name, paragraph_text in self.paragraphs():
        #     paragraph_display = ''  # 既往史：{鼻腔}。{鼻中隔}。{间接鼻咽镜检查}。
        #     segments = []
        #     # 粗分句，且针对特殊内容预处理
        #     blocks = get_raw_text_extract_instance(type_name, paragraph_text).extract_blocks()
        #     for block in blocks:
        #         # 精分句，拆分成具有完整语义的句子
        #         sentences = get_block_extract_instance(block).extract_sentences()
        #         for sentence in sentences:
        #             # 通过sentence获取segment，及前后标点符号
        #             sgmts = get_sentence_extract_instance(sentence).extract_segments()
        #             for sgmt in sgmts:
        #                 # 拼接segments
        #                 segment, before_punctuation, after_punctuation, sentence_text, display = sgmt
        #                 paragraph_display += '{}{}{}'.format(before_punctuation, display, after_punctuation)
        #                 if segment:
        #                     segments.append([segment, sentence_text])

        # paragraph_display = '<b>{}：{}</b>'.format(type_name, paragraph_display)
        # print(paragraph_display)
        # print(json.dumps(segments, ensure_ascii=False))
        # print()
        # result.append([self.file_name, paragraph_display, segments, paragraph_text])

        return result

    def is_continue(self):
        """
        是否继续下一个文件（跳过该文件）
        :return:
        """
        # 如果文件不是以HTML结尾，则忽略
        if not re.findall('.*txt$', self.file_name):
            return True
