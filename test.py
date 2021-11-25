import copy
import json
import re

import pandas
import pandas as pd


#
# text = """
# 475 {"label":"皮肤","type":"RADIO","value":["1"],"options":[{"label":"局部","display":"局部皮肤{充盈}","props":{"color":"orange"},"value":"1","addition":[{"label":"充盈","type":"RADIO","value":["1"],"options":[{"label":"正常","display":"正常充盈","props":{"color":"orange"},"value":"1","addition":null},{"label":"擦伤","display":"擦伤充盈","props":{"color":"orange"},"value":"2","addition":null},{"label":"红肿","display":"红肿充盈","props":{"color":"orange"},"value":"3","addition":null},{"label":"皮温升高","display":"皮温升高充盈","props":{"color":"orange"},"value":"4","addition":null},{"label":"静脉","display":"静脉充盈","props":{"color":"orange"},"value":"5","addition":null}]}]}]}
# 1259 {"label":"皮肤","type":"RADIO","value":["1"],"options":[{"label":"局部","display":"局部皮肤{红肿}","props":{"color":"orange"},"value":"1","addition":[{"label":"红肿","type":"RADIO","value":["1"],"options":[{"label":"有","display":"有红肿","props":{"color":"orange"},"value":"1","addition":null},{"label":"无","display":"无红肿","props":{"color":"orange"},"value":"2","addition":null}]}]}]}
# """
#
# a = text.split('\n')
# result = set()
# for i in a:
#     if not i:
#         continue
#     _, segment = i.split(' ')
#     segment = json.loads(segment)
#
#     for x in segment.get('options', []):
#         addition = x.get('addition')
#         if addition:
#             for ad in addition:
#                 for op in ad.get('options', []):
#                     result.add(op['display'])
#         else:
#             result.add(x['label'])
# print(result)
#
# text = """{"label":"血管疾病史","type":"RADIO","value":["1"],"options":[{"label":"无","display":"无血管疾病史","props":{"color":"orange"},"value":"1","addition":null},{"label":"有","display":"有血管疾病史","props":{"color":"orange"},"value":"2","addition":null}]}"""
# a = json.loads(text)
# a['value'] = ['0']
# a['options'][0]['props']['color'] = 'red'
# a['options'][1]['props']['color'] = 'green'
# a['options'][1]['value'] = '0'
# # a['options'] = a['options'][::-1]
# print(json.dumps(a, ensure_ascii=False))


# import regex
#
# texts = [
#     ['有无高血压、糖尿病史', '有无高血压、糖尿病史等'],
#     ['有无高血压、糖尿病史等', '有无高血压、糖尿病史等'],
#     ['有无高血压、糖尿病', '有无高血压、糖尿病等'],
#     ['有无高血压、糖尿病等', '有无高血压、糖尿病等'],
#     ['有高血压、心脏病、糖尿病史、脑梗塞史，常规服药，控制良好。', '有高血压、心脏病、糖尿病史、脑梗塞史等，常规服药，控制良好。'],
#     ['有高血压、心脏病、糖尿病史、脑梗塞史等，常规服药，控制良好。', '有高血压、心脏病、糖尿病史、脑梗塞史等，常规服药，控制良好。'],
#     ['有高血压、心脏病、糖尿病史、脑梗塞，常规服药，控制良好。', '有高血压、心脏病、糖尿病史、脑梗塞等，常规服药，控制良好。'],
#     ['有高血压、心脏病、糖尿病史、脑梗塞等，常规服药，控制良好。', '有高血压、心脏病、糖尿病史、脑梗塞等，常规服药，控制良好。'],
#     ['有高血压、糖尿病史、脑梗塞史、心脏病，常规服药，控制良好。', '有高血压、糖尿病史、脑梗塞史、心脏病等，常规服药，控制良好。'],
#     # ['有高血压，糖尿病史，脑梗塞史，心脏病，常规服药，控制良好。', '有高血压，糖尿病史，脑梗塞史，心脏病等，常规服药，控制良好。'],
#     ['有高血压、糖尿病史、脑梗塞史、心脏病等，常规服药，控制良好。', '有高血压、糖尿病史、脑梗塞史、心脏病等，常规服药，控制良好。'],
#     # ['有高血压，糖尿病史，脑梗塞史，心脏病等，常规服药，控制良好。', '有高血压，糖尿病史，脑梗塞史，心脏病等，常规服药，控制良好。'],
#     ['有高血压。', '有高血压。'],
#     ['有高血压，常规服药，控制良好。', '有高血压，常规服药，控制良好。'],
# ]
# for text, right in texts:
#     raw_text = text
#     for pat in [
#         '(?<=、)(高血压|脑梗塞|糖尿病|哮喘病|心脏病)(?![史、等])',
#         '(?<=、)(高血压史|脑梗塞史|糖尿病史|哮喘病史|心脏病史)(?![、等])',
#     ]:
#         text = regex.sub(pat, r'\1等', text)
#     assert text == right, '{} --> {}'.format(raw_text, text)
from myUtils import read_excel


def get_entities(raw_json):
    for v in raw_json.values():
        for i in v:
            print('content为：{}'.format(i['content']))
            for ind, entity in enumerate(i['entity_list']):
                print(ind, entity['text'])
                for x in entity['misc']['deco']:
                    print('deco - ', x)
                for x in entity['misc']['tags']:
                    print('tags - ', x)


import os

all_htmls = ['4360105-九舍门诊耳鼻喉科-门诊病历(初诊)-鼻部疾病1-门诊病历(初诊).html', '4290100-门诊康复科-门诊病历(初诊)-粘连性肩关节囊炎-门诊病历(初诊).html',
             '4280000-门诊推拿科-门诊病历(初诊)-腰肌筋膜炎-门诊病历(初诊).html', '4100200-门诊儿内-门诊病历(复诊)-矮小症-门诊病历(复诊).html',
             '4250100-门诊耳鼻咽喉科-门诊病历(初诊)-腮腺肿物-门诊病历(初诊).html', '4360117-九舍门诊普内科-皮肤粘膜出血-高干复诊-门诊病历(复诊).html',
             '4270000-门诊针灸科-门诊病历(复诊)-腰痛-门诊病历(复诊).html', '4090100-门诊中医内科-肺系疾病-肺肾两虚证(初诊)模板-门诊病历(初诊).html',
             '4360109-九舍门诊骨科-门诊病历(初诊)-痛风性关节炎-门诊病历(初诊).html', '4360117-九舍门诊普内科-贫血-高干复诊-门诊病历(复诊).html',
             '4121601-门诊乳腺中心-门诊病历(复诊)-乳腺钙化灶-门诊病历(复诊).html', '4260100-门诊皮肤科-痤疮脱发(初诊)模板-门诊病历(初诊).html',
             '4360117-九舍门诊普内科-急性呼吸道感染-初诊-门诊病历(初诊).html', '1010200-广慈门诊-门诊病历(初诊)-门诊病历(初诊).html',
             '4350100-营养门诊-营养门诊病历(配药)-门诊病历(配药).html', '4250100-门诊耳鼻咽喉科-门诊病历(初诊)-鼻前庭囊肿-门诊病历(初诊).html',
             '4050100-门诊血液-白细胞减少(复诊)-门诊病历(复诊).html', '4240100-门诊口腔科-门诊病历(初诊)-义齿修复-门诊病历(初诊).html',
             '4160100-门诊烧伤整形-门诊病历(配药)-灼伤换药-门诊病历(配药).html', '4121601-门诊乳腺中心-门诊病历(配药)-乳腺癌新辅助内分泌治疗-门诊病历(配药).html',
             '4090200-门诊中医外科-银屑病-白疕(初诊)模板-门诊病历(初诊).html', '4250100-门诊耳鼻咽喉科-门诊病历(初诊)-慢性鼻窦炎-门诊病历(初诊).html',
             '4350100-营养门诊-营养门诊病历(初诊)-门诊病历(初诊).html', '4121800-门诊肿瘤-门诊病历(复诊)-晚期肿瘤-门诊病历(复诊).html',
             '1010200-广慈门诊-门诊病历(配药)-门诊病历(配药).html', '4090100-门诊中医内科-肺系疾病-肺阴亏耗证(复诊)模板-门诊病历(复诊).html',
             '4370503-特需体检-门诊病历(初诊)-特需体检(男)-门诊病历(初诊).html', '4100200-门诊儿内-门诊病历(初诊)-甲亢危象-门诊病历(初诊).html',
             '4090100-门诊中医内科-中医内科(初诊)模板-门诊病历(初诊).html', '4260100-门诊皮肤科-银屑病(复诊)模板-门诊病历(复诊).html',
             '4050100-门诊血液-贫血(初诊)-门诊病历(初诊).html', '4121601-门诊乳腺中心-门诊病历(配药)-乳腺癌新辅助化疗-门诊病历(配药).html',
             '4100200-门诊儿内-门诊病历(初诊)-糖尿病酮症-门诊病历(初诊).html', '4050100-门诊血液-血小板减少(复诊)-门诊病历(复诊).html',
             '4060100-门诊神内-门诊病历(配药)-复杂-门诊病历(配药).html', '4090100-门诊中医内科-胃恶性肿瘤气血两虚证(初诊)模板-门诊病历(初诊).html',
             '4090200-门诊中医外科-湿疹(初诊)模板-门诊病历(初诊).html', '4360106-九舍门诊妇科-门诊病历(初诊)-停经-门诊病历(初诊).html',
             '4121601-门诊乳腺中心-门诊病历(初诊)-乳腺增生-门诊病历(初诊).html', '4090100-门诊中医内科-心系疾病-痰热壅盛证(初诊)模板-门诊病历(初诊).html',
             '4360105-九舍门诊耳鼻喉科-门诊病历(初诊)-颈部疾病-门诊病历(初诊).html', '4250100-门诊耳鼻咽喉科-门诊病历(初诊)-声带白斑-门诊病历(初诊).html',
             '0080600-护理专病门诊-常规造口护理(复诊)模板-门诊病历(复诊).html', '4100200-门诊儿内-门诊病历(初诊)-血友病-门诊病历(初诊).html',
             '4121601-门诊乳腺中心-门诊病历(初诊)-拉帕替尼-门诊病历(初诊).html', '4320100-门诊心理科-门诊病历(初诊)-抑郁焦虑状态-门诊病历(初诊).html',
             '4060100-门诊神内-门诊病历(复诊)_神内-门诊病历(复诊).html', '4180100-门诊伤科-门诊病历(复诊)-门诊病历(复诊).html',
             '4250100-门诊耳鼻咽喉科-门诊病历(初诊)-会厌囊肿-门诊病历(初诊).html', '4090100-门诊中医内科-心系疾病-气阴两虚证(初诊)模板-门诊病历(初诊).html',
             '4300500-门诊疼痛-门诊病历(初诊)-麻醉评估-门诊病历(初诊).html', '4250100-门诊耳鼻咽喉科-门诊病历(初诊)-声带麻痹-门诊病历(初诊).html',
             '1010200-广慈门诊-通用-复诊-门诊病历(复诊).html', '4090100-门诊中医内科-脑病-脉络空虚、风邪入中证(初诊)模板-门诊病历(初诊).html',
             '4280000-门诊推拿科-门诊病历(初诊)-急性腰扭伤-门诊病历(初诊).html', '4090100-门诊中医内科-结肠恶性肿瘤肝气乘脾证(复诊)模板-门诊病历(复诊).html',
             '4250100-门诊耳鼻咽喉科-门诊病历(初诊)-慢性咽炎-门诊病历(初诊).html', '4090100-门诊中医内科-脑病-肝肾阴虚、风阳上扰证(复诊)模板-门诊病历(复诊).html',
             '4360127-九舍门诊眼科-门诊病历(初诊)-眼科(详细)-门诊病历(初诊).html', '4260100-门诊皮肤科-皮肤护理专病(复诊)模板-门诊病历(复诊).html',
             '4300500-门诊疼痛-门诊病历(配药)-开具麻醉药品-门诊病历(配药).html', '4360117-九舍门诊普内科-头晕-初诊-门诊病历(初诊).html',
             '4050100-门诊血液-慢粒靶向药物(初诊)-门诊病历(初诊).html', '4090100-门诊中医内科-月经病——气血两亏型(初诊)模板-门诊病历(初诊).html',
             '4360117-九舍门诊普内科-急性呼吸道感染-高干复诊-门诊病历(复诊).html', '0080600-护理专病门诊-门诊护理（配造口产品）模板-门诊病历(初诊).html',
             '4100200-门诊儿内-门诊病历(初诊)-性早熟（男童）-门诊病历(初诊).html', '4090100-门诊中医内科-淋巴瘤气血两虚证(初诊)模板-门诊病历(初诊).html',
             '4090100-门诊中医内科-心系疾病-气血两虚证(复诊)模板-门诊病历(复诊).html', '4240100-门诊口腔科-门诊病历(复诊)-种植（复诊拆线）-门诊病历(复诊).html',
             '0080600-护理专病门诊-配静脉护理产品模板-门诊病历(配药).html', '4161101-门诊创面修复中心-门诊病历(初诊)-外伤性溃疡-门诊病历(初诊).html',
             '4360113-九舍门诊口腔科-门诊病历(复诊)-根充-门诊病历(复诊).html', '4360106-九舍门诊妇科-门诊病历(初诊)-腹痛-门诊病历(初诊).html',
             '4090100-门诊中医内科-脑病-肝阳上抗证(初诊)模板-门诊病历(初诊).html', '4360117-九舍门诊普内科-甲状腺结节-高干复诊-门诊病历(复诊).html',
             '4090100-门诊中医内科-结肠恶性肿瘤气滞血瘀证(复诊)模板-门诊病历(复诊).html', '4360106-九舍门诊妇科-门诊病历(空白页)-临时-门诊病历(补充续打).html',
             '4090100-门诊中医内科-月经病——血寒型(复诊)模板-门诊病历(复诊).html', '4090200-门诊中医外科-带状疱疹(复诊)模板-门诊病历(复诊).html',
             '4431000-急诊发热-门诊病历(复诊)模板-门诊病历(复诊).html', '4090100-门诊中医内科-胃恶性肿瘤胃阴不足证(初诊)模板-门诊病历(初诊).html',
             '0080600-护理专病门诊-PORT护理（常规护理）模板-门诊病历(配药).html', '4090100-门诊中医内科-淋巴瘤痰瘀互结证(初诊)模板-门诊病历(初诊).html',
             '4200200-门诊妇科-门诊病历(初诊)-妇产科-门诊病历(初诊).html', '1010200-广慈门诊-门诊病历(空白页)-门诊病历(补充续打).html',
             '4360117-九舍门诊普内科-高血压-高干复诊-门诊病历(复诊).html', '4100200-门诊儿内-门诊病历(初诊)-胸闷-门诊病历(初诊).html',
             '4360117-九舍门诊普内科-腹泻-初诊-门诊病历(初诊).html', '4360114-九舍门诊泌外-门诊病历(初诊)-前列腺增生-门诊病历(初诊).html',
             '4090100-门诊中医内科-心系疾病-水饮凌心证(初诊)模板-门诊病历(初诊).html', '4270000-门诊针灸科-门诊病历(初诊)-颈椎痛-门诊病历(初诊).html',
             '4360117-九舍门诊普内科-皮肤粘膜出血-初诊-门诊病历(初诊).html', '4360117-九舍门诊普内科-通用-复诊-门诊病历(复诊).html',
             '4360117-九舍门诊普内科-上腹痛-初诊-门诊病历(初诊).html', '4200100-门诊产科-门诊病历(复诊2)-产科-门诊病历(复诊).html',
             '4100200-门诊儿内-门诊病历(复诊)模板-门诊病历(复诊).html', '4090100-门诊中医内科-胃恶性肿瘤脾气亏虚证(初诊)模板-门诊病历(初诊).html',
             '4090100-门诊中医内科-结肠恶性肿瘤脾肾阳虚证(初诊)模板-门诊病历(初诊).html', '4360113-九舍门诊口腔科-门诊病历(初诊)-肿块-门诊病历(初诊).html',
             '4270000-门诊针灸科-门诊病历(初诊)-黄斑变性-门诊病历(初诊).html', '4090200-门诊中医外科-痤疮-粉刺(复诊)模板-门诊病历(复诊).html',
             '4201500-门诊生殖中心-门诊病历(复诊)模板-门诊病历(复诊).html', '4230100-门诊眼科-门诊病历(初诊)-激光角膜屈光手术-门诊病历(初诊).html',
             '4360105-九舍门诊耳鼻喉科-门诊病历(初诊)-喉部疾病-门诊病历(初诊).html', '4090100-门诊中医内科-淋巴瘤气郁痰凝证(复诊)模板-门诊病历(复诊).html',
             '4360113-九舍门诊口腔科-门诊病历(初诊)-RCT(牙髓炎根尖周炎)-门诊病历(初诊).html', '4121601-门诊乳腺中心-门诊病历(配药)-乳腺癌辅助化疗-门诊病历(配药).html',
             '4090100-门诊中医内科-血瘀证(复诊)模板-门诊病历(复诊).html', '4090100-门诊中医内科-心系疾病-瘀血阻络证(初诊)模板-门诊病历(初诊).html',
             '4180100-门诊伤科-门诊病历(复诊)模板-门诊病历(复诊).html', '4270000-门诊针灸科-门诊病历(配药)-鼻窦炎-门诊病历(配药).html',
             '4200200-门诊妇科-门诊病历(空白页)模板-门诊病历(补充续打).html', '4230100-门诊眼科-门诊病历(复诊)-激光角膜屈光手术术后复查-门诊病历(复诊).html',
             '4100200-门诊儿内-门诊病历(初诊)-甲状腺炎-门诊病历(初诊).html', '4190100-骨科-腰背痛及骨关节炎-门诊病历(初诊).html', 'xs.html',
             '4360113-九舍门诊口腔科-门诊病历(初诊)-拔牙-门诊病历(初诊).html', '4100200-门诊儿内-门诊病历(初诊)-腹痛-门诊病历(初诊).html',
             '4270000-门诊针灸科-门诊病历(复诊)-胃痛-门诊病历(复诊).html', '4090100-门诊中医内科-肺系疾病-痰湿蕴肺证(复诊)模板-门诊病历(复诊).html',
             '4090100-门诊中医内科-直肠恶性肿瘤湿热下注证(复诊)模板-门诊病历(复诊).html', '4100200-门诊儿内-门诊病历(复诊)-复诊-门诊病历(复诊).html',
             '4360109-九舍门诊骨科-门诊病历(初诊)-桡骨茎突腱鞘炎-门诊病历(初诊).html', '4250100-门诊耳鼻咽喉科-门诊病历(初诊)-咽部乳头状瘤-门诊病历(初诊).html',
             '4140100-门诊泌外-门诊病历(配药)模板-门诊病历(配药).html', '4250100-门诊耳鼻咽喉科-门诊病历(初诊)-特发性突聋-门诊病历(初诊).html',
             '4090100-门诊中医内科-气滞证(初诊)模板-门诊病历(初诊).html', '4090100-门诊中医内科-胃恶性肿瘤肝胃不和证(复诊)模板-门诊病历(复诊).html',
             '4250100-门诊耳鼻咽喉科-门诊病历(初诊)-鼻咽癌-门诊病历(初诊).html', '4200200-门诊妇科-门诊病历(初诊)模板-门诊病历(初诊).html',
             '4250100-门诊耳鼻咽喉科-门诊病历(初诊)-急性会厌炎-门诊病历(初诊).html', '4221500-胰腺外一-门诊病历(复诊)-门诊病历(复诊).html',
             '4090100-门诊中医内科-直肠恶性肿瘤气血两虚证(复诊)模板-门诊病历(复诊).html', '4090100-门诊中医内科-阴虚证(复诊)模板-门诊病历(复诊).html',
             '4250100-门诊耳鼻咽喉科-门诊病历(初诊)-小儿OSAHS-门诊病历(初诊).html',
             '4250100-门诊耳鼻咽喉科-门诊病历(初诊)-颈部肿块(淋巴结转移癌)-门诊病历(初诊).html', '4201500-门诊生殖中心-门诊病历(初诊)-门诊病历(初诊).html',
             '4360114-九舍门诊泌外-门诊病历(初诊)-早泄-门诊病历(初诊).html', '4240100-门诊口腔科-门诊病历(复诊)-拆线（复诊）-门诊病历(复诊).html',
             '4360109-九舍门诊骨科-门诊病历(初诊)-膝痛-门诊病历(初诊).html', '4100200-门诊儿内-门诊病历(初诊)-剧烈啼哭-门诊病历(初诊).html',
             '4360117-九舍门诊普内科-呕吐-高干复诊-门诊病历(复诊).html', '4360117-九舍门诊普内科-慢性阻塞性肺病急性加重-高干复诊-门诊病历(复诊).html',
             '4090100-门诊中医内科-气虚证(初诊)模板-门诊病历(初诊).html', '0080600-护理专病门诊-门诊病历(配造口产品)模板-门诊病历(补充续打).html',
             '4180100-门诊伤科-门诊病历(初诊)-颈痛-门诊病历(初诊).html', '4100200-门诊儿内-门诊病历(初诊)-尿路感染-门诊病历(初诊).html',
             '4360117-九舍门诊普内科-冠心病心绞痛-初诊-门诊病历(初诊).html', '4090100-门诊中医内科-结肠恶性肿瘤气滞血瘀证(初诊)模板-门诊病历(初诊).html',
             '4280000-门诊推拿科-门诊病历(初诊)-椎动脉型颈椎病-门诊病历(初诊).html', '4270000-门诊针灸科-门诊病历(复诊)-颈椎病-门诊病历(复诊).html',
             '4090100-门诊中医内科-月经病——血寒型(初诊)模板-门诊病历(初诊).html', '4090200-门诊中医外科-带状疱疹(初诊)模板-门诊病历(初诊).html',
             '4161101-门诊创面修复中心-门诊病历(初诊)-下肢静脉性溃疡-门诊病历(初诊).html', '4431000-急诊发热-门诊病历(初诊)模板-门诊病历(初诊).html',
             '4090100-门诊中医内科-胃恶性肿瘤胃阴不足证(复诊)模板-门诊病历(复诊).html', '4360117-九舍门诊普内科-骨质疏松-高干复诊-门诊病历(复诊).html',
             '4090100-门诊中医内科-淋巴瘤痰瘀互结证(复诊)模板-门诊病历(复诊).html', '4250100-门诊耳鼻咽喉科-门诊病历(初诊)-外耳道真菌-门诊病历(初诊).html',
             '4250100-门诊耳鼻咽喉科-门诊病历(初诊)-外耳道炎-门诊病历(初诊).html', '4370500-特需门诊-门诊配药-特需内镜治疗-门诊病历(配药).html',
             '4250100-门诊耳鼻咽喉科-门诊病历(初诊)-急性扁桃体炎-门诊病历(初诊).html', '4090100-门诊中医内科-月经病——气血两亏型(复诊)模板-门诊病历(复诊).html',
             '4360117-九舍门诊普内科-呕血-高干复诊-门诊病历(复诊).html', '4360117-九舍门诊普内科-2型糖尿病-高干复诊-门诊病历(复诊).html',
             '4070100-门诊呼吸科-呼吸科门诊(复诊)-门诊病历(复诊).html', '4260100-门诊皮肤科-皮肤护理(复诊)模板-门诊病历(复诊).html',
             '4360109-九舍门诊骨科-门诊病历(初诊)-扁平足-门诊病历(初诊).html', '4090100-门诊中医内科-心系疾病-气血两虚证(初诊)模板-门诊病历(初诊).html',
             '4090100-门诊中医内科-淋巴瘤气血两虚证(复诊)模板-门诊病历(复诊).html', '4240100-门诊口腔科-门诊病历(配药)-简易病史（代配药）-门诊病历(配药).html',
             '4200100-门诊产科-门诊病历(初诊)-产科-门诊病历(初诊).html', '4120200-门诊普外-门诊病历(初诊)-胰腺-门诊病历(初诊).html',
             '4201500-门诊生殖中心-门诊病历(空白页)模板-门诊病历(补充续打).html', '4240100-门诊口腔科-门诊病历(初诊)-智齿阻生牙拔牙-门诊病历(初诊).html',
             '4090100-门诊中医内科-脑病-肝阳上抗证(复诊)模板-门诊病历(复诊).html', '4090100-门诊中医内科-结肠恶性肿瘤脾肾阳虚证(复诊)模板-门诊病历(复诊).html',
             '4121601-门诊乳腺中心-门诊病历(初诊)-乳腺癌辅助化疗-门诊病历(初诊).html', '4360114-九舍门诊泌外-门诊病历(初诊)-慢性前列腺炎-门诊病历(初诊).html',
             '4360127-九舍门诊眼科-门诊病历(复诊)-眼科-门诊病历(复诊).html', '4090200-门诊中医外科-痤疮-粉刺(初诊)模板-门诊病历(初诊).html',
             '4090100-门诊中医内科-门诊病历(复诊)模板-门诊病历(复诊).html', '4090100-门诊中医内科-淋巴瘤气郁痰凝证(初诊)模板-门诊病历(初诊).html',
             '4200100-门诊产科-门诊病历(复诊1)-产科-门诊病历(复诊).html', '4360117-九舍门诊普内科-便血-高干复诊-门诊病历(复诊).html',
             '4280000-门诊推拿科-门诊病历(初诊)-腕管综合征-门诊病历(初诊).html', '4090100-门诊中医内科-血瘀证(初诊)模板-门诊病历(初诊).html',
             '4180100-门诊伤科-颈痛-门诊病历(初诊)-门诊病历(初诊).html', '0080600-护理专病门诊-配造口产品-门诊病历(配药).html',
             '4090100-门诊中医内科-心系疾病-水饮凌心证(复诊)模板-门诊病历(复诊).html', '4360117-九舍门诊普内科-骨质疏松-初诊-门诊病历(初诊).html',
             '4250100-门诊耳鼻咽喉科-门诊病历(初诊)-变应性鼻炎-门诊病历(初诊).html', '4260100-门诊皮肤科-皮肤淋巴瘤(初诊)模板-门诊病历(初诊).html',
             '4360117-九舍门诊普内科-呕吐-初诊-门诊病历(初诊).html', '4090100-门诊中医内科-胃恶性肿瘤脾气亏虚证(复诊)模板-门诊病历(复诊).html',
             '4100200-门诊儿内-门诊病历(初诊)模板-门诊病历(初诊).html', '4360106-九舍门诊妇科-门诊病历(初诊)-妇科通用-门诊病历(初诊).html',
             '0080600-护理专病门诊-PICC护理（拔管护理）模板-门诊病历(配药).html', '4360109-九舍门诊骨科-门诊病历(初诊)-胸腰椎椎管狭窄-门诊病历(初诊).html',
             '4240100-门诊口腔科-门诊病历(初诊)-牙髓炎-门诊病历(初诊).html', '4090100-门诊中医内科-直肠恶性肿瘤湿热下注证(初诊)模板-门诊病历(初诊).html',
             '4100200-门诊儿内-儿科门诊(初诊)-门诊病历(初诊).html', '4090100-门诊中医内科-肺系疾病-痰湿蕴肺证(初诊)模板-门诊病历(初诊).html',
             '4180100-门诊伤科-腰痛-门诊病历(初诊)-门诊病历(初诊).html', '4160100-门诊烧伤整形-门诊病历(复诊)-灼伤-门诊病历(复诊).html',
             '4121601-门诊乳腺中心-门诊病历(配药)-乳腺癌靶向+化疗-门诊病历(配药).html', '4090100-门诊中医内科-气滞证(复诊)模板-门诊病历(复诊).html',
             '4090100-门诊中医内科-胃恶性肿瘤肝胃不和证(初诊)模板-门诊病历(初诊).html', '4090100-门诊中医内科-直肠恶性肿瘤气血两虚证(初诊)模板-门诊病历(初诊).html',
             '4360133-九舍门诊推拿-门诊病历(初诊)-推拿科-门诊病历(初诊).html', '4090100-门诊中医内科-心系疾病-瘀血阻络证(复诊)模板-门诊病历(复诊).html',
             '4200200-门诊妇科-门诊病历(初诊)-计划生育手术门诊病史-门诊病历(初诊).html', '4360109-九舍门诊骨科-门诊病历(初诊)-肩关节外伤-门诊病历(初诊).html',
             '4121601-门诊乳腺中心-门诊病历(初诊)-乳腺钙化灶-门诊病历(初诊).html', '4360105-九舍门诊耳鼻喉科-门诊病历(初诊)-鼻部-门诊病历(初诊).html',
             '4121601-门诊乳腺中心-门诊病历(复诊)-乳头溢液-门诊病历(复诊).html', '4180100-门诊伤科-门诊病历(初诊)-膝痛-门诊病历(初诊).html',
             '4090100-门诊中医内科-气虚证(复诊)模板-门诊病历(复诊).html', '4201500-门诊生殖中心-门诊病历(简易配药)-门诊病历(配药).html',
             '1010100-广慈办公室-消化内科(复诊)-门诊病历(复诊).html', '4260100-门诊皮肤科-发热性皮疹药疹(初诊)模板-门诊病历(初诊).html',
             '4090100-门诊中医内科-阴虚证(初诊)模板-门诊病历(初诊).html', '4250100-门诊耳鼻咽喉科-门诊病历(初诊)-鳃裂囊肿-门诊病历(初诊).html',
             '0080600-护理专病门诊-PICC护理（常规护理）模板-门诊病历(配药).html', '4201500-门诊生殖中心-门诊病历(妊娠保胎)-门诊病历(配药).html',
             '4270000-门诊针灸科-门诊病历(初诊)-耳鸣-门诊病历(初诊).html', '4100200-门诊儿内-门诊病历(初诊)-肥胖-门诊病历(初诊).html',
             '4270000-门诊针灸科-门诊病历(初诊)-支气管炎-门诊病历(初诊).html', '4090100-门诊中医内科-肺系疾病-肺肾两虚证(复诊)模板-门诊病历(复诊).html',
             '4100200-门诊儿内-门诊病历(初诊)-咳嗽-门诊病历(初诊).html', '4270000-门诊针灸科-门诊病历(复诊)-通用-门诊病历(复诊).html',
             '4360114-九舍门诊泌外-门诊病历(初诊)-肾上腺疾病-门诊病历(初诊).html', '4360113-九舍门诊口腔科-门诊病历(初诊)-洗牙-门诊病历(初诊).html',
             '4280000-门诊推拿科-门诊病历(初诊)-高脂血症-门诊病历(初诊).html', '4270000-门诊针灸科-门诊病历(配药)模板-门诊病历(配药).html',
             '4121601-门诊乳腺中心-门诊病历(复诊)-乳房肿块-门诊病历(复诊).html', '4240100-门诊口腔科-门诊病历(复诊)-RCT（复诊充填）-门诊病历(复诊).html',
             '4270000-门诊针灸科-门诊病历(初诊)-膝关节痛-门诊病历(初诊).html', '4240100-门诊口腔科-门诊病历(初诊)-根尖周炎-门诊病历(初诊).html',
             '4240100-门诊口腔科-门诊病历(复诊)-种植（复诊义齿修复）-门诊病历(复诊).html', '4360113-九舍门诊口腔科-门诊病历(初诊)-补牙(龋齿牙体缺损)-门诊病历(初诊).html',
             '0080600-护理专病门诊-门诊病历(配造口产品)模板-门诊病历(复诊).html', '4090100-门诊中医内科-肺系疾病-肺阴亏耗证(初诊)模板-门诊病历(初诊).html',
             '4270000-门诊针灸科-门诊病历(复诊)-甲状腺炎-门诊病历(复诊).html', '4200100-门诊产科-门诊病历(配药)复杂-产科-门诊病历(配药).html',
             '4360117-九舍门诊普内科-腹泻-高干复诊-门诊病历(复诊).html', '4260100-门诊皮肤科-银屑病(初诊)模板-门诊病历(初诊).html',
             '4270000-门诊针灸科-门诊病历(复诊)-鼻窦炎-门诊病历(复诊).html', '4280000-门诊推拿科-门诊病历(初诊)-神经根型颈椎病-门诊病历(初诊).html',
             '4360116-九舍门诊皮肤科-门诊病历(初诊)-一般模板-门诊病历(初诊).html', '4180100-门诊伤科-门诊病历(初诊)-肩痛-门诊病历(初诊).html',
             '4360117-九舍门诊普内科-冠心病心绞痛-高干复诊-门诊病历(复诊).html', '4090200-门诊中医外科-银屑病-白疕(复诊)模板-门诊病历(复诊).html',
             '4360106-九舍门诊妇科-门诊病历(初诊)-盆腔肿块-门诊病历(初诊).html', '4250100-门诊耳鼻咽喉科-门诊病历(初诊)-鼻中隔偏曲-门诊病历(初诊).html',
             '4360113-九舍门诊口腔科-门诊病历(初诊)-外伤-门诊病历(初诊).html', '4090100-门诊中医内科-心系疾病-痰热壅盛证(复诊)模板-门诊病历(复诊).html',
             '4250100-门诊耳鼻咽喉科-门诊病历(初诊)-腺样体肥大-门诊病历(初诊).html', '4121601-门诊乳腺中心-门诊病历(初诊)-赫赛汀-门诊病历(初诊).html',
             '4280000-门诊推拿科-门诊病历(初诊)-颈型颈椎病-门诊病历(初诊).html', '4250100-门诊耳鼻咽喉科-门诊病历(初诊)-喉咽恶性肿瘤-门诊病历(初诊).html',
             '4180100-门诊伤科-门诊病历(初诊)-腰痛-门诊病历(初诊).html', '4240100-门诊口腔科-门诊病历(复诊)-RCT（复诊换药）-门诊病历(复诊).html',
             '4050100-门诊血液-淋巴结肿大(初诊)-门诊病历(初诊).html', '4270000-门诊针灸科-门诊病历(初诊)-慢性前列腺增生-门诊病历(初诊).html',
             '4090200-门诊中医外科-湿疹(复诊)模板-门诊病历(复诊).html', '4090100-门诊中医内科-胃恶性肿瘤气血两虚证(复诊)模板-门诊病历(复诊).html',
             '4280000-门诊推拿科-门诊病历(初诊)-踝关节扭伤-门诊病历(初诊).html', '4360117-九舍门诊普内科-通用-初诊-门诊病历(初诊).html',
             '4121800-门诊肿瘤-门诊病历(配药)-门诊病历(配药).html', '4100200-门诊儿内-门诊病历(初诊)-呕吐-门诊病历(初诊).html',
             '4280000-门诊推拿科-门诊病历(初诊)-腰椎小关节滑膜嵌顿-门诊病历(初诊).html', '4121601-门诊乳腺中心-门诊病历(初诊)-氟维司群-门诊病历(初诊).html',
             '1010200-广慈门诊-检查外科(初诊)模板-门诊病历(初诊).html', '4020100-门诊心脏-心内-病窦(初诊)-门诊病历(初诊).html',
             '4090100-门诊中医内科-结肠恶性肿瘤肝气乘脾证(初诊)模板-门诊病历(初诊).html', '4090100-门诊中医内科-脑病-脉络空虚、风邪入中证(复诊)模板-门诊病历(复诊).html',
             '4090100-门诊中医内科-脑病-肝肾阴虚、风阳上扰证(初诊)模板-门诊病历(初诊).html', '4360129-九舍门诊中医内-门诊病历(初诊)-中医-门诊病历(初诊).html',
             '4260100-门诊皮肤科-皮肤护理专病(初诊)模板-门诊病历(初诊).html', '4360105-九舍门诊耳鼻喉科-门诊病历(初诊)-耳部-门诊病历(初诊).html',
             '4240100-门诊口腔科-门诊病历(初诊)-口腔溃疡粘膜病-门诊病历(初诊).html', '4090100-门诊中医内科-心系疾病-气阴两虚证(复诊)模板-门诊病历(复诊).html',
             '1010100-广慈办公室-上腹不适(初诊)-门诊病历(初诊).html', '4100200-门诊儿内-门诊病历(初诊)-呕血-门诊病历(初诊).html',
             '4250100-门诊耳鼻咽喉科-门诊病历(初诊)-急性中耳炎-门诊病历(初诊).html', '4300500-门诊疼痛-门诊病历(初诊)-带状疱疹-门诊病历(初诊).html',
             '4360105-九舍门诊耳鼻喉科-门诊病历(初诊)-耳部疾病1-门诊病历(初诊).html', '4270000-门诊针灸科-门诊病历(初诊)-肩关节痛-门诊病历(初诊).html',
             '4100200-门诊儿内-门诊病历(初诊)-胸痛-门诊病历(初诊).html', '4121601-门诊乳腺中心-门诊病历(初诊)-乳腺癌新辅助内分泌治疗-门诊病历(初诊).html',
             '4161101-门诊创面修复中心-门诊病历(初诊)-医源性创面-门诊病历(初诊).html', '4090100-门诊中医内科-结肠恶性肿瘤湿热下注证(初诊)模板-门诊病历(初诊).html',
             '4201500-门诊生殖中心-门诊病历(监测排卵)-门诊病历(配药).html', '4090100-门诊中医内科-淋巴瘤肝肾阴虚证(复诊)模板-门诊病历(复诊).html',
             '4360106-九舍门诊妇科-门诊病历(复诊)-停经-门诊病历(复诊).html', '4100200-门诊儿内-门诊病历(初诊)-甲亢-门诊病历(初诊).html',
             '4360114-九舍门诊泌外-门诊病历(初诊)-肾癌-门诊病历(初诊).html', '4360114-九舍门诊泌外-门诊病历(初诊)-膀胱癌-门诊病历(初诊).html',
             '4090100-门诊中医内科-月经病——血热型(复诊)模板-门诊病历(复诊).html', '1010200-广慈门诊-检查内科(女)(初诊)模板-门诊病历(初诊).html',
             '4300500-门诊疼痛-门诊病历(初诊)-膝关节疼痛-门诊病历(初诊).html', '4090100-门诊中医内科-结肠恶性肿瘤气血两虚证(初诊)模板-门诊病历(初诊).html',
             '4360117-九舍门诊普内科-贫血-初诊-门诊病历(初诊).html', '4201500-门诊生殖中心-门诊病历(复诊)-门诊病历(复诊).html',
             '4121601-门诊乳腺中心-门诊病历(初诊)-乳腺癌靶向+化疗-门诊病历(初诊).html',
             '3060100-门诊超声-门诊病历(复诊)-甲状腺良性结节恶性肿瘤射频消融-门诊病历(复诊).html', '4280000-门诊推拿科-门诊病历(初诊)-骶髂关节错位-门诊病历(初诊).html',
             '4090100-门诊中医内科-痰湿证(初诊)模板-门诊病历(初诊).html', '4230100-门诊眼科-门诊病历(复诊)-激光角膜屈光手术术前复诊-门诊病历(复诊).html',
             '4060100-门诊神内-门诊病历(初诊)_神内-门诊病历(初诊).html', '4360109-九舍门诊骨科-门诊病历(初诊)-踝关节扭伤-门诊病历(初诊).html',
             '4121601-门诊乳腺中心-门诊病历(复诊)-乳腺增生-门诊病历(复诊).html', '4221500-胰腺外一-门诊病历(初诊)-门诊病历(初诊).html',
             '4240100-门诊口腔科-门诊病历(初诊)-冠周炎（智齿其他初诊）-门诊病历(初诊).html', '4090100-门诊中医内科-血虚证(复诊)模板-门诊病历(复诊).html',
             '4090100-门诊中医内科-月经病——气滞血瘀型(初诊)模板-门诊病历(初诊).html', '4320100-门诊心理科-门诊病历(初诊)-强迫状态-门诊病历(初诊).html',
             '4160100-门诊烧伤整形-门诊病历(初诊)-灼伤后疤痕-门诊病历(初诊).html', '4360106-九舍门诊妇科-门诊病历(初诊)-妇科炎症-门诊病历(初诊).html',
             '4270000-门诊针灸科-门诊病历(初诊)-鼻窦炎-门诊病历(初诊).html', '4360117-九舍门诊普内科-甲状腺结节-初诊-门诊病历(初诊).html',
             '4090100-门诊中医内科-胃恶性肿瘤脾虚痰湿证(复诊)模板-门诊病历(复诊).html', '4240100-门诊口腔科-门诊病历(初诊)-种植-门诊病历(初诊).html',
             '4360113-九舍门诊口腔科-门诊病历(复诊)-RCT-门诊病历(复诊).html', '4060100-门诊神内-门诊病历(空白页)_神内-门诊病历(补充续打).html',
             '4360117-九舍门诊普内科-白细胞减少-初诊-门诊病历(初诊).html', '4090100-门诊中医内科-直肠恶性肿瘤气滞血瘀证(初诊)模板-门诊病历(初诊).html',
             '4090100-门诊中医内科-心系疾病-阴虚火旺证(复诊)模板-门诊病历(复诊).html', '4050100-门诊血液-门诊随访-门诊病历(复诊).html',
             '4360127-九舍门诊眼科-门诊病历(配药)-眼科-门诊病历(配药).html', '4270000-门诊针灸科-门诊病历(初诊)-腰痛-门诊病历(初诊).html',
             '4360119-九舍门诊伤科-门诊病历(初诊)-伤科-门诊病历(初诊).html', '4090100-门诊中医内科-心系疾病-阳气亏虚证(初诊)模板-门诊病历(初诊).html',
             '4290100-门诊康复科-门诊病历(初诊)-肩袖损伤-门诊病历(初诊).html', '4121800-门诊肿瘤-门诊病历(初诊)-晚期肿瘤-门诊病历(初诊).html',
             '4090100-门诊中医内科-直肠恶性肿瘤脾肾阳虚证(复诊)模板-门诊病历(复诊).html', '4121601-门诊乳腺中心-小叶增生-门诊病历(初诊).html',
             '4360117-九舍门诊普内科-上腹痛-高干复诊-门诊病历(复诊).html', '4180100-门诊伤科-门诊病历(配药)模板-门诊病历(配药).html',
             '4121601-门诊乳腺中心-门诊病历(复诊)-乳腺癌术后-门诊病历(复诊).html', '4260100-门诊皮肤科-疱病专病(初诊)模板-门诊病历(初诊).html',
             '4360129-九舍门诊中医内-门诊病历(配药)-原方-门诊病历(配药).html', '4360117-九舍门诊普内科-肺部阴影-初诊-门诊病历(初诊).html',
             '4280000-门诊推拿科-门诊病历(初诊)-中风后遗症-门诊病历(初诊).html', '4360109-九舍门诊骨科-门诊病历(初诊)-腰椎间盘突出症-门诊病历(初诊).html',
             '4270000-门诊针灸科-门诊病历(复诊)-周围性面瘫-门诊病历(复诊).html', '4360117-九舍门诊普内科-便秘-初诊-门诊病历(初诊).html',
             '4090100-门诊中医内科-心系疾病-肝郁气滞证(复诊)模板-门诊病历(复诊).html', '4360129-九舍门诊中医内-门诊病历(配药)-药方导入-门诊病历(配药).html',
             '4360117-九舍门诊普内科-咯血-初诊-门诊病历(初诊).html', '4360109-九舍门诊骨科-门诊病历(初诊)-肱骨外伤-门诊病历(初诊).html',
             '4200200-门诊妇科-门诊病历(初诊)-宫颈专病门诊病史-门诊病历(初诊).html', '4280000-门诊推拿科-门诊病历(初诊)-梨状肌综合征-门诊病历(初诊).html',
             '4200200-门诊妇科-门诊病历(复诊)-阴道镜报告-门诊病历(复诊).html', '4090100-门诊中医内科-脑病-气虚血瘀证(复诊)模板-门诊病历(复诊).html',
             '4290100-门诊康复科-门诊病历(初诊)-面神经麻痹-门诊病历(初诊).html', '4280000-门诊推拿科-门诊病历(初诊)-肩关节周围炎-门诊病历(初诊).html',
             '4240100-门诊口腔科-门诊病历(复诊)-简易病史（代配药）-门诊病历(复诊).html', '3060100-门诊超声-门诊病历(初诊)-门诊病历(初诊).html',
             '4050100-门诊血液-慢粒靶向药物(复诊)-门诊病历(复诊).html', '4250100-门诊耳鼻咽喉科-门诊病历(初诊)-声门型喉癌-门诊病历(初诊).html',
             '4360105-九舍门诊耳鼻喉科-门诊病历(初诊)-鼻咽部疾病-门诊病历(初诊).html', '4280000-门诊推拿科-门诊病历(初诊)-肱骨内上髁炎-门诊病历(初诊).html',
             '4260100-门诊皮肤科-免疫专病(初诊)模板-门诊病历(初诊).html', '4270000-门诊针灸科-门诊病历(初诊)-胃痛-门诊病历(初诊).html',
             '4121900-门诊胃肠外科-门诊病历(初诊)_胃癌-门诊病历(初诊).html', '4270000-门诊针灸科-门诊病历(初诊)-颈椎病-门诊病历(初诊).html',
             '4250100-门诊耳鼻咽喉科-门诊病历(初诊)-甲状舌管囊肿-门诊病历(初诊).html', '4240100-门诊口腔科-门诊病历(复诊)-简易病史（连续拔牙）-门诊病历(复诊).html',
             '4360117-九舍门诊普内科-肺部阴影-高干复诊-门诊病历(复诊).html', '4090100-门诊中医内科-心系疾病-寒凝心脉证(复诊)模板-门诊病历(复诊).html',
             '4270000-门诊针灸科-门诊病历(初诊)模板-门诊病历(初诊).html', '4100200-门诊儿内-门诊病历(初诊)-头痛-门诊病历(初诊).html',
             '4050100-门诊血液-血液科疾病急诊-门诊病历(复诊).html', '4180100-门诊伤科-膝痛-门诊病历(初诊)-门诊病历(初诊).html',
             '4360114-九舍门诊泌外-门诊病历(初诊)-前列腺癌-门诊病历(初诊).html', '4090100-门诊中医内科-直肠恶性肿瘤肝气乘脾证(初诊)模板-门诊病历(初诊).html',
             '4200100-门诊产科-门诊病历(配药)简单-产科-门诊病历(配药).html', '4240100-门诊口腔科-门诊病历(初诊)-肿块-门诊病历(初诊).html',
             '4270000-门诊针灸科-门诊病历(复诊)-中风后遗症-门诊病历(复诊).html', '4360117-九舍门诊普内科-白细胞减少-高干复诊-门诊病历(复诊).html',
             '4300500-门诊疼痛-门诊病历(初诊)-无痛胃肠镜麻醉-门诊病历(初诊).html', '4260100-门诊皮肤科-光敏性皮肤病(初诊)模板-门诊病历(初诊).html',
             '4090100-门诊中医内科-心系疾病-痰浊闭阻证(复诊)模板-门诊病历(复诊).html', '4090100-门诊中医内科-肺系疾病-痰热郁肺证(初诊)模板-门诊病历(初诊).html',
             '4250100-门诊耳鼻咽喉科-门诊病历(初诊)-声门上型喉癌-门诊病历(初诊).html', '4250100-门诊耳鼻咽喉科-门诊病历(初诊)-慢性中耳炎-门诊病历(初诊).html',
             '4360105-九舍门诊耳鼻喉科-门诊病历(初诊)-咽部-门诊病历(初诊).html', '4090100-门诊中医内科-胃恶性肿瘤血虚证(初诊)模板-门诊病历(初诊).html',
             '4100200-门诊儿内-门诊病历(初诊)-血尿-门诊病历(初诊).html', '4090100-门诊中医内科-肿瘤气血两虚证(复诊)模板-门诊病历(复诊).html',
             '4360117-九舍门诊普内科-高血压-初诊-门诊病历(初诊).html', '4090100-门诊中医内科-肺系疾病-风寒犯肺证(初诊)模板-门诊病历(初诊).html',
             '4050100-门诊血液-血小板减少(初诊)-门诊病历(初诊).html', '4090100-门诊中医内科-淋巴瘤寒痰凝滞证(初诊)模板-门诊病历(初诊).html',
             '4090100-门诊中医内科-肺系疾病-风热犯肺证(复诊)模板-门诊病历(复诊).html', '4360117-九舍门诊普内科-慢性阻塞性肺病急性加重-初诊-门诊病历(初诊).html',
             '4050100-门诊血液-贫血(复诊)-门诊病历(复诊).html', '4201500-门诊生殖中心-门诊病历(监测排卵)-门诊病历(复诊).html',
             '4350100-营养门诊-营养门诊病历(复诊)-门诊病历(复诊).html', '4090100-门诊中医内科-阳虚证(初诊)模板-门诊病历(初诊).html',
             '4250100-门诊耳鼻咽喉科-门诊病历(初诊)-耳廓假性囊肿-门诊病历(初诊).html', '4360109-九舍门诊骨科-门诊病历(初诊)-颈椎病-门诊病历(初诊).html',
             '4090100-门诊中医内科-胃恶性肿瘤气滞血瘀证(复诊)模板-门诊病历(复诊).html', '4240100-门诊口腔科-门诊病历(初诊)-松动牙、乳牙拔牙-门诊病历(初诊).html',
             '0080600-护理专病门诊-门诊病历(造口护理（首次随访复诊出现问题）)模板-门诊病历(复诊).html', '1010200-广慈门诊-门诊病历(复诊)-门诊病历(复诊).html',
             '4270000-门诊针灸科-门诊病历(复诊)-黄斑变性-门诊病历(复诊).html', '4050100-门诊血液-白细胞减少(初诊)-门诊病历(初诊).html',
             '4280000-门诊推拿科-门诊病历(初诊)-第三腰椎横突综合征-门诊病历(初诊).html', '4121601-门诊乳腺中心-乳房肿块-门诊病历(初诊).html',
             '4090100-门诊中医内科-淋巴瘤痰热内蕴证(初诊)模板-门诊病历(初诊).html', '4090100-门诊中医内科-胃恶性肿瘤热毒证(复诊)模板-门诊病历(复诊).html',
             '4090100-门诊中医内科-肺系疾病-肺气虚寒证(复诊)模板-门诊病历(复诊).html', '4100200-门诊儿内-门诊病历(初诊)-肾上腺-门诊病历(初诊).html',
             '4250100-门诊耳鼻咽喉科-门诊病历(初诊)-鼻腔肿物(恶性)-门诊病历(初诊).html', '4360109-九舍门诊骨科-门诊病历(初诊)-腕管综合征-门诊病历(初诊).html',
             '4090100-门诊中医内科-淋巴瘤脾虚痰湿证(复诊)模板-门诊病历(复诊).html', '4360106-九舍门诊妇科-门诊病历(初诊)-阴道出血-门诊病历(初诊).html',
             '4121601-门诊乳腺中心-门诊病历(配药)-拉帕替尼-门诊病历(配药).html', '4250100-门诊耳鼻咽喉科-门诊病历(初诊)-急性咽炎-门诊病历(初诊).html',
             '4260100-门诊皮肤科-银屑病-生物制剂使用(初诊)模板-门诊病历(初诊).html', '4090100-门诊中医内科-月经病——肾虚型(复诊)模板-门诊病历(复诊).html',
             '4160100-门诊烧伤整形-门诊病历(初诊)-灼伤-门诊病历(初诊).html', '4360127-九舍门诊眼科-门诊病历(初诊)-眼科(一般)-门诊病历(初诊).html',
             '4190100-骨科-骨关节炎-门诊病历(初诊).html', '4100200-门诊儿内-门诊病历(初诊)-惊厥-门诊病历(初诊).html',
             '4360117-九舍门诊普内科-下腹痛-初诊-门诊病历(初诊).html', '4280000-门诊推拿科-门诊病历(初诊)-膝关节炎-门诊病历(初诊).html',
             '4270000-门诊针灸科-门诊病历(复诊)-支气管炎-门诊病历(复诊).html', '4090100-门诊中医内科-脑病-气虚血瘀证(初诊)模板-门诊病历(初诊).html',
             '4360117-九舍门诊普内科-呕血-初诊-门诊病历(初诊).html', '4250100-门诊耳鼻咽喉科-门诊病历(初诊)-成人OSAHS-门诊病历(初诊).html',
             '4121601-门诊乳腺中心-门诊病历(初诊)-乳腺癌新辅助化疗-门诊病历(初诊).html', '4360109-九舍门诊骨科-门诊病历(初诊)-颈部肌肉劳损腰肌劳损-门诊病历(初诊).html',
             '4260100-门诊皮肤科-光敏性皮肤病(复诊)模板-门诊病历(复诊).html', '4090100-门诊中医内科-心系疾病-痰浊闭阻证(初诊)模板-门诊病历(初诊).html',
             '4100200-门诊儿内-门诊病历(初诊)-四肢麻木-门诊病历(初诊).html', '4090100-门诊中医内科-肺系疾病-痰热郁肺证(复诊)模板-门诊病历(复诊).html',
             '4090100-门诊中医内科-胃恶性肿瘤血虚证(复诊)模板-门诊病历(复诊).html', '4360114-九舍门诊泌外-门诊病历(初诊)-泌尿系感染-门诊病历(初诊).html',
             '4090100-门诊中医内科-肺系疾病-风寒犯肺证(复诊)模板-门诊病历(复诊).html', '4260100-门诊皮肤科-皮炎湿疹(初诊)模板-门诊病历(初诊).html',
             '4090100-门诊中医内科-肿瘤气血两虚证(初诊)模板-门诊病历(初诊).html', '4320100-门诊心理科-门诊病历(初诊)-精神障碍-门诊病历(初诊).html',
             '4090100-门诊中医内科-淋巴瘤寒痰凝滞证(复诊)模板-门诊病历(复诊).html', '4270000-门诊针灸科-门诊病历(初诊)-周围性面瘫-门诊病历(初诊).html',
             '4060100-门诊神内-门诊病历(配药)_神内-门诊病历(配药).html', '4121601-门诊乳腺中心-门诊病历(配药)-赫赛汀-门诊病历(配药).html',
             '4090100-门诊中医内科-心系疾病-寒凝心脉证(初诊)模板-门诊病历(初诊).html', '4290100-门诊康复科-门诊病历(初诊)-腰背-门诊病历(初诊).html',
             '4121601-门诊乳腺中心-门诊病历(初诊)-乳头溢液-门诊病历(初诊).html', '4090100-门诊中医内科-直肠恶性肿瘤肝气乘脾证(复诊)模板-门诊病历(复诊).html',
             '4121601-门诊乳腺中心-门诊病历(配药)-乳腺癌辅助内分泌治疗-门诊病历(配药).html', '4270000-门诊针灸科-门诊病历(复诊)-耳鸣-门诊病历(复诊).html',
             '4200200-门诊妇科-门诊病历(初诊)-阴道镜报告-门诊病历(初诊).html', '4360117-九舍门诊普内科-下腹痛-高干复诊-门诊病历(复诊).html',
             '4090100-门诊中医内科-胃恶性肿瘤气滞血瘀证(初诊)模板-门诊病历(初诊).html', '4360109-九舍门诊骨科-门诊病历(初诊)-肱骨内、外上髁炎-门诊病历(初诊).html',
             '4121601-门诊乳腺中心-门诊病历(配药)-氟维司群-门诊病历(配药).html', '4260100-门诊皮肤科-病历讨论(初诊)模板-门诊病历(初诊).html',
             '4250100-门诊耳鼻咽喉科-门诊病历(初诊)-神经性耳鸣-门诊病历(初诊).html', '4100200-门诊儿内-门诊病历(初诊)-性早熟（女童）-门诊病历(初诊).html',
             '4180100-门诊伤科-肩痛-门诊病历(初诊)-门诊病历(初诊).html', '4161101-门诊创面修复中心-门诊病历(初诊)-下肢动脉性溃疡-门诊病历(初诊).html',
             '4090100-门诊中医内科-肺系疾病-风热犯肺证(初诊)模板-门诊病历(初诊).html', '4250100-门诊耳鼻咽喉科-门诊病历(初诊)-鼻咽良性肿瘤-门诊病历(初诊).html',
             '4100200-门诊儿内-门诊病历(初诊)-发热-门诊病历(初诊).html', '4360109-九舍门诊骨科-门诊病历(初诊)-距骨软骨损伤-门诊病历(初诊).html',
             '4360117-九舍门诊普内科-头晕-高干复诊-门诊病历(复诊).html', '4090100-门诊中医内科-阳虚证(复诊)模板-门诊病历(复诊).html',
             '4360117-九舍门诊普内科-通用-配药-门诊病历(配药).html', '4120200-门诊普外-门诊病历(复诊)-胰腺-门诊病历(复诊).html',
             '4090100-门诊中医内科-淋巴瘤脾虚痰湿证(初诊)模板-门诊病历(初诊).html', '4121800-门诊肿瘤-门诊病历(初诊)-肿瘤根治术后-门诊病历(初诊).html',
             '4360127-九舍门诊眼科-门诊病历(初诊)-眼科-门诊病历(初诊).html', '4360117-九舍门诊普内科-血小板减少-初诊-门诊病历(初诊).html',
             '4100200-门诊儿内-门诊病历(初诊)-淋巴结肿大-门诊病历(初诊).html', '4250100-门诊耳鼻咽喉科-门诊病历(初诊)-急性鼻窦炎-门诊病历(初诊).html',
             '4160100-门诊烧伤整形-门诊病历(复诊)-灼伤后疤痕-门诊病历(复诊).html', '4090100-门诊中医内科-月经病——肾虚型(初诊)模板-门诊病历(初诊).html',
             '4090100-门诊中医内科-淋巴瘤痰热内蕴证(复诊)模板-门诊病历(复诊).html', '4090100-门诊中医内科-肺系疾病-肺气虚寒证(初诊)模板-门诊病历(初诊).html',
             '4090100-门诊中医内科-胃恶性肿瘤热毒证(初诊)模板-门诊病历(初诊).html', '4360113-九舍门诊口腔科-门诊病历(初诊)-冠周炎(智齿其他)-门诊病历(初诊).html',
             '4360114-九舍门诊泌外-门诊病历(初诊)-勃起功能障碍-门诊病历(初诊).html', '4240100-门诊口腔科-门诊病历(初诊)-TMD-门诊病历(初诊).html',
             '4260100-门诊皮肤科-脱发(初诊)模板-门诊病历(初诊).html', '4280000-门诊推拿科-门诊病历(初诊)-腰椎间盘突出-门诊病历(初诊).html',
             '4360117-九舍门诊普内科-便血-初诊-门诊病历(初诊).html', '4250100-门诊耳鼻咽喉科-门诊病历(初诊)-声带息肉-门诊病历(初诊).html',
             '4250100-门诊耳鼻咽喉科-门诊病历(初诊)-慢性扁桃体炎-门诊病历(初诊).html', '4360117-九舍门诊普内科-咯血-高干复诊-门诊病历(复诊).html',
             '4100200-门诊儿内-门诊病历(初诊)-头晕-门诊病历(初诊).html', '4280000-门诊推拿科-门诊病历(初诊)-寰枢关节扭伤-门诊病历(初诊).html',
             '4260100-门诊皮肤科-皮肤肿瘤(初诊)模板-门诊病历(初诊).html', '4090100-门诊中医内科-痰湿证(复诊)模板-门诊病历(复诊).html',
             '4250100-门诊耳鼻咽喉科-门诊病历(初诊)-扁桃体恶性肿瘤-门诊病历(初诊).html', '4100200-门诊儿内-门诊病历(初诊)-昏迷-门诊病历(初诊).html',
             '4250100-门诊耳鼻咽喉科-门诊病历(初诊)-声门下型喉癌-门诊病历(初诊).html', '4270000-门诊针灸科-门诊病历(复诊)-慢性前列腺增生-门诊病历(复诊).html',
             '4270000-门诊针灸科-门诊病历(复诊)-肩关节痛-门诊病历(复诊).html', '4240100-门诊口腔科-门诊病历(初诊)-洗牙-门诊病历(初诊).html',
             '4090100-门诊中医内科-结肠恶性肿瘤湿热下注证(复诊)模板-门诊病历(复诊).html', '4100200-门诊儿内-门诊病历(初诊)-矮小症-门诊病历(初诊).html',
             '4290100-门诊康复科-门诊病历(初诊)-颈椎-门诊病历(初诊).html', '4280000-门诊推拿科-门诊病历(初诊)-肱骨外上髁炎-门诊病历(初诊).html',
             '4090100-门诊中医内科-淋巴瘤肝肾阴虚证(初诊)模板-门诊病历(初诊).html', '4100200-门诊儿内-门诊病历(初诊)-溶血危象-门诊病历(初诊).html',
             '4250100-门诊耳鼻咽喉科-门诊病历(初诊)-慢性鼻炎-门诊病历(初诊).html', '1010200-广慈门诊-检查五官科(初诊)模板-门诊病历(初诊).html',
             '4190100-骨科-骨折及软组织损伤-门诊病历(初诊).html', '4090100-门诊中医内科-月经病——血热型(初诊)模板-门诊病历(初诊).html',
             '4090100-门诊中医内科-结肠恶性肿瘤气血两虚证(复诊)模板-门诊病历(复诊).html', '4201500-门诊生殖中心-门诊病历(详细配药)-门诊病历(配药).html',
             '4161101-门诊创面修复中心-门诊病历(初诊)-糖尿病-门诊病历(初诊).html', '4360113-九舍门诊口腔科-门诊病历(初诊)-TMD-门诊病历(初诊).html',
             '4360105-九舍门诊耳鼻喉科-门诊病历(初诊)-口咽部疾病-门诊病历(初诊).html', '4100200-门诊儿内-门诊病历(初诊)-咯血-门诊病历(初诊).html',
             '4090100-门诊中医内科-胃恶性肿瘤脾虚痰湿证(初诊)模板-门诊病历(初诊).html', '4121601-门诊乳腺中心-门诊病历(初诊)-乳腺癌辅助内分泌治疗-门诊病历(初诊).html',
             '4260100-门诊皮肤科-甲病(初诊)模板-门诊病历(初诊).html', '4140100-门诊泌外-泌外肾癌门诊病历(配药)-门诊病历(配药).html',
             '4360117-九舍门诊普内科-血小板减少-高干复诊-门诊病历(复诊).html', '1010209-广慈门诊皮肤科-门诊病历(初诊)-门诊病历(初诊).html',
             '4250100-门诊耳鼻咽喉科-门诊病历(初诊)-鼻息肉-门诊病历(初诊).html', '4360117-九舍门诊普内科-便秘-高干复诊-门诊病历(复诊).html',
             '4360127-九舍门诊眼科-门诊病历(复诊)-眼科(一般)-门诊病历(复诊).html', '4100200-门诊儿内-门诊病历(初诊)-性发育异常-门诊病历(初诊).html',
             '4090100-门诊中医内科-血虚证(初诊)模板-门诊病历(初诊).html', '4360114-九舍门诊泌外-门诊病历(初诊)-泌尿系结石-门诊病历(初诊).html',
             '4100200-门诊儿内-门诊病历(初诊)-糖尿病-门诊病历(初诊).html', '4100200-门诊儿内-儿科门诊(复诊)-门诊病历(复诊).html',
             '4090100-门诊中医内科-月经病——气滞血瘀型(复诊)模板-门诊病历(复诊).html', '4140100-门诊泌外-泌外肾癌门诊病历(初诊)-门诊病历(初诊).html',
             '4010100-门诊消化-消化内科(初诊)-门诊病历(初诊).html', '4090100-门诊中医内科-心系疾病-阴虚火旺证(初诊)模板-门诊病历(初诊).html',
             '4240100-门诊口腔科-门诊病历(初诊)-龋齿牙体缺损-门诊病历(初诊).html', '4050100-门诊血液-血象异常(初诊)-门诊病历(初诊).html',
             '4270000-门诊针灸科-门诊病历(初诊)-甲状腺炎-门诊病历(初诊).html', '4090100-门诊中医内科-心系疾病-阳气亏虚证(复诊)模板-门诊病历(复诊).html',
             '4121601-门诊乳腺中心-浸润性癌门诊病历(配药)-门诊病历(配药).html', '4270000-门诊针灸科-门诊病历(初诊)-通用-门诊病历(初诊).html',
             '4121800-门诊肿瘤-门诊病历(复诊)-肿瘤根治术后-门诊病历(复诊).html', '4090100-门诊中医内科-直肠恶性肿瘤气滞血瘀证(复诊)模板-门诊病历(复诊).html',
             '4240100-门诊口腔科-门诊病历(复诊)-干髓治疗（复诊换药充填）-门诊病历(复诊).html', '4100200-门诊儿内-门诊病历(初诊)-呼吸困难-门诊病历(初诊).html',
             '4100200-门诊儿内-门诊病历(初诊)-川崎病-门诊病历(初诊).html', '4121601-门诊乳腺中心-浸润性癌门诊病历(初诊)-门诊病历(初诊).html',
             '4240100-门诊口腔科-门诊病历(初诊)-外伤-门诊病历(初诊).html', '4240100-门诊口腔科-门诊病历(初诊)-残根、残冠、死髓牙、折裂牙拔牙-门诊病历(初诊).html',
             '4090100-门诊中医内科-心系疾病-肝郁气滞证(初诊)模板-门诊病历(初诊).html', '4100200-门诊儿内-门诊病历(初诊)-发绀-门诊病历(初诊).html',
             '4100200-门诊儿内-门诊病历(初诊)-肾上腺危象-门诊病历(初诊).html', '4070100-门诊呼吸科-呼吸科门诊(初诊)-门诊病历(初诊).html',
             '4240100-门诊口腔科-门诊病历(复诊)-简易病史（义齿修理）-门诊病历(复诊).html', '4270000-门诊针灸科-门诊病历(初诊)-中风后遗症-门诊病历(初诊).html',
             '4100200-门诊儿内-门诊病历(初诊)-腹泻-门诊病历(初诊).html', '4090100-门诊中医内科-直肠恶性肿瘤脾肾阳虚证(初诊)模板-门诊病历(初诊).html',
             '4270000-门诊针灸科-门诊病历(复诊)-膝关节痛-门诊病历(复诊).html', '4360109-九舍门诊骨科-门诊病历(初诊)-拇外翻-门诊病历(初诊).html',
             '4360117-九舍门诊普内科-2型糖尿病-初诊-门诊病历(初诊).html', '4250100-门诊耳鼻咽喉科-门诊病历(初诊)-鼻腔肿物(良性)-门诊病历(初诊).html',
             '4360109-九舍门诊骨科-门诊病历(初诊)-类风湿性关节炎多关节病骨关节炎-门诊病历(初诊).html', '4121601-门诊乳腺中心-门诊病历(初诊)-乳房肿块-门诊病历(初诊).html']


def temp():
    department = '神经根型颈椎病'
    template = ''
    for html in all_htmls:
        if department in html and template in html:
            print(html)


def get_top100_templates():
    """
    获取使用量在100以上的模板，并获取配套的初复诊
    :return:
    """
    top100_htmls = [
        '4431000-急诊发热-门诊病历(初诊)模板-门诊病历(初诊).html',
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
    result = {}
    add_result = {}
    for raw_top100_html in top100_htmls:
        # top100_html = '0080600-护理专病门诊-PICC护理（拔管护理）模板-门诊病历(配药).html'
        top100_html = raw_top100_html.replace('（', '(').replace('）', ')').replace('-复诊-', '(复诊)').replace('-初诊-', '(初诊)').replace('-配药-', '(配药)')
        patt = re.sub('\([\u4e00-\u9fa5]+\)', r'(\([\u4e00-\u9fa5]+\))', top100_html)
        for html in all_htmls:
            if re.search(patt,
                         html.replace('（', '(').replace('）', ')').replace('-复诊-', '(复诊)').replace('-初诊-', '(初诊)').replace('-配药-', '(配药)')
                         ):
                result.setdefault(raw_top100_html, set())
                result[raw_top100_html].add(html)

    for k, v in result.items():
        temp = []
        sign = False
        for i in v:
            if i != k and i not in top100_htmls:
                sign=True
                print('    {}'.format(i))
                temp.append(i)
        if sign:
            add_result[k] = temp
            print(k)
            print()

    print(add_result)

def add_excel():
    add_result = {'4360127-九舍门诊眼科-门诊病历(复诊)-眼科(一般)-门诊病历(复诊).html': ['4360127-九舍门诊眼科-门诊病历(初诊)-眼科(详细)-门诊病历(初诊).html', '4360127-九舍门诊眼科-门诊病历(初诊)-眼科(一般)-门诊病历(初诊).html'], '4360127-九舍门诊眼科-门诊病历(配药)-眼科-门诊病历(配药).html': ['4360127-九舍门诊眼科-门诊病历(复诊)-眼科-门诊病历(复诊).html', '4360127-九舍门诊眼科-门诊病历(初诊)-眼科-门诊病历(初诊).html'], '4360117-九舍门诊普内科-通用-配药-门诊病历(配药).html': ['4360117-九舍门诊普内科-通用-初诊-门诊病历(初诊).html'], '4121601-门诊乳腺中心-门诊病历(配药)-乳腺癌辅助内分泌治疗-门诊病历(配药).html': ['4121601-门诊乳腺中心-门诊病历(初诊)-乳腺癌辅助内分泌治疗-门诊病历(初诊).html'], '4360117-九舍门诊普内科-通用-复诊-门诊病历(复诊).html': ['4360117-九舍门诊普内科-通用-初诊-门诊病历(初诊).html'], '4350100-营养门诊-营养门诊病历(配药)-门诊病历(配药).html': ['4350100-营养门诊-营养门诊病历(复诊)-门诊病历(复诊).html', '4350100-营养门诊-营养门诊病历(初诊)-门诊病历(初诊).html'], '4121601-门诊乳腺中心-门诊病历(配药)-乳腺癌辅助化疗-门诊病历(配药).html': ['4121601-门诊乳腺中心-门诊病历(初诊)-乳腺癌辅助化疗-门诊病历(初诊).html'], '4121601-门诊乳腺中心-门诊病历(配药)-赫赛汀-门诊病历(配药).html': ['4121601-门诊乳腺中心-门诊病历(初诊)-赫赛汀-门诊病历(初诊).html'], '4270000-门诊针灸科-门诊病历(复诊)-腰痛-门诊病历(复诊).html': ['4270000-门诊针灸科-门诊病历(初诊)-腰痛-门诊病历(初诊).html'], '4270000-门诊针灸科-门诊病历(复诊)-颈椎病-门诊病历(复诊).html': ['4270000-门诊针灸科-门诊病历(初诊)-颈椎病-门诊病历(初诊).html'], '4121601-门诊乳腺中心-门诊病历(配药)-乳腺癌新辅助化疗-门诊病历(配药).html': ['4121601-门诊乳腺中心-门诊病历(初诊)-乳腺癌新辅助化疗-门诊病历(初诊).html'], '4270000-门诊针灸科-门诊病历(复诊)-肩关节痛-门诊病历(复诊).html': ['4270000-门诊针灸科-门诊病历(初诊)-肩关节痛-门诊病历(初诊).html'], '4270000-门诊针灸科-门诊病历(复诊)-周围性面瘫-门诊病历(复诊).html': ['4270000-门诊针灸科-门诊病历(初诊)-周围性面瘫-门诊病历(初诊).html'], '4270000-门诊针灸科-门诊病历(复诊)-膝关节痛-门诊病历(复诊).html': ['4270000-门诊针灸科-门诊病历(初诊)-膝关节痛-门诊病历(初诊).html']}
    df = read_excel('/Users/jeremy.li/Basebit/Projects/AutoTemplate/近1年门诊常用科室模板与disease.xlsx', 'Sheet1')
    print(df.loc[df[9] >= 100][2].values)
    for exists, adds in add_result.items():
        department_code, department, num, icd, disease_name, remark = df.loc[df[2] == exists][[3,4,5,6,7,8]].values[0]
        for add in adds:
            if not df.loc[df[2] == add].empty:
                print('已经存在：', add, department_code, department, num, icd, disease_name, remark)
            else:
                print(add, department_code, department, 100, icd, disease_name, remark)

if __name__ == '__main__':
    # temp()
    # get_top100_templates()
    add_excel()
