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
import services.excel2mysql as excel2mysql
# 是否打印日志
from services.block_service import get_block_extract_instance
from services.sentence_service import get_sentence_extract_instance

# 是否将代码的解析结果，写入到Excel中
is_record = True
template_files = ['4431000-急诊发热-门诊病历(初诊)模板-门诊病历(初诊).html',
                  '4360127-九舍门诊眼科-门诊病历(复诊)-眼科(一般)-门诊病历(复诊).html',
                  '4360127-九舍门诊眼科-门诊病历(配药)-眼科-门诊病历(配药).html',
                  '0080600-护理专病门诊-PICC护理（常规护理）模板-门诊病历(配药).html',
                  '4360117-九舍门诊普内科-通用-配药-门诊病历(配药).html',
                  '4121601-门诊乳腺中心-门诊病历(配药)-乳腺癌辅助内分泌治疗-门诊病历(配药).html',
                  '4121601-门诊乳腺中心-门诊病历(复诊)-乳房肿块-门诊病历(复诊).html',
                  '4360117-九舍门诊普内科-通用-复诊-门诊病历(复诊).html',
                  '4121601-门诊乳腺中心-门诊病历(复诊)-乳腺增生-门诊病历(复诊).html',
                  '4350100-营养门诊-营养门诊病历(配药)-门诊病历(配药).html',
                  '0080600-护理专病门诊-PORT护理（常规护理）模板-门诊病历(配药).html',
                  '4121601-门诊乳腺中心-门诊病历(复诊)-乳腺癌术后-门诊病历(复诊).html',
                  '4121601-门诊乳腺中心-门诊病历(配药)-乳腺癌辅助化疗-门诊病历(配药).html',
                  '4200100-门诊产科-门诊病历(配药)简单-产科-门诊病历(配药).html',
                  '4280000-门诊推拿科-门诊病历(初诊)-颈型颈椎病-门诊病历(初诊).html',
                  '4121601-门诊乳腺中心-门诊病历(配药)-赫赛汀-门诊病历(配药).html',
                  '4240100-门诊口腔科-门诊病历(初诊)-龋齿牙体缺损-门诊病历(初诊).html',
                  '4270000-门诊针灸科-门诊病历(复诊)-腰痛-门诊病历(复诊).html',
                  '0080600-护理专病门诊-PICC护理（拔管护理）模板-门诊病历(配药).html',
                  '4270000-门诊针灸科-门诊病历(复诊)-颈椎病-门诊病历(复诊).html',
                  '4121601-门诊乳腺中心-门诊病历(初诊)-乳腺增生-门诊病历(初诊).html',
                  '4121601-门诊乳腺中心-门诊病历(配药)-乳腺癌新辅助化疗-门诊病历(配药).html',
                  '1010200-广慈门诊-通用-复诊-门诊病历(复诊).html',
                  '4300500-门诊疼痛-门诊病历(初诊)-无痛胃肠镜麻醉-门诊病历(初诊).html',
                  '4121601-门诊乳腺中心-门诊病历(配药)-乳腺癌靶向+化疗-门诊病历(配药).html',
                  '4270000-门诊针灸科-门诊病历(复诊)-肩关节痛-门诊病历(复诊).html',
                  '4270000-门诊针灸科-门诊病历(复诊)-周围性面瘫-门诊病历(复诊).html',
                  '4370500-特需门诊-门诊配药-特需内镜治疗-门诊病历(配药).html',
                  '4240100-门诊口腔科-门诊病历(初诊)-洗牙-门诊病历(初诊).html',
                  '4240100-门诊口腔科-门诊病历(初诊)-智齿阻生牙拔牙-门诊病历(初诊).html',
                  '4280000-门诊推拿科-门诊病历(初诊)-腰肌筋膜炎-门诊病历(初诊).html',
                  '4431000-急诊发热-门诊病历(复诊)模板-门诊病历(复诊).html',
                  '4270000-门诊针灸科-门诊病历(复诊)-膝关节痛-门诊病历(复诊).html',
                  '4280000-门诊推拿科-门诊病历(初诊)-腰椎间盘突出-门诊病历(初诊).html',
                  '4280000-门诊推拿科-门诊病历(初诊)-椎动脉型颈椎病-门诊病历(初诊).html',
                  '4121601-门诊乳腺中心-门诊病历(初诊)-乳房肿块-门诊病历(初诊).html',
                  '4240100-门诊口腔科-门诊病历(初诊)-牙髓炎-门诊病历(初诊).html',
                  '4280000-门诊推拿科-门诊病历(初诊)-神经根型颈椎病-门诊病历(初诊).html',
                  ]


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

            if file not in template_files:
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
                blocks = get_raw_text_extract_instance(type_name, text).extract()
                for block in blocks:
                    # 精分句，拆分成具有完整语义的句子
                    sentences = get_block_extract_instance(block).extract()
                    # 通过sentence获取segment
                    for sentence in sentences:
                        sgmts = get_sentence_extract_instance(sentence).extract()
                        # # 经过一系列处理，获取segments，及前后标点符号
                        # sgmts = block_instance.get_segments(sentences)
                        # 拼接segments
                        for sgmt in sgmts:
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
        if is_record:
            record2excel(cons.EXCEL_FILE_PATH, datas)

    check_segments(template_files)
    excel2mysql.main(template_files)


if __name__ == '__main__':
    main()
