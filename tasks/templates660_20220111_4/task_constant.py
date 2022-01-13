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
PRESENT_FILE_PATH = None
TEMPLATE_DISEASE_FILE_PATH = '{}/template_disease_map.xlsx'.format(TASK_PATH)
EXCEL_STANDARD_FILE_PATH = '{}/standard_templates.xlsx'.format(TASK_PATH)

EXTRACT_TEMPLATE_FILES = [
    '门诊病历(初诊)-氟维司群(4121601)门诊病历(初诊)24e84d02-e7d4-40bf-89c5-d30d45652b30.html',
    '高血压（初诊）(1080100)高血压(初诊)22e77c9c-38d2-4cf4-89ea-0d1b7babd524.html',
    '高血压门诊病史(初诊)(1080100)高血压门诊病史(初诊)90568bc6-b0e8-42d0-9851-7b31ce9784c9.html',
    '门诊病历(初诊)-赫赛汀(4121601)门诊病历(初诊)3459fc16-d7dc-4832-b8cd-23c61296a8d4.html',
    '浸润性癌门诊病历(初诊)(4121601)门诊病历(初诊)ec0efb45-2f59-4621-9bdc-c22cf6f33086.html',
    '门诊病历(复诊)-乳腺增生(4121601)门诊病历(复诊)4a7e076b-6371-4ff9-be31-c479f931506c.html',
    '门诊病历(复诊)-乳腺钙化灶(4121601)门诊病历(复诊)f26e8cda-ccdb-42e6-8e24-de7469bfc8cf.html',
    '门诊病历(配药)-乳腺癌新辅助内分泌治疗(4121601)门诊病历(配药)a38d2fb8-f634-4733-a00c-019d2076338a.html',
    '门诊病历(配药)-乳腺癌新辅助化疗(4121601)门诊病历(配药)90a6fd36-fdc1-4f0b-aa31-2009dd344eb7.html',
    '门诊病历(复诊)-乳腺癌术后(4121601)门诊病历(复诊)e96779e5-0f03-4b68-9d96-b475ec71b175.html',
    '门诊病历(配药)-乳腺癌辅助内分泌治疗(4121601)门诊病历(配药)89740baf-2ad9-4dd7-bfdc-b24841b0ec6c.html',
    '门诊病历(配药)-乳腺癌辅助化疗(4121601)门诊病历(配药)9e870823-ea0c-4d27-8002-22474f2e5d74.html',
    '门诊病历(配药)-乳腺癌靶向+化疗(4121601)门诊病历(配药)f9977cef-bfd1-42d1-bf89-abcca0e7c0a0.html',
    '门诊病历(复诊)-乳头溢液(4121601)门诊病历(复诊)41a02469-967e-43bb-9146-9f15dc7fa95f.html',
    '门诊病历(复诊)-乳房肿块(4121601)门诊病历(复诊)b8101e76-2af5-481d-9cf4-76993474e390.html',
    '门诊病历(初诊)-拉帕替尼(4121601)门诊病历(初诊)f817b28d-1271-4852-93b6-09e80ca2c1d5.html',
    '门诊病历(配药)-拉帕替尼(4121601)门诊病历(配药)9a7f772c-0027-412a-8344-42011031c206.html',
    '门诊病历(初诊)-乳头溢液(4121601)门诊病历(初诊)65834e13-8170-4d1f-a89e-91e96d1963d7.html',
    '门诊病历(初诊)-乳腺癌靶向+化疗(4121601)门诊病历(初诊)d1431521-b987-4516-98c5-8d08e1655908.html',
    '门诊病历(初诊)-乳腺癌辅助化疗(4121601)门诊病历(初诊)eb84192f-719e-4a7e-8647-ca5e62898a61.html',
    '门诊病历(初诊)-乳腺癌辅助内分泌治疗(4121601)门诊病历(初诊)97e5246e-55cf-4043-b755-a0c9e1d6ca99.html',
    '门诊病历(初诊)-乳腺癌新辅助化疗(4121601)门诊病历(初诊)ba605571-bbaf-4536-bbb1-8b6e29b2596a.html',
    '门诊病历(初诊)-乳腺癌新辅助内分泌治疗(4121601)门诊病历(初诊)b170fe4c-1cba-41a0-9e1a-ab293e53fe2c.html',
    '门诊病历(初诊)-乳腺钙化灶(4121601)门诊病历(初诊)481234f3-9349-4c38-b8f1-f953578b9102.html',
    '门诊病历(初诊)-乳腺增生(4121601)门诊病历(初诊)3e4770c7-5bae-44fe-8f3a-2b0f7d0e552a.html',
    '浸润性癌门诊病历(配药)(4121601)门诊病历(配药)7e46b4cc-ed25-43c7-b1fe-0b78594e5d13.html',
    '门诊病历(配药)-赫赛汀(4121601)门诊病历(配药)58a61c94-8288-4db1-aa5c-5b645b7d027b.html',
    '高血压（复诊）(1080100)高血压（复诊）ff498815-2b15-4f20-886b-44a4cf0b5032.html',
    '门诊病历(配药)-氟维司群(4121601)门诊病历(配药)d04fcefc-081f-428d-838e-2e4583d3c10c.html', ]
