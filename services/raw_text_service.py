#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/25 7:21 上午
# @File    : raw_text_service.py
# @Software: Basebit
# @Description:

import regex

import templateExtract.config as conf


def get_raw_text_extract_instance(type_name, text):
    """
    根据raw_text，返回对应的解析实例
    :param type_name: 既往史、个人史……
    :param text:
    :return:
    """
    return RawTextExtractBase(type_name, text)


class RawTextExtractBase:

    def __init__(self, type_name, text):
        """
        :param type_name: 既往史、个人史……
        :param text:
        """
        self.type_name = type_name
        self.text = text

    def extract(self):
        """
        解析的入口方法，每个子类若有特殊情况，可以重写
        1、将原始段落，分成语句块block
        2、将block分词，进一步拆分成语义独立的句子sentence
        3、sentence继续拆分成多个segment
        【单选复选、颜色、默认值……暂时不能自动识别】
        :return:
        """
        # 针对一些特殊情况，修改源文本
        text = self._block_pre_treatment(self.text)
        # 默认以句号进行分句
        blocks = self._get_blocks_by_text(text)

        blocks = [i for i in blocks if i.strip()]

        return blocks

    def _get_blocks_by_text(self, text):
        """
        利用句号切分后，还需要保留句号，否则最终拼接不能还原，没办法直接用split
        :param text:
        :return:
        """
        blocks = ['']
        for i in text:
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


if __name__ == '__main__':
    # 用于测试
    text = '有无浅表淋巴结肿大，部位直径'
    # text = '体温输入℃'
    # text = 'HR88次/分，律齐。'
    # text = '1）皮肤科门诊或周一上午痤疮专病门诊随访 2）忌食辛辣刺激甜食3）保证睡眠避免熬夜 4）（建议）妇科门诊就诊排除多囊卵巢的可能。'
    text.replace(' ', '')
    get_raw_text_extract_instance('个人史', text).extract()
