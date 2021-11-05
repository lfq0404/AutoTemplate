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


import regex

texts = [
    ['有无高血压、糖尿病史', '有无高血压、糖尿病史等'],
    ['有无高血压、糖尿病史等', '有无高血压、糖尿病史等'],
    ['有无高血压、糖尿病', '有无高血压、糖尿病等'],
    ['有无高血压、糖尿病等', '有无高血压、糖尿病等'],
    ['有高血压、心脏病、糖尿病史、脑梗塞史，常规服药，控制良好。', '有高血压、心脏病、糖尿病史、脑梗塞史等，常规服药，控制良好。'],
    ['有高血压、心脏病、糖尿病史、脑梗塞史等，常规服药，控制良好。', '有高血压、心脏病、糖尿病史、脑梗塞史等，常规服药，控制良好。'],
    ['有高血压、心脏病、糖尿病史、脑梗塞，常规服药，控制良好。', '有高血压、心脏病、糖尿病史、脑梗塞等，常规服药，控制良好。'],
    ['有高血压、心脏病、糖尿病史、脑梗塞等，常规服药，控制良好。', '有高血压、心脏病、糖尿病史、脑梗塞等，常规服药，控制良好。'],
    ['有高血压、糖尿病史、脑梗塞史、心脏病，常规服药，控制良好。', '有高血压、糖尿病史、脑梗塞史、心脏病等，常规服药，控制良好。'],
    # ['有高血压，糖尿病史，脑梗塞史，心脏病，常规服药，控制良好。', '有高血压，糖尿病史，脑梗塞史，心脏病等，常规服药，控制良好。'],
    ['有高血压、糖尿病史、脑梗塞史、心脏病等，常规服药，控制良好。', '有高血压、糖尿病史、脑梗塞史、心脏病等，常规服药，控制良好。'],
    # ['有高血压，糖尿病史，脑梗塞史，心脏病等，常规服药，控制良好。', '有高血压，糖尿病史，脑梗塞史，心脏病等，常规服药，控制良好。'],
    ['有高血压。', '有高血压。'],
    ['有高血压，常规服药，控制良好。', '有高血压，常规服药，控制良好。'],
]
for text, right in texts:
    raw_text = text
    for pat in [
        '(?<=、)(高血压|脑梗塞|糖尿病|哮喘病|心脏病)(?![史、等])',
        '(?<=、)(高血压史|脑梗塞史|糖尿病史|哮喘病史|心脏病史)(?![、等])',
    ]:
        text = regex.sub(pat, r'\1等', text)
    assert text == right, '{} --> {}'.format(raw_text, text)
