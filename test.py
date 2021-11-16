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


if __name__ == '__main__':
    raw_json = {"samples":[{"age":30,"content":"\u5de6/\u53f3\u4e0b\u80a2\u8db3\u9774\u533a/\u8e1d\u5468\u53ef\u89c1\u6bdb\u7ec6\u8840\u7ba1\u6269\u5f20,\u9759\u8109\u66f2\u5c48\u53ca\u56ca\u72b6\u9686\u8d77,\u4f34\u76ae\u708e\u3001\u6e7f\u75b9,\u7619\u75d2,\u8272\u7d20\u6c89\u7740\u660e\u663e\u3002","date":"2019-09-30 15:06:03","entity_list":[{"code":"I78.803","misc":{"deco":[[2,2,"symptom_pos","\u53f3"],[3,4,"symptom_obj","\u4e0b\u80a2"],[8,10,"symptom_pos","/\u8e1d\u5468"]],"tags":[[2,2,"symptom_pos","\u53f3"],[3,4,"symptom_obj","\u4e0b\u80a2"],[8,10,"symptom_pos","/\u8e1d\u5468"],[13,18,"disease","\u6bdb\u7ec6\u8840\u7ba1\u6269\u5f20"]],"timex3":[{}]},"normalization":1,"source":"default","text":"\u6bdb\u7ec6\u8840\u7ba1\u6269\u5f20\u75c7","time":"2019-09-30","type":"disease","value":1},{"misc":{"deco":[[37,38,"symptom_deco","\u7619\u75d2"],[44,45,"symptom_deco","\u660e\u663e"]],"tags":[[31,32,"symptom","\u76ae\u708e"],[37,38,"symptom_deco","\u7619\u75d2"],[44,45,"symptom_deco","\u660e\u663e"]],"timex3":[{}]},"normalization":0,"source":"default","text":"\u76ae\u708e","time":"2019-09-30","type":"symptom","value":1},{"code":"R21.x00","misc":{"deco":[[37,38,"symptom_deco","\u7619\u75d2"],[44,45,"symptom_deco","\u660e\u663e"]],"tags":[[34,35,"symptom","\u6e7f\u75b9"],[37,38,"symptom_deco","\u7619\u75d2"],[44,45,"symptom_deco","\u660e\u663e"]],"timex3":[{}]},"normalization":1,"source":"default","text":"\u76ae\u75b9\u548c\u5176\u4ed6\u975e\u7279\u5f02\u6027\u6591\u75b9","time":"2019-09-30","type":"symptom","value":1},{"addition":{"type23801":[{"code":"A18","source":"\u8272\u7d20\u6c89\u7740","text":"\u8272\u7d20\u6c89\u7740"}]},"code":"R23.801","misc":{"deco":[[37,38,"symptom_deco","\u7619\u75d2"],[44,45,"symptom_deco","\u660e\u663e"]],"tags":[[37,38,"symptom_deco","\u7619\u75d2"],[40,43,"symptom_desc","\u8272\u7d20\u6c89\u7740"],[44,45,"symptom_deco","\u660e\u663e"]],"timex3":[{}]},"normalization":1,"source":"default","text":"\u76ae\u80a4\u6539\u53d8","time":"2019-09-30","type":"symptom","value":1}],"gender":"M","id":"00000001"}]}

    get_entities(raw_json)
