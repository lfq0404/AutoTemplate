#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/15 2:25 下午
# @File    : main.py
# @Software: Basebit
# @Description:
import json
import os
import re

import myUtils
from services.raw_text_service import get_raw_text_extract_instance
from services.manul_check_service import check_segments
from services.pandas2excel import record2excel
import constant as cons
import config as conf
import services.excel2mysql as excel2mysql
# 是否打印日志
from services.block_service import get_block_extract_instance
from services.sentence_service import get_sentence_extract_instance


def code_extract():
    """
    代码解析
    :return:
    """
    g = os.walk(cons.RAW_TEMPLATES_PATH)

    result = []
    for path, _, file_list in g:
        for ind, file in enumerate(file_list):

            if not re.findall('^\d.*html', file):
                print('文件名不满足要求，不处理<{}>：{}'.format(ind, file))
                continue

            if file not in conf.EXTRACT_TEMPLATE_FILES:
                continue

            # file = '4240100-门诊口腔科-门诊病历(初诊)-智齿阻生牙拔牙-门诊病历(初诊).html'
            file_path = '{}/{}'.format(path, file)
            print('开始处理<{}>：{}'.format(ind, file_path))
            raw_text = myUtils.html2text(file_path)

            # 初步拆分文本，解析出文本块（个人史、婚育史……）
            raw_texts = myUtils.get_blocks_by_type(raw_text)

            # 遍历各种史，提取信息
            for type_name, text in raw_texts:
                paragraph_display = ''  # 既往史：{鼻腔}。{鼻中隔}。{间接鼻咽镜检查}。
                segments = []
                # 粗分句，且针对特殊内容补全文本
                blocks = get_raw_text_extract_instance(type_name, text).extract_blocks()
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
                result.append([file, paragraph_display, segments, text])

    return result


def main():
    """
    1、通过代码解析模板信息
    2、人工校验模板信息
    3、数据入库
    :return:
    """
    reload = input('是否重新根据原始模板提取（y or n）：')
    # reload = 'y'
    if reload == 'y':
        datas = code_extract()
        record2excel(cons.EXCEL_FILE_PATH, datas)
    elif reload == 'n':
        pass
    else:
        raise ValueError('请输入正确的指令')

    check_segments()
    excel2mysql.main()


if __name__ == '__main__':
    main()
