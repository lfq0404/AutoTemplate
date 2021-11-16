#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/25 7:23 上午
# @File    : block_service.py
# @Software: Basebit
# @Description:
import re
import jieba
import jieba.posseg as psg

import constant as cons
import config as conf

# 读取自定义的词组
for word in conf.JIEBA_USER_WORDS:
    jieba.add_word(*word)
# 为了不拆分userword中的特殊字符。eg：中括号等
psg.re_han_internal = re.compile('([^°]+)', re.U)
jieba.re_userdict = re.compile('^(.+?)(\u0040\u0040[0-9]+)?(\u0040\u0040[a-z]+)?$', re.U)


def get_block_extract_instance(block):
    """
    根据block，返回对应的解析实例
    :param block: 根据句号断句后的text
    :return:
    """
    block = block.strip()

    # 特殊词组
    for search, words in conf.SPECIAL_WORDS:
        if search in block:
            return SpecialWordBlockExtract(block, [words])

    # 直接展示
    raw_words = []
    for display_text in conf.DISPLAY_SENTENCE_TEXTS:
        if display_text in block:
            raw_words.append(display_text)
    if raw_words:
        return DisplaySentenceBlockExtract(block, raw_words)

    return BlockExtractBase(block)


class BlockExtractBase:
    """
    将block拆分成完整语义的句子
    """

    def __init__(self, block):
        self.block = block

    def extract_sentences(self):
        """
        block解析入口方法
        :return:
        """
        # 利用结巴分词，获取词性
        block_cut = self.word_segment()
        # 通过block_cut，解析出语义独立的短句
        sentences = self.get_sentences_by_block_cut(block_cut)

        return sentences

    def word_segment(self):
        """
        默认利用jieba分词
        :return: [['有无', 'option'], ['手术史', 'n']]
        """
        block_cut = []
        if not self.block:
            return block_cut

        for k, v in psg.cut(self.block, HMM=False):
            if k in conf.NOT_BROKEN_SENTENCE:
                # 由于度数的单位 ° 在userdict中没法识别出来，在这里单独处理
                v = 'n'
            block_cut.append([k, v])

        return block_cut

    def get_sentences_by_block_cut(self, block_cut):
        """
        根据jieba的分词结果，进一步断句，拆分成短句
        保证一句话中至少：option >= 1 or text >= 1，且包含n
        :param block_cut:
        :return:
        """
        # 利用x预断句
        block_cut_temp = self._get_broken_sentences(block_cut)

        # 解析以特殊字符分割的选项
        block_cut = []
        for b in block_cut_temp:
            tmp = self._merge_option(b)
            block_cut.extend(tmp)

        # 保证一句话中至少：option >= 1 or text >= 1，且包含n（与名词有点关系的都可以）
        sentences = self._combo_independent_sentences(block_cut)

        return sentences

    def _combo_independent_sentences(self, block_cut):
        """
        组合具有完整语义的句子
        (有option or text) and 包括n and x为一句话
        :param block_cut:
        :return:
        """
        sentences = []
        # ag_sign: option text词性标识
        # part_sign: n,v,z词性标识
        sentence, ag_sign, part_sign = [], False, False
        for i in block_cut:
            if i[1] == cons.AG_DISPLAY:
                # 特殊处理：对直接display的处理
                sentences.append([i])
            else:
                # 通用逻辑
                if i[1] == cons.AG_OPTION:
                    ag_sign = True
                    part_sign = True
                elif i[1] == cons.AG_TEXT:
                    ag_sign = True
                elif 'n' in i[1] or 'v' in i[1] or 'z' in i[1]:
                    part_sign = True
                sentence.append(i)
                # 满足以下条件，默认是一段完整的句子
                if 'x' == i[1] and ag_sign and part_sign:
                    sentences.append(sentence)
                    sentence, ag_sign, part_sign = [], False, False
        else:
            # 对最后的循环判断
            # 如果结尾的短句没有标识，则添加到之前的最后一组
            if sentence:
                ags = [i[1] for i in sentence]
                # 如果短句存在选项、文本 并且 词性包括n or m，则作为新的一组
                if (cons.AG_OPTION in ags or cons.AG_TEXT in ags) and \
                        max(map(lambda x: 'n' in x or 'm' in x, ags)) is True:
                    sentences.append(sentence)
                else:
                    if sentences:
                        sentences[-1].extend(sentence)
                    else:
                        sentences.append(sentence)

        return sentences

    def _get_broken_sentences(self, block_cut):
        """
        将block_cut断句
        默认以 x 属性断句
        :param block_cut:
        :return:
        """
        sentences_tmp = [[]]
        for b in block_cut:
            sentences_tmp[-1].append(b)
            if b[1] == 'x':
                sentences_tmp.append([])

        sentences_tmp = [i for i in sentences_tmp if i]
        return sentences_tmp

    def _merge_option(self, sentence):
        """
        如果被OPTION_SPLITS分割，则判断为option
        若被拆分成多个词，则合并成一个
        :param sentence: [['鼻中隔', 'n'], ['左偏', 'd'], ['/', 'x'], ['右', 'f'], ['偏', 'd'], ['/', 'x'], ['居中', 'v']]
        :return: [['鼻中隔', 'n'], ['左偏|右偏|居中', 'option']]
        """
        for option_split in conf.OPTION_SPLITS:
            split_inds = [i for i, v in enumerate(sentence) if v[0] == option_split]
            last_ind = None
            split_ind = None
            for split_ind in split_inds:
                # 删除分隔符
                sentence[split_ind][1] = cons.AG_DEL

                if last_ind is None:
                    # 将第一个分割词左边的词性设置为option
                    sentence[split_ind - 1][1] = cons.AG_MERGE_OPTION
                    last_ind = split_ind
                elif split_ind - last_ind > 1:
                    # 如果两个分割词之间超过一个元素，则拼接多个元素
                    for ind in range(last_ind + 2, split_ind):
                        sentence[last_ind + 1][0] += sentence[ind][0]
                        sentence[ind][1] = cons.AG_DEL
                    else:
                        sentence[last_ind + 1][1] = cons.AG_MERGE_OPTION
                        last_ind = split_ind
            else:
                # 最后一个分割词右边的设置为option
                if split_ind:
                    if split_ind + 1 < len(sentence):
                        # 如果以/收尾，则不管
                        sentence[split_ind + 1][1] = cons.AG_MERGE_OPTION
                    # 如果原文为：不详/无遗传性家族性疾病史/有阳性家族性疾病史，则需要要“有”后面的“阳性家族性疾病史”纳入到选项中
                    end_ind = None
                    option_words = ''.join([i[0] for i in sentence if i[1] == cons.AG_MERGE_OPTION])
                    for i in range(split_ind + 2, len(sentence)):
                        if sentence[i][0] == 'x':
                            break
                        if sentence[i][0] in option_words:
                            end_ind = i
                    if end_ind:
                        for i in range(split_ind + 2, end_ind + 1):
                            sentence[split_ind + 1][0] += sentence[i][0]
                            sentence[i][1] = cons.AG_DEL

        # 合并ag_merge_option
        first_option_ind = None
        for ind, i in enumerate(sentence):
            if i[1] == cons.AG_MERGE_OPTION:
                if first_option_ind is None:
                    first_option_ind = ind
                    i[1] = cons.AG_OPTION
                else:
                    sentence[first_option_ind][0] += '{}{}'.format(cons.SPLIT_TEXT, i[0])
                    i[1] = cons.AG_DEL

        # 删除已经被合并的元素
        sentence = [i for i in sentence if i[1] != cons.AG_DEL]

        # 补丁：防止某些字没办法被jieba打标记
        # 注意：不能放在“合并ag_merge_option”中
        for i in sentence:
            if i[1] != cons.AG_OPTION and conf.OPTION_MAP.get(i[0]):
                i[1] = cons.AG_OPTION

        return sentence


class SpecialWordBlockExtract(BlockExtractBase):
    """
    特殊字符需要临时组合成词
    示例：
    不详/无遗传性家族性疾病史/有阳性家族史 --> 将“有阳性家族史”组成词组
    """

    def __init__(self, block, words):
        super(SpecialWordBlockExtract, self).__init__(block)
        self.words = words

    def word_segment(self):
        """
        默认利用jieba分词
        :return: [['有无', 'option'], ['手术史', 'n']]
        """
        for word in self.words:
            jieba.add_word(word[0], conf.DEFAULT_FREQUENCY, word[1])

        block_cut = super(SpecialWordBlockExtract, self).word_segment()

        for word in self.words:
            jieba.del_word(word[0])

        return block_cut


class DisplaySentenceBlockExtract(SpecialWordBlockExtract):
    """
    指定某些words用于display展示
    示例：
    末次月经[0]年[0]月[0]日，为了把“末次月经”与“年”拆开，将“末次月经”直接放在display中
    """

    def __init__(self, block, raw_words):
        super(SpecialWordBlockExtract, self).__init__(block)
        self.raw_words = raw_words
        self.words = [[i, 'n'] for i in raw_words]

    def word_segment(self):
        """
        利用jieba分词，给指定的字符打上标签
        :return: [['有无', 'option'], ['手术史', 'n']]
        """
        block_cut = super(DisplaySentenceBlockExtract, self).word_segment()
        for i in block_cut:
            if i[0] in self.raw_words:
                i[1] = cons.AG_DISPLAY
        return block_cut
