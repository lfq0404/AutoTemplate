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
PRESENT_FILE_PATH = '{}/现病史第二批.xlsx'.format(TASK_PATH)
TEMPLATE_DISEASE_FILE_PATH = '{}/template_disease_map.xlsx'.format(TASK_PATH)
EXCEL_STANDARD_FILE_PATH = '{}/standard_templates.xlsx'.format(TASK_PATH)

EXTRACT_TEMPLATE_FILES = [
    '门诊病历(初诊)-矮小症(4100200)门诊病历(初诊)32f2bead-82f8-4b3d-9d2d-1dc925374152.html',
    '门诊病历(初诊)-川崎病(4100200)门诊病历(初诊)673cfa66-16d7-4409-901b-fc5f9d743d8b.html',
    '儿科门诊(初诊)(4100200)门诊病历(初诊)703ccfdf-4e4e-4e89-b9d6-38f4893495b8.html',
    '门诊病历(初诊)-发绀(4100200)门诊病历(初诊)502cd87b-ea33-4f8d-b719-fd8f5cc0e454.html',
    '门诊病历(初诊)-发热(4100200)门诊病历(初诊)91b5fe76-b9a4-4921-a8a2-0ba9d5c4e171.html',
    '门诊病历(初诊)-肥胖(4100200)门诊病历(初诊)0a7cc1d9-0233-45d2-a839-6794aef0bac0.html',
    '门诊病历(初诊)-腹泻(4100200)门诊病历(初诊)9c82fe0f-991c-4fd2-90fb-59f3bc0047ab.html',
    '门诊病历(初诊)-呼吸困难(4100200)门诊病历(初诊)f3a76ffe-91cb-41c9-ab94-ad2686d000a3.html',
    '门诊病历(初诊)-昏迷(4100200)门诊病历(初诊)013ce9dc-bade-4fc8-bc83-645b61b6774b.html',
    '门诊病历(初诊)-甲亢(4100200)门诊病历(初诊)6b428835-09df-4d21-ad2c-63f014b8ec9b.html',
    '门诊病历(初诊)-甲亢危象(4100200)门诊病历(初诊)0d23328a-3335-486c-8d1d-d7884a2e8309.html',
    '门诊病历(初诊)-甲状腺炎(4100200)门诊病历(初诊)c5fc7a9d-03b6-4e4d-8926-3fee657c405f.html',
    '门诊病历(初诊)-惊厥(4100200)门诊病历(初诊)ebd1797f-34e4-4015-976a-90ea77c75a82.html',
    '门诊病历(初诊)-剧烈啼哭(4100200)门诊病历(初诊)b8e53328-cf28-4b02-a467-043592ec109e.html',
    '门诊病历(初诊)-咳嗽(4100200)门诊病历(初诊)c6086902-699b-4a01-a880-78bfd1777e10.html',
    '门诊病历(初诊)-淋巴结肿大(4100200)门诊病历(初诊)8cf66c96-e6d0-40cb-95fb-0d7a7be72875.html',
    '门诊病历(初诊)-尿路感染(4100200)门诊病历(初诊)45d9927b-a354-4fb4-b703-9a6f1afdc0b7.html',
    '门诊病历(复诊)-复诊(4100200)门诊病历(复诊)ea348fbf-64a0-4301-a3c2-b5e156420602.html',
    '门诊病历(初诊)-溶血危象(4100200)门诊病历(初诊)a4611126-9d5a-4a1d-a127-d9b09d608a30.html',
    '门诊病历(初诊)-肾上腺(4100200)门诊病历(初诊)c156f07d-0c61-4283-a986-24bda69d096a.html',
    '门诊病历(初诊)-肾上腺危象(4100200)门诊病历(初诊)a03575bd-5100-4753-afb0-d2eb82c7adc6.html',
    '门诊病历(初诊)-四肢麻木(4100200)门诊病历(初诊)f34f2a54-37d1-40eb-af49-4bf5e1f07052.html',
    '门诊病历(初诊)-糖尿病(4100200)门诊病历(初诊)0b06a3ed-db63-4131-a0ce-9fcd2f4f95eb.html',
    '门诊病历(初诊)-糖尿病酮症(4100200)门诊病历(初诊)e10b8ab4-6099-4159-948f-1c112ad80682.html',
    '门诊病历(初诊)-头痛(4100200)门诊病历(初诊)1b9eb8f0-17db-45f2-b0ad-10a813cdfaf8.html',
    '门诊病历(初诊)-性发育异常(4100200)门诊病历(初诊)4c7f6977-5cfb-4925-9ce2-3d5bc4fdbb37.html',
    '门诊病历(初诊)-胸闷(4100200)门诊病历(初诊)2dc03c6b-51b1-4526-aa4a-03a04160c313.html',
    '门诊病历(初诊)-胸痛(4100200)门诊病历(初诊)57d12cd2-e937-4076-95ad-ff24b40f491b.html',
    '门诊病历(初诊)-血尿(4100200)门诊病历(初诊)cf17be78-6b93-436b-934d-8551f1e6b51d.html',
    '儿科门诊(复诊)(4100200)门诊病历(复诊)142595dc-35b1-4567-98c1-c2670ceed1e5.html',
    '门诊病历(复诊)-矮小症(4100200)门诊病历(复诊)a51d64b0-b07e-4c0a-8757-f3ad3aebce93.html', ]
