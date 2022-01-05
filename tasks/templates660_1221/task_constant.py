#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/21 17:30
# @File    : constant.py
# @Software: Basebit
# @Description:

from constant import *

# 原始模板地址
TEMPLATE_PATH = '/Users/jeremy.li/Basebit/Documents/develop/smart/20211013-瑞金门急诊模板配置/20211220-门诊660'
TASK_PATH = os.path.abspath(os.path.dirname(__file__))

# 输出的Excel
EXCEL_RESULT_FOR_CHECK_PATH = '{}/result_for_check_templates.xlsx'.format(TASK_PATH)
PRESENT_FILE_PATH = '{}/现病史第一批.xlsx'.format(TASK_PATH)
TEMPLATE_DISEASE_FILE_PATH = '{}/template_disease_map.xlsx'.format(TASK_PATH)
EXCEL_STANDARD_FILE_PATH = '{}/standard_templates.xlsx'.format(TASK_PATH)

TEMPLATE_BATCHES = {
    1: ['门诊病历(初诊)-外耳道炎(4250100)门诊病历(初诊)2ce86d8b-47ba-47f3-9764-621f32332e3d.html',
        '门诊病历(初诊)-急性扁桃体炎(4250100)门诊病历(初诊)be0a9d9e-76d8-43fb-9864-df9b1ef300bd.html',
        '门诊病历(初诊)-咯血(4100200)门诊病历(初诊)8b933a9b-f0ed-459f-8974-ce2e07d44568.html',
        '门诊病历(初诊)-头晕(4100200)门诊病历(初诊)d51ddaf7-fa7d-454b-bdf2-d7ea8537eb2c.html',
        '门诊病历(初诊)-呕血(4100200)门诊病历(初诊)33edc51f-9a2d-4826-bfab-d87658601b59.html',
        '门诊病历(初诊)-腹痛(4100200)门诊病历(初诊)e8b9e6fd-3645-4956-af23-ef9273ff6641.html',
        '门诊病历(初诊)-性早熟（男童）(4100200)门诊病历(初诊)a00123c0-b012-4b13-905a-bdaaa56d05fe.html',
        '门诊病历(初诊)-性早熟（女童）(4100200)门诊病历(初诊)14647c84-46a0-4d4e-9516-d2529a567743.html',
        '门诊病历(初诊)-血友病(4100200)门诊病历(初诊)63cf300b-fd4c-4f7f-bdf4-8d564a4cdd68.html',
        '门诊病历(初诊)-椎动脉型颈椎病(4280000)门诊病历(初诊)57cabcfd-e091-4721-bafd-5b62e2c49e34.html',
        '门诊病历(初诊)-腹痛(4360106)门诊病历(初诊)ac497743-980a-447f-ad04-5a3be8bf288b.html',
        '上腹痛-初诊(4360117)上腹痛-初诊4a8594fd-b473-47da-89db-3b7a2e942877.html',
        '下腹痛-初诊(4360117)下腹痛-初诊baa6a105-a261-49d7-a114-e6b557434051.html',
        '头晕-初诊(4360117)头晕-初诊226014e5-341b-4416-b529-15fbe2dc9aee.html',
        '血小板减少(初诊)(4050100)门诊病历(初诊)f15f5b78-2855-46c8-a04b-c804b1a73739.html',
        '门诊病历(初诊)-肩关节痛(4270000)门诊病历(初诊)57af8ad2-dcb7-4f0f-ad10-0c7ca9fb3526.html',
        '门诊病历(初诊)-支气管炎(4270000)门诊病历(初诊)ccb3153b-d81c-4d36-83fb-ce0b6d274554.html',
        '门诊病历(初诊)-肱骨内上髁炎(4280000)门诊病历(初诊)24497434-91c7-4a31-9c92-e6c19301c014.html',
        '门诊病历(初诊)-肱骨外上髁炎(4280000)门诊病历(初诊)91a01a3a-0488-4657-8500-255df5353cc5.html',
        '门诊病历(初诊)-肱骨内、外上髁炎(4360109)门诊病历(初诊)0cf492da-aab5-425a-9f93-e6341fbcdc8a.html',
        '门诊病历(初诊)-肱骨内、外上髁炎(4360109)门诊病历(初诊)0cf492da-aab5-425a-9f93-e6341fbcdc8a.html',
        '门诊病历(初诊)-痛风性关节炎(4360109)门诊病历(初诊)00910d10-3b78-4f86-a569-4fc54e2ce3e5.html',
        '皮炎湿疹(初诊)模板(4260100)皮炎湿疹(初诊)f9ee85c1-f29d-4b3c-9f9c-e6fc11be6218.html',
        '皮炎湿疹(初诊)模板(4260100)皮炎湿疹(初诊)f9ee85c1-f29d-4b3c-9f9c-e6fc11be6218.html',
        '湿疹(初诊)模板(4090200)门诊病历(初诊)0111ef2f-d69c-4d84-ae91-9b3e5a3f9443.html',
        '呕血-初诊(4360117)呕血-初诊6ef37e8a-6493-4943-9637-b05e842c1685.html',
        '血小板减少-初诊(4360117)血小板减少-初诊79dfe5ef-1fab-4ed2-b80d-41688eb296ea.html',
        '门诊病历(初诊)-乳房肿块(4121601)门诊病历(初诊)b5073a25-30ba-44b6-8c0f-b5a81ab810c8.html',
        '门诊病历(初诊)-抑郁焦虑状态(4320100)门诊病历(初诊)c55c69e2-84ea-4cb8-adca-7caadd17e81c.html',
        '门诊病历(初诊)-抑郁焦虑状态(4320100)门诊病历(初诊)c55c69e2-84ea-4cb8-adca-7caadd17e81c.html', ]
}
