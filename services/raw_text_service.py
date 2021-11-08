#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/25 7:21 上午
# @File    : raw_text_service.py
# @Software: Basebit
# @Description:

import regex

import config as conf


def get_raw_text_extract_instance(type_name, paragraph_text):
    """
    根据raw_text，返回对应的解析实例
    :param type_name: 既往史、个人史……
    :param paragraph_text:
    :return:
    """
    return RawTextExtractBase(type_name, paragraph_text)


class RawTextExtractBase:

    def __init__(self, type_name, paragraph_text):
        """
        :param type_name: 既往史、个人史……
        :param paragraph_text:
        """
        self.type_name = type_name
        self.paragraph_text = paragraph_text

    def extract_blocks(self):
        """
        粗断句
        将原始文本，拆分成语句块
        :return:
        """
        # 针对一些特殊情况，修改源文本
        paragraph_text = self._block_pre_treatment(self.paragraph_text)
        # 默认以句号进行分句
        blocks = self._get_blocks_by_text(paragraph_text)

        blocks = [i for i in blocks if i.strip()]

        return blocks

    def _get_blocks_by_text(self, paragraph_text):
        """
        利用句号切分后，还需要保留句号，否则最终拼接不能还原，没办法直接用split
        :param paragraph_text:
        :return:
        """
        blocks = ['']
        for i in paragraph_text:
            blocks[-1] += i
            if i in ['。', '\n']:
                blocks.append('')
        # 此处不能去掉文中的空格，否则有些英文术语会出问题
        blocks = [i for i in blocks if i.strip()]

        return blocks

    def _block_pre_treatment(self, block):
        """
        针对一些特殊情况，对文本进行预处理
        :param block:
        :return:
        """
        print('预处理的文本：{}'.format(block))
        for cfg in conf.PRE_TREATMENT_CFG:
            sub_str = regex.findall(cfg['pat'], block)
            if sub_str:
                block = regex.sub(cfg['pat'], cfg['repl'], block)
                print('根据规则 “{}” ，将文本修改为：{}'.format(cfg['pat'], block))

        return block
