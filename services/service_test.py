#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/29 11:29
# @File    : test.py
# @Software: Basebit
# @Description:
import json

from services.block_service import get_block_extract_instance
from services.raw_text_service import get_raw_text_extract_instance
from services.sentence_service import get_sentence_extract_instance
import constant as cons

if __name__ == '__main__':
    paragraph_display = ''
    segments = []
    type_name = '个人史'
    text = '有无服用阿司匹林，波立维，华法林，泰嘉，利血平等。'
    text = '不详/无遗传性家族性疾病史/有阳性家族史'
    text = '患儿神志清/不清，呼吸平稳/急促，呼吸节律齐/不齐，吸凹征有/无，皮肤黏膜红润/苍白/发绀'
    text = '有/无突眼，甲状腺无/I度/II度/III度肿大，有/无血管杂音，咽部有/无充血，双扁桃体无/I度/II度/III度肿大，有/无分泌物；心音有力/低钝/遥远，心率输入次/分，心律齐/不齐，有/无杂音；两肺呼吸音清/粗，有/无湿啰音，有/无哮鸣音'
    text = '脊柱无畸形、无侧弯、无压痛、无直接叩击痛、无间接叩击痛、肋脊点肋腰点无压痛、肋脊角无叩击痛'
    text = '部可及一肿块，直径约 mm，边界，质地，形态'
    text = '有无高血压、脑梗塞、糖尿病、哮喘病史'
    text = '伸直 度，屈曲度，浮髌征，过伸试验，屈曲试验，麦氏征，内侧/外侧侧方应力试验 ，研磨试验。 '
    text = '左/右下肢足靴区/踝周可见毛细血管扩张，静脉曲屈及囊状隆起，伴皮炎、湿疹，瘙痒，色素沉着明显。'
    text = '术顺，术后监护血压 /mmHg，心率 次/分，留观半小时无殊后予离开诊室。术后无渣饮食三天，避免剧烈活动，忌烟酒，避免辛辣刺激饮食，如有腹痛便血及时就诊，1年后复查胃肠镜'
    text = '流行病学史：有无发病前2周内国内重点地区旅行史，时间：____'
    text = '''今以 2%利多卡因5ml/4%阿替卡因1.7ml 行局麻，拔　，远中龈切/去骨/分牙，顺利，置明胶海绵，纱布咬合，告医嘱。 '''
    text = ''' 
双眼结膜充血，角膜光泽，前房清，虹瞳好，晶体清，眼底：视盘边界清，网膜平伏，黄斑中心反光可见。 








 '''

    # type_name = '其他'
    # text = '已告知患者拔牙术可能的并发症、治疗风险、费用及其他注意事项，患者知情同意。术后医嘱详见拔牙注意事项。'
    # text = '术顺，术后监护血压 /mmHg，心率 次/分，留观半小时无殊后予离开诊室。术后无渣饮食三天，避免剧烈活动，忌烟酒，避免辛辣刺激饮食，如有腹痛便血及时就诊，1年后复查胃肠镜'
    # text = '门诊密切随访。非那雄胺*2盒，1粒QDPO；多沙唑嗪*2盒，1粒QNPO。入院手术，一月后复查泌尿彩超、尿流率、PSA，fPSA'

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
