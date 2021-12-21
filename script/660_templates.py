#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/20 18:32
# @File    : 660_templates.py
# @Software: Basebit
# @Description:
import os
import re
import pandas
import pandas as pd

depart_cfg = {
    '4080100': '门诊高血压',
    '4420004': '核酸开单',
    '4420005': '核酸开单(北部)',
    '4420000': '预防保健科',
    '4220100': '门诊感染病',
    '4121601': '门诊乳腺中心',
    '4030100': '门诊内分泌',
    '4010100': '门诊消化',
    '4080101': '门诊高血压(北部)',
    '4070100': '门诊呼吸科',
    '4040100': '门诊肾脏',
    '4300500': '门诊疼痛',
    '4200201': '门诊妇科(北部)',
    '4201500': '门诊生殖中心',
    '4320100': '门诊心理科',
    '4010101': '门诊消化(北部)',
    '4020100': '门诊心脏',
    '4160100': '门诊烧伤整形',
    '4120700': '甲血外',
    '4200200': '门诊妇科',
    '4140100': '门诊泌外',
    '4431000': '急诊发热',
    '4060100': '门诊神内',
    '4250100': '门诊耳鼻咽喉科',
    '4420002': '预防保健科(北部)',
    '4260100': '门诊皮肤科',
    '4230100': '门诊眼科',
    '4370500': '特需门诊',
    '4220101': '门诊感染病(北部)',
    '4430100': '急诊内科',
    '4430101': '急诊内科(北部)',
    '4431001': '急诊发热(北部)',
    '4180100': '门诊伤科',
    '4120401': '急诊外科（北部）',
    '4130100': '门诊胸外',
    '3050100': '门诊放疗',
    '4190100': '骨科',
    '4030101': '门诊内分泌(北部)',
    '4070101': '门诊呼吸科(北部)',
    '4121900': '门诊胃肠外科',
    '4050100': '门诊血液',
    '4221500': '胰腺外一',
    '4120400': '急诊普外科',
    '4100203': '门诊儿内(北部)',
    '4020101': '门诊心脏(北部)',
    '4100301': '急诊儿内科(北部)',
    '4160200': '急诊烧伤整形',
    '4360117': '九舍门诊普内科',
    '4280000': '门诊推拿科',
    '4120201': '门诊普外(北部)',
    '4510100': '门诊风湿免疫',
    '4431201': '临观普内科',
    '4060101': '门诊神内(北部)',
    '3020000': '病理科',
    '4240100': '门诊口腔科',
    '4100200': '门诊儿内',
    '4230101': '门诊眼科(北部)',
    '4200100': '门诊产科',
    '4120800': '胃肠外三',
    '4340100': '门诊核医学',
    '4270000': '门诊针灸科',
    '4260101': '门诊皮肤科(北部)',
    '3060100': '门诊超声',
    '4030102': '门诊内分泌(远洋)',
    '4140101': '门诊泌外(北部)',
    '4190101': '门诊骨科(北部)',
    '4060300': '急诊神内科',
    '4250101': '门诊耳鼻喉科(北部)',
    '4120600': '肝胆外',
    '4040101': '门诊肾脏(北部)',
    '4090100': '门诊中医内科',
    '4190700': '急诊骨科',
    '4140300': '急诊泌外科',
    '3060101': '门诊超声(北部)',
    '4430500': '急诊抢救室',
    '4121800': '门诊肿瘤',
    '4370509': '全科医学科特需',
    '3100201': '质子放疗门诊',
    '4100300': '急诊儿内科',
    '80600': '护理专病门诊',
    '4500100': '门诊心外科',
    '4290101': '门诊康复科(北部)',
    '4130101': '门诊胸外(北部)',
    '4050600': '血液二',
    '4150700': '门诊功能神外',
    '4430501': '急诊抢救室(北部)',
    '4201501': '门诊生殖中心(北部)',
    '4180101': '门诊伤科(北部)',
    '4090102': '门诊中医内科(北部)',
    '4050200': '急诊血液',
    '4290100': '门诊康复科',
    '4300502': '麻醉评估门诊(北部)',
    '4150100': '门诊神外',
    '4121401': '门诊肝移植',
    '4210100': '门诊儿外',
    '4090200': '门诊中医外科',
    '4260600': '门诊激光室',
    '4150300': '急诊神外',
    '4260200': '急诊皮肤科',
    '4120200': '门诊普外',
    '4161101': '门诊创面修复中心',
    '4160101': '门诊烧伤整形(北部)',
    '4360140': '门诊老年病（北部）',
    '4340101': '门诊核医学(北部)',
    '4210101': '门诊儿外(北部)',
    '4320101': '门诊心理科(北部)',
    '4240101': '门诊口腔科(北部)',
    '4360103': '老年病门诊',
    '4050101': '门诊血液(北部)',
    '80601': '护理专病门诊(北部)',
    '3100400': '质子核医学科',
    '4350100': '营养门诊',
    '4360115': '九舍门诊内分泌',
    '3101800': '质子中心门诊',
    '4090500': '门诊中医五官',
    '4360123': '九舍门诊消化',
    '110701': '整合门诊',
    '4300501': '门诊疼痛(北部)',
    '4150101': '门诊神外(北部)',
    '4500200': '急诊心外科',
    '4360125': '九舍门诊心脏',
    '4360114': '九舍门诊泌外',
    '4230200': '急诊眼科',
    '3040100': '门诊放射',
    '3110100': '门诊放射介入',
    '4121801': '门诊肿瘤(北部)',
    '4420003': '预防保健科(远洋)',
    '4390300': '微创外科中心门诊',
    '4431202': '临观神内科',
    '3100301': '质子肿瘤门诊',
    '4270100': '门诊针灸科(北部)',
    '4201400': '急诊生殖中心',
    '4360138': 'N门诊老年病',
    '4360126': '九舍门诊血液',
    '3102701': '特需门诊(质子)',
    '4360113': '九舍门诊口腔科',
    '4130202': '胸痛急诊(北部)',
    '4360110': '九舍门诊呼吸科',
    '4360127': '九舍门诊眼科',
    '4270200': '门诊针灸（远洋）',
    '4360120': '九舍门诊神内',
    '4360129': '九舍门诊中医内',
    '4360139': '九舍麻醉评估门诊',
    '4360122': '九舍门诊肾脏',
    '3040102': '门诊放射(北部)',
    '3020400': '门诊病理科(北部)',
    '4120900': '胃肠外一',
    '4200500': '急诊妇产科',
    '4500101': '门诊心外科(北部)',
    '4290102': '门诊康复科(远洋)',
    '4540000': '全科医学科',
    '4360104': '九舍急诊内科',
    '4360109': '九舍门诊骨科',
    '4220300': '急诊肠道科',
    '4360105': '九舍门诊耳鼻喉科',
    '4130200': '急诊胸外科',
    '3101200': '质子超声科',
    '4360116': '九舍门诊皮肤科',
    '4431600': '急诊创伤外科',
    '4080102': '门诊高血压科（远洋）',
    '4350101': '营养门诊(北部)',
    '4360119': '九舍门诊伤科',
    '4360133': '九舍门诊推拿',
    '4380700': '门诊手术室(北部)',
    '4120203': '门诊外科（远洋）',
    '3103000': '质子中心中医内科',
    '4450200': '胃肠外二',
    '4370503': '特需体检',
    '4040102': '门诊肾内科（远洋）',
    '4040500': '血透室',
    '4020102': '门诊心内科（远洋）',
    '4431601': '急诊创伤外科(北部)',
    '4090101': '门诊膏方',
    '4360106': '九舍门诊妇科',
    '4360118': '九舍门诊普外',
    '4360112': '九舍门诊康复科',
    '4100900': '儿科夜门诊',
    '4360143': '九舍门诊乳腺外科',
    '4360107': '九舍门诊高血压',
    '110900': '门诊手术',
    '4250200': '急诊耳鼻咽喉科',
    '4360144': '九舍门诊老年综合评估',
    '4230201': '急诊眼科(北部)',
    '4250201': '急诊耳鼻咽喉科(北部)',
    '4150301': '急诊神外(北部)',
    '4431206': '临观神外科',
    '1010200': '广慈门诊',
}


def main():
    g = os.walk('/Users/jeremy.li/Basebit/Documents/develop/smart/20211013-瑞金门急诊模板配置/20211220-门诊660')

    files = []
    types = []
    depart_ids = []
    departs = []
    diseases = []
    for path, _, file_list in g:
        for ind, file in enumerate(file_list):
            if 'html' not in file:
                continue
            files.append(file)
            file = file[:-41]
            try:
                type_ = re.findall(('初诊|复诊|配药'), file)[0]
            except:
                type_, depart_id, disease = get_type_except(file)
                print(disease)
                print()

            else:
                depart_id = re.findall('\((\d+)\)', file)[0]
                # type_, file = '初诊', '门诊病历(初诊)_胃癌(4121900)门诊病历(初诊)'
                disease = get_disease(type_, file)
                print(disease)
                print()

            types.append(type_)
            depart_ids.append(depart_id)
            departs.append(depart_cfg.get(depart_id))
            diseases.append(disease)

    df = pd.DataFrame({
        '模板类型': types,
        '科室id': depart_ids,
        '科室名': departs,
        '疾病': diseases,
        '文件名': files,
    })
    df.to_excel('660_templates.xlsx')


def get_type_except(file):
    """
    获取type失败的类型解析
    :param file:
    :return:
    """
    # 肱骨外伤(1170100)肱骨外伤
    temp = re.findall('^(.+)\((\d+)\)(.+)$', file)
    if temp and temp[0][0] == temp[0][-1]:
        return '', temp[0][1], temp[0][0]
    # 门诊病历(配造口产品)模板(0080600)门诊病历(配造口产品)
    temp = re.findall('^门诊病历[\(（](.+)[\)）].*\((\d+)\)门诊病历', file)
    if temp:
        return '', temp[0][1], temp[0][0]
    if file == '阴道出血（首诊）(1180100)阴道出血（首诊）':
        return '初诊', '80100', '阴道出血'
    if file == '配静脉护理产品模板(0080600)配静脉护理产品':
        return '配药', '0080600', '配静脉护理产品'
    if file == '抢救室下午查房(1280600)抢救室下午-夜班查房':
        return '', '1280600', ''
    else:
        raise ValueError()


def model_pat_findall(text, model):
    """
    根据model进行匹配
    TODO：有bug
    :param text: ababcb
    :param model: xyx
    :return: ['aba', 'bab', 'bcb']
    """

    def ptn(s):
        l = []
        t = set()
        for c in s:
            if c not in t:
                l.append(r'(?P<%s>\w)' % c)
                t.add(c)
            else:
                l.append(r'(?P=%s)' % c)
        return '(?=(%s))' % ''.join(l)

    return [x[0] for x in re.compile(ptn(model)).findall(text)]


def get_disease(type_, text):
    """
    获取疾病信息
    :param text:
    :return:
    """
    # 门诊病历(初诊)-一般模板(4360116)门诊病历(初诊)
    disease = re.findall('^门诊病例\({}\)(.+?)\('.format(type_), text)
    if disease:
        return disease[0]
    # 肺癌及胸痛(复诊)(1120100)肺癌及胸痛(复诊)
    # 拔牙（初诊简易版）(1220100)拔牙（初诊简易版）
    disease = re.findall('^([^门诊]+?)[\(（]{}.*?[\)）]'.format(type_), text)
    if disease:
        return disease[0]
    # 慢性阻塞性肺病急性加重-高干复诊(4360117)慢性阻塞性肺病急性加重-高干复诊
    disease = re.findall('^([^门诊]+?)-.*{}'.format(type_), text)
    if disease:
        return disease[0]
    # 哮喘复诊(1100100)哮喘复诊
    disease = re.findall('^(.+?){}\(\d+\)'.format(type_), text)
    if disease:
        return disease[0]
    # 门诊病历(复诊)-颈椎病(4270000)门诊病历(复诊)
    disease = re.findall('^门诊病历[\(（]{}[\)）]-(.+?)[\(（]\d+[\)）]'.format(type_), text)
    if disease:
        return disease[0]
    # 腰背痛及骨关节炎(4190100)门诊病历(初诊)
    disease = re.findall('^([^\(\)]+?)[\(（]\d+[\)）].+[\(（]{}[\)）]'.format(type_), text)
    if disease:
        return disease[0]
    # 门诊病历(初诊)_胃癌(4121900)门诊病历(初诊)
    disease = re.findall('^门诊病历[\(（]{}[\)）](.+?)\(\d'.format(type_), text)
    if disease:
        return disease[0]
    # 脑病-气虚血瘀证(初诊)模板(4090100)脑病-气虚血瘀证(初诊)
    disease = re.findall('^([^门诊]+?)[\(（]{}[\)）]'.format(type_), text)
    if disease:
        return disease[0]
    # 门诊病历(胸痛复诊)(1283100)门诊病历(胸痛复诊)
    disease = re.findall('^门诊病历[\(（](.+?){}[\)）]'.format(type_), text)
    if disease:
        return disease[0]
    # 门诊病历(造口护理（首次随访-复诊出现问题）)模板(0080600)
    disease = re.findall('^门诊病历[\(（](.+?)（.+）[\)）]'.format(type_), text)
    if disease:
        return disease[0]
    # 甲状腺机能亢进门诊电子病历(复诊)(1030100)甲状腺机能亢进门诊电子病历(复诊)
    disease = re.findall('^(.+?)(门诊电子病历|门诊病历|门急诊|门诊病史|通用门诊|门诊)[\(（]{}[\)）]'.format(type_), text)
    if disease:
        return disease[0][0]

    print()


if __name__ == '__main__':
    main()
