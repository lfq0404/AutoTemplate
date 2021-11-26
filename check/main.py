#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/26 10:20
# @File    : main.py
# @Software: Basebit
# @Description:
import re

all_files = [
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
    '4270000-门诊针灸科-门诊病历(初诊)-颈椎病-门诊病历(初诊).html',
    '4270000-门诊针灸科-门诊病历(初诊)-周围性面瘫-门诊病历(初诊).html',
    '4270000-门诊针灸科-门诊病历(初诊)-腰痛-门诊病历(初诊).html',
    '4270000-门诊针灸科-门诊病历(初诊)-肩关节痛-门诊病历(初诊).html',
    '4350100-营养门诊-营养门诊病历(初诊)-门诊病历(初诊).html',
    '4360127-九舍门诊眼科-门诊病历(初诊)-眼科(详细)-门诊病历(初诊).html',
    '4360127-九舍门诊眼科-门诊病历(初诊)-眼科(一般)-门诊病历(初诊).html',
    '4360127-九舍门诊眼科-门诊病历(复诊)-眼科-门诊病历(复诊).html',
    '4360127-九舍门诊眼科-门诊病历(初诊)-眼科-门诊病历(初诊).html',
    '4360117-九舍门诊普内科-通用-初诊-门诊病历(初诊).html',
    '4121601-门诊乳腺中心-门诊病历(初诊)-乳腺癌辅助内分泌治疗-门诊病历(初诊).html',
    '4360117-九舍门诊普内科-通用-初诊-门诊病历(初诊).html',
    '4350100-营养门诊-营养门诊病历(复诊)-门诊病历(复诊).html',
    '4121601-门诊乳腺中心-门诊病历(初诊)-乳腺癌辅助化疗-门诊病历(初诊).html',
    '4121601-门诊乳腺中心-门诊病历(初诊)-赫赛汀-门诊病历(初诊).html',
    '4121601-门诊乳腺中心-门诊病历(初诊)-乳腺癌新辅助化疗-门诊病历(初诊).html',
    '4270000-门诊针灸科-门诊病历(初诊)-膝关节痛-门诊病历(初诊).html',
]

for file in all_files:
    print(file)
    department_code = int(re.findall('(\d+)-', file)[0])
    if '初诊' in file:
        _type = 'INITIAL'
    elif '复诊' in file:
        _type = 'SUBSEQUENT'
    else:
        _type = 'MEDICINE'

    with open('aiwizard.html', 'r') as f:
        html = f.read()
    html = re.sub('deptCode: "(\d+)"', 'deptCode: "{}"'.format(department_code), html)
    html = re.sub('tplType: "(.+)"', 'tplType: "{}"'.format(_type), html)
    with open('aiwizard.html', 'w') as f:
        f.write(html)
    while input('打开原始HTML与aiwizard，对比效果。如果继续，请输入y') != 'y':
        pass


