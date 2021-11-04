#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/29 10:31
# @File    : sentence_service.py
# @Software: Basebit
# @Description:
import re

import templateExtract.constant as cons
import templateExtract.config as conf


def get_sentence_extract_instance(sentence):
    """
    根据sentence，返回对应的解析实例
    :param sentence: 最小单元的一句话
    :return:
    """
    if '等' in str(sentence) and '不良情绪' in str(sentence):
        return SentenceExtractBase(sentence)
    elif '等' in str(sentence):
        return InfiniteEnumSentenceExtract(sentence)
    else:
        return SentenceExtractBase(sentence)


class SentenceExtractBase:
    """
    将句子解析为segments
    """

    def __init__(self, sentence):
        """
        :param sentence: [['，', 'x'], ['左右双', 'option'], ['侧', 'v'], ['侧下', 'n'], ['鼻甲', 'n'], ['有无', 'option'], ['肥大', 'a']]
        """
        self.sentence = sentence

    def extract(self):
        """
        sentence解析入口
        :return: [(segment, before_punctuation, after_punctuation, sentence_text), ...]
        """
        segments = []

        # 结构化短句sentence，提取选项，标点符号，展示内容等
        # 获取这段话开头，结尾的标点符号
        before_punctuation, after_punctuation = '', ''
        if self.sentence[0][1] == 'x':
            before_punctuation = self.sentence[0][0]
            self.sentence.pop(0)
        if self.sentence[-1][1] == 'x':
            after_punctuation = self.sentence[-1][0]
            self.sentence.pop(-1)

        # 初步结构化
        sentence_text = ''.join([i[0] for i in self.sentence])  # 供后续校验对比使用
        sen = self.sentence.copy()
        segment_temps = self._get_segment_levels(sen)
        # 如果没有指定type，则说明是一段纯文本，直接添加在display中
        if segment_temps and not segment_temps[0].get(cons.KEY_TYPE):
            display = sentence_text
            return [(None, before_punctuation, after_punctuation, sentence_text, display)]

        # 获取最终的segment
        for segment_temp in segment_temps:
            segment = self._get_segment(segment_temp, {})
            display = '{{{}}}'.format(segment[cons.KEY_LABEL])
            segments.append((segment, before_punctuation, after_punctuation, sentence_text, display))

        return segments

    def _get_segment(self, st, last_op):
        """
        获取最终的segment
        :param st:
        :param last_op: 上一层级的option
        :return:
        """
        if st[cons.KEY_TYPE] == cons.TYPE_TEXT:
            if last_op:
                last_op[cons.KEY_DISPLAY] += '{{{}}}'.format(st[cons.KEY_LABEL])
            return st
        elif st[cons.KEY_TYPE] == cons.TYPE_RADIO:
            return self._get_option_segment(st, last_op)

    def _get_option_segment(self, st, last_op):
        """
        解析选项类型的segment
        :param st: {'display': '{option}侧侧下鼻甲', 'option': '左右双', 'addition': [{'display': '{option}肥大', 'option': '有无'}]}
        :param last_op: 上一层级的option
        :return:
        """
        options = []
        display = st[cons.KEY_DISPLAY]  # '{option}侧侧下鼻甲'
        option = st[cons.AG_OPTION]
        addition = st.get(cons.KEY_ADDITION)
        label = self._get_label_name(label=st[cons.KEY_DISPLAY], option=option)

        # 解析选项
        if cons.SPLIT_TEXT in option:
            option_texts = option.split(cons.SPLIT_TEXT)
            # 如果已经解析出了option，默认按枚举值来看
            start_ind = 1
        else:
            option_texts, start_ind = conf.OPTION_MAP[option]

        for ind, opt in enumerate(option_texts):
            # 判断展示颜色
            color = self._get_display_color(start_ind, ind)

            option_temp = {
                cons.KEY_LABEL: opt,
                # 针对一些特殊的语法习俗，做特殊的处理
                cons.KEY_DISPLAY: display.format(
                    option=conf.SPECIAL_OPTION_DISPLAY.get(opt) if conf.SPECIAL_OPTION_DISPLAY.get(
                        opt) is not None else opt),
                cons.KEY_PROPS: {
                    cons.KEY_COLOR: color,
                },
                # 特殊：如果是阴阳，索引值从0开始；如果是枚举，则从1开始
                cons.KEY_VALUE: str(ind + start_ind),
            }
            if addition:
                addition_res = []
                for ad in addition:
                    addition_res.append(self._get_segment(ad, option_temp))
                option_temp[cons.KEY_ADDITION] = addition_res
            else:
                option_temp[cons.KEY_ADDITION] = None

            options.append(option_temp)

        if last_op:
            # 如果存在上一层级的option，则需要将本层级的label附加上去
            last_op[cons.KEY_DISPLAY] += '{{{}}}'.format(label)

        result = {
            cons.KEY_LABEL: label,
            cons.KEY_TYPE: st[cons.KEY_TYPE],
            # TODO：暂时以options的第一个为准，后面考虑怎么优化
            cons.KEY_VALUE: [options[0][cons.KEY_VALUE]],
            cons.KEY_OPTIONS: options,
        }

        return result

    def _get_display_color(self, start_ind, ind):
        """
        获取展示的颜色
        只做大概的推测，不一定准确，后续需要人工校验
        :param start_ind:
        :param ind:
        :return:
        """
        if start_ind == 0:
            if ind == 0:
                # 如果是阴阳，则第一位是绿色，其余为红色
                color = 'green'
            else:
                color = 'red'
        else:
            # 如果是枚举，默认是橘色
            color = 'orange'

        return color

    def _get_segment_levels(self, sentence):
        """
        获取segment的层级结构，方便后续的进一步处理
        TODO：待优化代码
        :param sentence: [['左右双', 'option'], ['侧', 'v'], ['侧下', 'n'], ['鼻甲', 'n'], ['有无', 'option'], ['肥大', 'a']]
        :return: [{'display': '{option}侧侧下鼻甲', 'option': '左右双', 'addition': [{'display': '{option}肥大', 'option': '有无'}]}]
        """
        st = {}
        display_temp = ''
        option_temp = ''

        # self.my_print('当前处理的短句为：{}'.format(sentence))
        while sentence:
            word = sentence.pop(0)
            # option对应的segment
            if word[1] == cons.AG_OPTION:
                # 如果存在选项，暂时写死为单选
                st[cons.KEY_TYPE] = cons.TYPE_RADIO

                # 保证至少存在option后才有addition
                if cons.OPTION_FORMAT in display_temp:
                    st[cons.KEY_DISPLAY] = display_temp
                    st[cons.AG_OPTION] = option_temp
                    sentence.insert(0, word)
                    st[cons.KEY_ADDITION] = self._get_segment_levels(sentence)
                else:
                    display_temp += cons.OPTION_FORMAT
                    option_temp = word[0]
            # text对应的segment
            # TODO：后续会结合前端进行优化，放在一个segment中
            elif word[1] == cons.AG_TEXT:
                # 为了兼容选项后，紧跟text的情况，需要判断之前是否已经有option了
                # Tanner分期G/B输入期
                if cons.OPTION_FORMAT in display_temp:
                    st[cons.KEY_DISPLAY] = display_temp
                    st[cons.AG_OPTION] = option_temp
                    sentence.insert(0, word)
                    st[cons.KEY_ADDITION] = self._get_segment_levels(sentence)
                else:
                    st[cons.KEY_TYPE] = cons.TYPE_TEXT
                    display_temp += '{}{}'.format(word[0], cons.SPLIT_TEXT) \
                        if word[0] in conf.RETAIN_TEXTS else cons.SPLIT_TEXT
            elif word[1] == cons.AG_DISPLAY:
                display_temp += word[0]
            # 其他类型的话，直接拼接字符串
            else:
                display_temp += word[0]

        # 对text类型特殊处理
        # 可能一句话要被拆分成多个segment。末次月经：[]年[]月[]日，需要拆分成3个。
        if st.get(cons.KEY_TYPE) == cons.TYPE_TEXT:
            segment_temps = self._get_text_segments(display_temp)
        # 对最后一轮数据的收尾
        else:
            if not st.get(cons.KEY_ADDITION):
                st[cons.KEY_DISPLAY] = display_temp
                st[cons.AG_OPTION] = option_temp
            segment_temps = [st]

        return segment_temps

    def _get_label_name(self, label=None, pre=None, post=None, option=None):
        """
        获取label名
        :param pre:
        :param post:
        :param label:
        :return:
        """
        if pre:
            label = re.sub('[:：]', '', pre)
        if label:
            label = re.sub(r'[{}]+'.format(cons.PUNCTUATION), '', label.replace(cons.OPTION_FORMAT, ''))
        label = label or pre or post or option.replace(cons.SPLIT_TEXT, '') or '待命名'
        return label

    def _get_text_segments(self, display):
        """
        解析text类型的segment
        总体思路是：从左往右遍历文本，第一次优先保证pre_text、post_text均有值
        :param display: 末次月经：~年~月~日
        :return:
        """

        def _build_segment(pre, post, label=None):

            return {
                cons.KEY_LABEL: self._get_label_name(pre=pre, post=post, label=label),
                cons.KEY_TYPE: cons.TYPE_TEXT,
                cons.KEY_VALUE: '',
                cons.KEY_FREETEXTPREFIX: pre,
                cons.KEY_FREETEXTPOSTFIX: post,
                cons.KEY_PLACEHOLDER: '',
                # cons.KEY_VALIDATION: [{
                #     cons.KEY_REGEX: '',
                #     cons.KEY_MESSAGE: ''
                # }]
            }

        segment_temps = []
        pre_text, post_text, position = '', '', 'left'

        for i in display:
            if i != cons.SPLIT_TEXT:
                # 如果是普通的文本，则往对应的文本中添加
                if position == 'left':
                    pre_text += i
                elif position == 'right':
                    post_text += i
            else:
                # 如果是待输入的文本，则改变光标position的位置
                position = 'right'
                if post_text:
                    segment_temps.append(_build_segment(pre_text, post_text))
                    pre_text, post_text = '', ''
        else:
            if not (pre_text or post_text):
                label = '输入'
            else:
                label = None
            segment_temps.append(_build_segment(pre_text, post_text, label))
        return segment_temps


class InfiniteEnumSentenceExtract(SentenceExtractBase):
    def extract(self):
        """
        获取无穷枚举类型的segment
        硬写代码
        :return:
        """
        # 供后续校验对比使用
        sentence_text = ''.join([i[0] for i in self.sentence])

        # 判断收尾的标点符号
        if self.sentence[0][1] == 'x':
            before_punctuation = self.sentence.pop(0)[0]
        else:
            before_punctuation = ''
        if self.sentence[-1][1] == 'x':
            after_punctuation = self.sentence.pop()[0]
        else:
            after_punctuation = ''

        # 获取选项
        enums = []
        enum = ''
        action_text = ''
        for word in self.sentence[1:]:
            if word[0] in conf.INFINITE_ENUM_FREFIX:
                action_text = word[0]
            elif word[1] != 'x' and word[0] != '等':
                enum += word[0]
            else:
                enums.append(enum)
                enum = ''
        else:
            suffix_text = enum

        # "无" 对应的segment
        segment1 = {
            cons.KEY_LABEL: '无',
            cons.KEY_DISPLAY: '无{}{}等{}'.format(action_text, '，'.join(enums), suffix_text),
            cons.KEY_PROPS: {
                cons.KEY_COLOR: 'green',
            },
            cons.KEY_ADDITION: None,
            cons.KEY_VALUE: '0',
        }

        # "有" 对应的segment
        child_key = ''.join(enums)
        addtion = [{
            cons.KEY_LABEL: child_key,
            cons.KEY_TYPE: 'CHECKBOX',
            cons.KEY_VALUE: ['1'],
            cons.KEY_OPTIONS: [{
                cons.KEY_LABEL: v,
                cons.KEY_DISPLAY: v,
                cons.KEY_PROPS: {
                    cons.KEY_COLOR: 'red',
                },
                cons.KEY_ADDITION: None,
                cons.KEY_VALUE: str(k + 1),  # 非阴阳，从1开始
            } for k, v in enumerate(enums)]
        }]
        addtion2 = {
            cons.KEY_LABEL: '其他',
            cons.KEY_DISPLAY: '其他：{自定义文本}',
            cons.KEY_PROPS: {
                cons.KEY_COLOR: 'red',
            },
            cons.KEY_ADDITION: [{
                cons.KEY_LABEL: '自定义文本',
                cons.KEY_TYPE: cons.TYPE_TEXT,
                cons.KEY_VALUE: '',
                cons.KEY_FREETEXTPREFIX: '',
                cons.KEY_FREETEXTPOSTFIX: '',
                cons.KEY_PLACEHOLDER: '',
                # cons.KEY_VALIDATION: [{
                #     cons.KEY_REGEX: '',
                #     cons.KEY_MESSAGE: ''
                # }]
            }],
            cons.KEY_VALUE: str(len(addtion[0][cons.KEY_OPTIONS]) + 1)
        }
        addtion[0][cons.KEY_OPTIONS].append(addtion2)

        segment2 = {
            cons.KEY_LABEL: '有',
            cons.KEY_DISPLAY: '有{}{{{}}}{}'.format(action_text, child_key, suffix_text),
            cons.KEY_PROPS: {
                cons.KEY_COLOR: 'red',
            },
            cons.KEY_ADDITION: addtion,
            cons.KEY_VALUE: '1',
        }
        segment = {
            cons.KEY_LABEL: '{}{}'.format(action_text, ''.join(enums)),
            cons.KEY_TYPE: cons.TYPE_RADIO,
            cons.KEY_VALUE: ['0'],
            cons.KEY_OPTIONS: [segment1, segment2]
        }
        display = '{{{}}}'.format(segment[cons.KEY_LABEL])

        return [(segment, before_punctuation, after_punctuation, sentence_text, display)]
