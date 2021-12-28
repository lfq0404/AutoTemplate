#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/2 11:30
# @File    : config.py.py
# @Software: Basebit
# @Description:
from zhon.hanzi import punctuation as zh_punc
import constant as cons

# 默认的词频，设置的比较高，尽量让自定义的词组识别出来
DEFAULT_FREQUENCY = 99999999999999

# 扩展选项。当option设定为该值时，需要扩展为TEXT，让用户填写
EXTENSION_OPTIONS = 'EXTENSION_OPTIONS'

# jieba自定义词组
JIEBA_USER_DICTS = [
    ['手术史', DEFAULT_FREQUENCY, 'n'],
    ['家族性', DEFAULT_FREQUENCY, 'n'],
    ['疾病史', DEFAULT_FREQUENCY, 'n'],
    ['减充血剂', DEFAULT_FREQUENCY, 'n'],
    ['侧下', DEFAULT_FREQUENCY, 'n'],
    ['°', DEFAULT_FREQUENCY, 'n'],
    ['kg/m2', DEFAULT_FREQUENCY, 'n'],
    ['冶游史', DEFAULT_FREQUENCY, 'n'],
    ['治游史', DEFAULT_FREQUENCY, 'n'],
    ['婚', DEFAULT_FREQUENCY, 'n'],
    ['额部', DEFAULT_FREQUENCY, 'n'],
    ['枕部', DEFAULT_FREQUENCY, 'n'],
    ['次/分', DEFAULT_FREQUENCY, 'n'],
    ['C5/6', DEFAULT_FREQUENCY, 'n'],
    ['±', DEFAULT_FREQUENCY, 'n'],
    ['Ⅰ', DEFAULT_FREQUENCY, 'n'],
    ['Ⅱ', DEFAULT_FREQUENCY, 'n'],
    ['Ⅲ', DEFAULT_FREQUENCY, 'n'],
    ['无法暴露', DEFAULT_FREQUENCY, 'n'],
    ['Hoffmann’s', DEFAULT_FREQUENCY, 'n'],
    ['hoffman征', DEFAULT_FREQUENCY, 'n'],
    ['未婚未育', DEFAULT_FREQUENCY, 'n'],
    ['已婚未育', DEFAULT_FREQUENCY, 'n'],
    ['已婚已育', DEFAULT_FREQUENCY, 'n'],
    ['清创缝合', DEFAULT_FREQUENCY, 'n'],
    ['育有', DEFAULT_FREQUENCY, 'n'],
    ['吸凹征', DEFAULT_FREQUENCY, 'n'],
    ['呼吸节律', DEFAULT_FREQUENCY, 'n'],
    ['发绀', DEFAULT_FREQUENCY, 'n'],
    ['曾在', DEFAULT_FREQUENCY, 'n'],
    ['或', DEFAULT_FREQUENCY // 10, 'n'],
    ['阳性家族史', DEFAULT_FREQUENCY, 'n'],
    ['反跳痛', DEFAULT_FREQUENCY, 'n'],
    ['足靴区', DEFAULT_FREQUENCY, 'n'],
    ['踝周', DEFAULT_FREQUENCY, 'n'],
    ['导管评估', DEFAULT_FREQUENCY, 'n'],
    ['导管情况', DEFAULT_FREQUENCY, 'n'],
    ['内置', DEFAULT_FREQUENCY, 'n'],
    ['外露', DEFAULT_FREQUENCY, 'n'],
    ['紫暗', DEFAULT_FREQUENCY, 'n'],
    ['冲管', DEFAULT_FREQUENCY, 'n'],
    ['冷', DEFAULT_FREQUENCY, 'n'],
    ['叩', DEFAULT_FREQUENCY, 'n'],
    ['松', DEFAULT_FREQUENCY, 'n'],
    ['2%利多卡因5ml', DEFAULT_FREQUENCY, 'n'],
    ['4%阿替卡因1.7ml', DEFAULT_FREQUENCY, 'n'],
    ['远中龈切/去骨/分牙', DEFAULT_FREQUENCY, 'n'],
    ['有瘀斑', DEFAULT_FREQUENCY, 'n'],
    ['下肢', DEFAULT_FREQUENCY, 'n'],
    ['锌基封', DEFAULT_FREQUENCY, 'n'],
    ['暂封', DEFAULT_FREQUENCY, 'n'],
    ['后突', DEFAULT_FREQUENCY, 'n'],
    ['长期生活于', DEFAULT_FREQUENCY, 'n'],
    ['瘀血证', DEFAULT_FREQUENCY, 'n'],
    ['寒湿证', DEFAULT_FREQUENCY, 'n'],
    ['肾虚证', DEFAULT_FREQUENCY, 'n'],
    ['左下肢足靴区', DEFAULT_FREQUENCY, 'n'],
    ['内侧', DEFAULT_FREQUENCY, 'n'],
    ['外侧', DEFAULT_FREQUENCY, 'n'],
    ['侧方应力试验', DEFAULT_FREQUENCY, 'n'],
    ['气滞血瘀证', DEFAULT_FREQUENCY, 'n'],
    ['肝肾亏虚证', DEFAULT_FREQUENCY, 'n'],
    ['感受外寒证', DEFAULT_FREQUENCY, 'n'],
    ['湿热中阻证', DEFAULT_FREQUENCY, 'n'],
    ['寒湿犯腰证', DEFAULT_FREQUENCY, 'n'],
    ['湿热犯腰证', DEFAULT_FREQUENCY, 'n'],
    ['左寸口细脉', DEFAULT_FREQUENCY, 'n'],
    ['右寸口细脉', DEFAULT_FREQUENCY, 'n'],
    ['S1-12', DEFAULT_FREQUENCY, 'n'],
    ['Fc棉捻', DEFAULT_FREQUENCY, 'n'],
    ['氢氧化钙糊剂', DEFAULT_FREQUENCY, 'n'],
    ['C/D', DEFAULT_FREQUENCY, 'n'],
    ['右：', DEFAULT_FREQUENCY, 'n'],
    ['左：', DEFAULT_FREQUENCY, 'n'],
    ['右眼结膜充血', DEFAULT_FREQUENCY, 'n'],
    ['左眼结膜充血', DEFAULT_FREQUENCY, 'n'],
    ['T', DEFAULT_FREQUENCY, 'n'],
    ['导管是否完整', DEFAULT_FREQUENCY, 'n'],
    ['阻生', DEFAULT_FREQUENCY, 'n'],
    ['废用', DEFAULT_FREQUENCY, 'n'],
    ['弥漫性充血', DEFAULT_FREQUENCY, 'n'],
    ['mg/L', DEFAULT_FREQUENCY, 'n'],
    ['IU/L', DEFAULT_FREQUENCY, 'n'],
    ['umol/l', DEFAULT_FREQUENCY, 'n'],
    ['g/l', DEFAULT_FREQUENCY, 'n'],
    ['mmol/L', DEFAULT_FREQUENCY, 'n'],
    ['充血红肿', DEFAULT_FREQUENCY, 'n'],
    ['风寒阻络证', DEFAULT_FREQUENCY, 'n'],
    ['湿热内蕴证', DEFAULT_FREQUENCY, 'n'],
    ['气血亏虚证', DEFAULT_FREQUENCY, 'n'],
    ['湿热浸淫证', DEFAULT_FREQUENCY, 'n'],
    ['脾虚湿盛证', DEFAULT_FREQUENCY, 'n'],
    ['血虚风燥证', DEFAULT_FREQUENCY, 'n'],
    ['胃苓汤或参苓白术散', DEFAULT_FREQUENCY, 'n'],
    ['双侧瞳孔', DEFAULT_FREQUENCY, 'n'],
    ['固定难以推动', DEFAULT_FREQUENCY, 'n'],
    ['肌卫', DEFAULT_FREQUENCY, 'n'],
    ['左下', DEFAULT_FREQUENCY, 'n'],
    ['口齿', DEFAULT_FREQUENCY, 'n'],
    ['等大等圆', DEFAULT_FREQUENCY, 'n'],
    ['肝脾肋下', DEFAULT_FREQUENCY, 'n'],
    ['活动性', DEFAULT_FREQUENCY, 'n'],
    ['易紧张', DEFAULT_FREQUENCY, 'n'],
    ['经期暂缓', DEFAULT_FREQUENCY, 'n'],

    ['穿刺点及周围皮肤情况', DEFAULT_FREQUENCY * 10, 'n'],
    ['港体及导管处皮肤情况', DEFAULT_FREQUENCY * 10, 'n'],
    ['未冲管', DEFAULT_FREQUENCY * 10, 'n'],
    ['及时间', DEFAULT_FREQUENCY * 10, 'n'],
    ['发生时间', DEFAULT_FREQUENCY * 10, 'n'],
    ['双附件', DEFAULT_FREQUENCY * 10, 'n'],
    ['已告知', DEFAULT_FREQUENCY * 10, 'n'],
    ['未引出', DEFAULT_FREQUENCY * 10, 'n'],
    ['程度', DEFAULT_FREQUENCY * 10, 'n'],
    ['无殊', DEFAULT_FREQUENCY * 10, 'n'],
    ['无渣饮食', DEFAULT_FREQUENCY * 10, 'n'],
    ['如有', DEFAULT_FREQUENCY * 10, 'n'],
    ['可考虑', DEFAULT_FREQUENCY * 10, 'n'],
    ['未来潮', DEFAULT_FREQUENCY * 10, 'n'],
    ['时间：', DEFAULT_FREQUENCY * 10, 'n'],
    ['维护情况', DEFAULT_FREQUENCY * 10, 'n'],
    ['异常情况', DEFAULT_FREQUENCY * 10, 'n'],
    ['一般可', DEFAULT_FREQUENCY * 10, 'n'],
    ['皮肤情况', DEFAULT_FREQUENCY * 10, 'n'],
    ['拔管情况', DEFAULT_FREQUENCY * 10, 'n'],
    ['无明显症状按时复诊', DEFAULT_FREQUENCY * 10, 'n'],
    ['侧', DEFAULT_FREQUENCY * 10, 'n'],
    ['明显红肿', DEFAULT_FREQUENCY * 10, 'n'],
    ['氯双', DEFAULT_FREQUENCY * 10, 'n'],
    ['肩峰下缘', DEFAULT_FREQUENCY * 10, 'n'],
    ['少神', DEFAULT_FREQUENCY * 10, 'n'],
    ['行动自如', DEFAULT_FREQUENCY * 10, 'n'],
    ['行动欠佳', DEFAULT_FREQUENCY * 10, 'n'],
    ['细软无力', DEFAULT_FREQUENCY * 10, 'n'],
    ['明显干湿罗音', DEFAULT_FREQUENCY * 10, 'n'],
    ['/L', DEFAULT_FREQUENCY * 10, 'n'],
    ['多思多虑', DEFAULT_FREQUENCY * 10, 'n'],

    ['时间', DEFAULT_FREQUENCY // 10, 'text'],
    ['[0]', DEFAULT_FREQUENCY, 'text'],
    ['输入', DEFAULT_FREQUENCY, 'text'],
    ['请输入', DEFAULT_FREQUENCY, 'text'],
    ['编辑', DEFAULT_FREQUENCY, 'text'],
    ['情况', DEFAULT_FREQUENCY, 'text'],
    ['/文字描述', DEFAULT_FREQUENCY, 'text'],

    # 在这添加了option，需要在OPTION_MAP中添加对应的解析
    ['有无', DEFAULT_FREQUENCY, 'option'],
    ['无', DEFAULT_FREQUENCY // 10, 'option'],
    ['是否', DEFAULT_FREQUENCY, 'option'],
    ['左右双', DEFAULT_FREQUENCY, 'option'],
    ['左右', DEFAULT_FREQUENCY, 'option'],
    ['右', DEFAULT_FREQUENCY, 'option'],
    ['左', DEFAULT_FREQUENCY, 'option'],
    ['双', DEFAULT_FREQUENCY, 'option'],
    ['(+)', DEFAULT_FREQUENCY, 'option'],
    ['（+）', DEFAULT_FREQUENCY, 'option'],
    ['(-)', DEFAULT_FREQUENCY, 'option'],
    ['（-）', DEFAULT_FREQUENCY, 'option'],
    ['正常', DEFAULT_FREQUENCY, 'option'],
    ['薄', DEFAULT_FREQUENCY, 'option'],
    ['厚', DEFAULT_FREQUENCY, 'option'],
    ['阴性', DEFAULT_FREQUENCY, 'option'],
    ['阳性', DEFAULT_FREQUENCY, 'option'],
    ['已', DEFAULT_FREQUENCY, 'option'],
    ['（+-）', DEFAULT_FREQUENCY, 'option'],
    ['局部', DEFAULT_FREQUENCY, 'option'],
    ['齐', DEFAULT_FREQUENCY, 'option'],
    ['不齐', DEFAULT_FREQUENCY * 10, 'option'],
    ['升高', DEFAULT_FREQUENCY, 'option'],
    ['未及', DEFAULT_FREQUENCY, 'option'],
    ['阳阴性', DEFAULT_FREQUENCY, 'option'],
    ['淡红', DEFAULT_FREQUENCY, 'option'],
    ['白腻', DEFAULT_FREQUENCY, 'option'],
    ['脉滑', DEFAULT_FREQUENCY, 'option'],
    ['可', DEFAULT_FREQUENCY, 'option'],
    ['弦细', DEFAULT_FREQUENCY, 'option'],
    ['粗', DEFAULT_FREQUENCY, 'option'],
    ['两', DEFAULT_FREQUENCY, 'option'],
    ['中上', DEFAULT_FREQUENCY, 'option'],
    ['平软', DEFAULT_FREQUENCY, 'option'],
    ['平', DEFAULT_FREQUENCY // 10, 'option'],
    ['紫绀', DEFAULT_FREQUENCY, 'option'],
    ['潮红', DEFAULT_FREQUENCY, 'option'],
    ['软', DEFAULT_FREQUENCY, 'option'],
    ['切题', DEFAULT_FREQUENCY, 'option'],
    ['桶状', DEFAULT_FREQUENCY, 'option'],
    ['膨隆', DEFAULT_FREQUENCY, 'option'],
    ['轻度', DEFAULT_FREQUENCY, 'option'],
    ['脓性粘性水样血性干酪样', DEFAULT_FREQUENCY, 'option'],
    ['息肉样乳头状桑葚状菜花样', DEFAULT_FREQUENCY, 'option'],
    ['清', DEFAULT_FREQUENCY, 'option'],
    ['颈项部', DEFAULT_FREQUENCY, 'option'],
    ['广泛性', DEFAULT_FREQUENCY, 'option'],
    ['光泽', DEFAULT_FREQUENCY, 'option'],
    ['好', DEFAULT_FREQUENCY, 'option'],
    ['平伏', DEFAULT_FREQUENCY, 'option'],
    ['反光可见', DEFAULT_FREQUENCY, 'option'],
    ['有关节', DEFAULT_FREQUENCY, 'option'],
    ['原籍', DEFAULT_FREQUENCY, 'option'],
    ['骶棘', DEFAULT_FREQUENCY, 'option'],
    ['条索样', DEFAULT_FREQUENCY, 'option'],
    ['肱二头肌、肱三头肌', DEFAULT_FREQUENCY, 'option'],
    ['合作', DEFAULT_FREQUENCY, 'option'],
    ['-/±/+', DEFAULT_FREQUENCY, 'option'],
    ['黄红状', DEFAULT_FREQUENCY, 'option'],
    ['++/+++', DEFAULT_FREQUENCY, 'option'],
    ['下', DEFAULT_FREQUENCY, 'option'],
    ['双侧上', DEFAULT_FREQUENCY, 'option'],
    ['多', DEFAULT_FREQUENCY // 10, 'option'],
    ['红肿', DEFAULT_FREQUENCY // 10, 'option'],
    ['+/-', DEFAULT_FREQUENCY, 'option'],
    ['减轻', DEFAULT_FREQUENCY, 'option'],
    ['不能', DEFAULT_FREQUENCY, 'option'],
    ['减弱', DEFAULT_FREQUENCY, 'option'],
    ['变窄', DEFAULT_FREQUENCY, 'option'],
    ['清晰', DEFAULT_FREQUENCY, 'option'],
    ['居中', DEFAULT_FREQUENCY, 'option'],
    ['明显', DEFAULT_FREQUENCY // 10, 'option'],
    ['无红肿', DEFAULT_FREQUENCY, 'option'],
    ['表面见', DEFAULT_FREQUENCY, 'option'],
    ['薄白', DEFAULT_FREQUENCY, 'option'],
    ['否认', DEFAULT_FREQUENCY, 'option'],
    ['如常', DEFAULT_FREQUENCY, 'option'],
    ['柔软灵活', DEFAULT_FREQUENCY, 'option'],
    ['弦滑', DEFAULT_FREQUENCY, 'option'],
    ['清晰', DEFAULT_FREQUENCY, 'option'],
    ['对称', DEFAULT_FREQUENCY, 'option'],
    ['未闻及', DEFAULT_FREQUENCY, 'option'],
    ['未闻', DEFAULT_FREQUENCY, 'option'],
    ['规律', DEFAULT_FREQUENCY // 10, 'option'],
    ['不规律', DEFAULT_FREQUENCY, 'option'],
]
# 自定义词组存在的词
JIEBA_USER_WORDS = [i[0] for i in JIEBA_USER_DICTS]
# 词性为指定的text，且需要在display中保留的词
RETAIN_TEXTS = ['时间']

# option对应的解析规则
# 1、阴性放前面
# 2、sign标识。
#   0：表示阴阳
#   1：表示枚举，颜色全为orange
#   2：全是阳性，颜色均为red
OPTION_MAP = {
    '有无': [['无', '有'], 0, cons.VALUE_TYPE_RADIO],
    '是否': [['否', '是'], 0, cons.VALUE_TYPE_RADIO],
    '左右双': [['左', '右', '双'], 1, cons.VALUE_TYPE_RADIO],
    '双': [['双', '左', '右'], 1, cons.VALUE_TYPE_RADIO],
    '两': [['两', '左', '右'], 1, cons.VALUE_TYPE_RADIO],
    '左右': [['左', '右'], 1, cons.VALUE_TYPE_RADIO],
    '右': [['左', '右'], 1, cons.VALUE_TYPE_RADIO],
    '左': [['左', '右'], 1, cons.VALUE_TYPE_RADIO],
    '无': [['无', '有'], 0, cons.VALUE_TYPE_RADIO],
    '(+)': [['(-)', '(+)'], 0, cons.VALUE_TYPE_RADIO],
    '(-)': [['(-)', '(+)'], 0, cons.VALUE_TYPE_RADIO],
    '（+）': [['（-）', '（+）'], 0, cons.VALUE_TYPE_RADIO],
    '（-）': [['（-）', '（+）'], 0, cons.VALUE_TYPE_RADIO],
    '（+-）': [['（-）', '（+）'], 0, cons.VALUE_TYPE_RADIO],
    '正常': [['正常', '不正常'], 0, cons.VALUE_TYPE_RADIO],
    '薄': [['正常', '薄', '厚'], 0, cons.VALUE_TYPE_RADIO],
    '厚': [['正常', '薄', '厚'], 0, cons.VALUE_TYPE_RADIO],
    '阴性': [['阴性', '阳性'], 0, cons.VALUE_TYPE_RADIO],
    '阳性': [['阴性', '阳性'], 0, cons.VALUE_TYPE_RADIO],
    '已': [['已', '未'], 0, cons.VALUE_TYPE_RADIO],
    '局部': [['局部'], 1, cons.VALUE_TYPE_RADIO],
    '齐': [['齐', '不齐'], 0, cons.VALUE_TYPE_RADIO],
    '不齐': [['齐', '不齐'], 0, cons.VALUE_TYPE_RADIO],
    '升高': [['正常', '升高', '降低'], 0, cons.VALUE_TYPE_RADIO],
    '未及': [['未及', '可及'], 0, cons.VALUE_TYPE_RADIO],
    '阳阴性': [['阴性', '阳性'], 0, cons.VALUE_TYPE_RADIO],
    '淡红': [['淡红', '无淡红'], 0, cons.VALUE_TYPE_RADIO],
    '白腻': [['无白腻', '白腻'], 0, cons.VALUE_TYPE_RADIO],
    '脉滑': [['脉无滑', '脉滑'], 0, cons.VALUE_TYPE_RADIO],
    '可': [['可', '不可'], 0, cons.VALUE_TYPE_RADIO],
    '清': [['清', '不清'], 0, cons.VALUE_TYPE_RADIO],
    '弦细': [['弦细', '粗'], 0, cons.VALUE_TYPE_RADIO],
    '粗': [['弦细', '粗'], 0, cons.VALUE_TYPE_RADIO],
    '中上': [['右上', '中上', '左上', '右下', '中下', '左下'], 1, cons.VALUE_TYPE_RADIO],
    '平软': [['平软', '僵硬'], 0, cons.VALUE_TYPE_RADIO],
    '平': [['平', '不平'], 0, cons.VALUE_TYPE_RADIO],
    '紫绀': [['紫绀'], 0, cons.VALUE_TYPE_RADIO],
    '潮红': [['潮红'], 0, cons.VALUE_TYPE_RADIO],
    '软': [['软', '硬'], 0, cons.VALUE_TYPE_RADIO],
    '切题': [['切题', '不切题'], 0, cons.VALUE_TYPE_RADIO],
    '桶状': [['桶状'], 1, cons.VALUE_TYPE_RADIO],
    '轻度': [['轻度', '中度', '重度'], 2, cons.VALUE_TYPE_RADIO],
    '一般': [['一般'], 1, cons.VALUE_TYPE_RADIO],
    '脓性粘性水样血性干酪样': [['脓性', '粘性', '水样', '血性', '干酪样'], 2, cons.VALUE_TYPE_RADIO],
    '息肉样乳头状桑葚状菜花样': [['息肉样', '乳头状', '桑葚状', '菜花样'], 2, cons.VALUE_TYPE_RADIO],
    '颈项部': [['颈项部'], 1, cons.VALUE_TYPE_RADIO],
    '广泛性': [['广泛性'], 1, cons.VALUE_TYPE_RADIO],
    '光泽': [['光泽'], 0, cons.VALUE_TYPE_RADIO],
    '好': [['好', '不好'], 0, cons.VALUE_TYPE_RADIO],
    '平伏': [['平伏'], 0, cons.VALUE_TYPE_RADIO],
    '反光可见': [['反光可见', '反光不可见'], 0, cons.VALUE_TYPE_RADIO],
    '有关节': [['无关节', '有关节'], 0, cons.VALUE_TYPE_RADIO],
    '原籍': [['原籍', EXTENSION_OPTIONS], 0, cons.VALUE_TYPE_RADIO],
    '骶棘': [['骶棘', EXTENSION_OPTIONS], 1, cons.VALUE_TYPE_RADIO],
    '条索样': [['条索样', EXTENSION_OPTIONS], 1, cons.VALUE_TYPE_RADIO],
    '肱二头肌、肱三头肌': [['肱二头肌、肱三头肌', '肱二头肌', '肱三头肌'], 1, cons.VALUE_TYPE_RADIO],
    '合作': [['合作', '不配合'], 0, cons.VALUE_TYPE_RADIO],
    '平稳': [['平稳', '急促'], 0, cons.VALUE_TYPE_RADIO],
    '红润': [['红润', '苍白', '发绀'], 0, cons.VALUE_TYPE_RADIO],
    '有力': [['有力', '低钝', '遥远'], 0, cons.VALUE_TYPE_RADIO],
    '-/±/+': [['-', '±', '+'], 0, cons.VALUE_TYPE_RADIO],
    '++/+++': [['-', '+', '++', '+++'], 0, cons.VALUE_TYPE_RADIO],
    '黄红状': [['黄红状'], 0, cons.VALUE_TYPE_RADIO],
    '下': [['下', '上'], 1, cons.VALUE_TYPE_RADIO],
    '多': [['少', '多'], 0, cons.VALUE_TYPE_RADIO],
    '双侧上': [['双侧上', '双侧下', '左侧下', '左侧上', '右侧下', '右侧上'], 1, cons.VALUE_TYPE_RADIO],
    '红肿': [['正常', '红肿'], 0, cons.VALUE_TYPE_RADIO],
    '无红肿': [['无红肿', '红肿'], 0, cons.VALUE_TYPE_RADIO],
    '透明': [['透明', '云翳', '斑翳'], 0, cons.VALUE_TYPE_RADIO],
    '圆': [['圆', '欠圆'], 0, cons.VALUE_TYPE_RADIO],
    '+/-': [['-', '+'], 0, cons.VALUE_TYPE_RADIO],
    'n': [['n', 'n+1', 'n+2', 'n-1'], 0, cons.VALUE_TYPE_RADIO],
    '红': [['红', '暗紫', '有瘀斑'], 0, cons.VALUE_TYPE_RADIO],
    '龋': [['正常', '龋', '缺损'], 0, cons.VALUE_TYPE_RADIO],
    '紧张': [['正常', '紧张'], 0, cons.VALUE_TYPE_RADIO],
    '减轻': [['减轻', '加重'], 0, cons.VALUE_TYPE_RADIO],
    '可以': [['可以', '不能'], 0, cons.VALUE_TYPE_RADIO],
    '不能': [['可以', '不能'], 0, cons.VALUE_TYPE_RADIO],
    '阻生': [['阻生', '废用'], 0, cons.VALUE_TYPE_RADIO],
    '明显': [['不明显', '明显'], 0, cons.VALUE_TYPE_RADIO],
    '减弱': [['正常', '减弱', '增强'], 0, cons.VALUE_TYPE_RADIO],
    '膨隆': [['正常', '膨隆', '凹陷'], 0, cons.VALUE_TYPE_RADIO],
    '变窄': [['正常', '变窄', '变宽'], 0, cons.VALUE_TYPE_RADIO],
    '清晰': [['清晰'], 0, cons.VALUE_TYPE_RADIO],
    '居中': [['居中', '偏左', '偏右'], 0, cons.VALUE_TYPE_RADIO],
    '表面见': [['表面未见', '表面见'], 0, cons.VALUE_TYPE_RADIO],
    '薄白': [['薄白', '厚白'], 0, cons.VALUE_TYPE_RADIO],
    '否认': [['否认', '有'], 0, cons.VALUE_TYPE_RADIO],
    '如常': [['如常'], 0, cons.VALUE_TYPE_RADIO],
    '柔软灵活': [['柔软灵活', '僵硬'], 0, cons.VALUE_TYPE_RADIO],
    '弦滑': [['弦滑', '滑数'], 0, cons.VALUE_TYPE_RADIO],
    '对称': [['对称', '不对称'], 0, cons.VALUE_TYPE_RADIO],
    '未闻及': [['未闻及', '闻及'], 0, cons.VALUE_TYPE_RADIO],
    '未闻': [['未闻及', '闻及'], 0, cons.VALUE_TYPE_RADIO],
    '规律': [['规律', '不规律'], 0, cons.VALUE_TYPE_RADIO],
    '灵敏': [['灵敏', '迟钝'], 0, cons.VALUE_TYPE_RADIO],
    '迟钝': [['灵敏', '迟钝'], 0, cons.VALUE_TYPE_RADIO],
    '存在': [['存在', '不存在'], 0, cons.VALUE_TYPE_RADIO],
    '光滑': [['光滑', '高低不平'], 0, cons.VALUE_TYPE_RADIO],
}

# 全为阳性的选项
POSITIVE_OPTIONS = {'寒湿证', '肾虚证', '瘀血证', '风寒阻络证', '湿热内蕴证', '气血亏虚证', '湿热浸淫证', '脾虚湿盛证', '血虚风燥证'}

# 针对OPTION_MAP拆解的词，作用在display中会有特殊的展示
SPECIAL_OPTION_DISPLAY = {
    '是': '',  # 一般来讲，“是”会省略。是可见 --> 可见
    '否': '不',
}

# TODO：针对有无展示形式不同的结构考虑
POSITIVE_EXTENSION_SEGMENTS = {
    '烟': {
        cons.KEY_LABEL: "烟",
        cons.KEY_DISPLAY: "吸烟：时长{时长}年，频率{频率}支/天",
        cons.KEY_PROPS: {
            cons.KEY_COLOR: "red"
        },
        cons.KEY_ADDITION: [
            {
                cons.KEY_LABEL: '时长',
                cons.KEY_TYPE: cons.VALUE_TYPE_TEXT,
                cons.KEY_VALUE: '',
                cons.KEY_FREETEXTPREFIX: '',
                cons.KEY_FREETEXTPOSTFIX: '',
                cons.KEY_PLACEHOLDER: '',
            },
            {
                cons.KEY_LABEL: '频率',
                cons.KEY_TYPE: cons.VALUE_TYPE_TEXT,
                cons.KEY_VALUE: '',
                cons.KEY_FREETEXTPREFIX: '',
                cons.KEY_FREETEXTPOSTFIX: '',
                cons.KEY_PLACEHOLDER: '',
            },
        ],
        cons.KEY_VALUE: '1'
    },
    '酒': {
        cons.KEY_LABEL: "酗酒",
        cons.KEY_DISPLAY: "酗酒：时长{时长}年，酒量{酒量}ml/天",
        cons.KEY_PROPS: {
            cons.KEY_COLOR: "red"
        },
        cons.KEY_ADDITION: [
            {
                cons.KEY_LABEL: '时长',
                cons.KEY_TYPE: cons.VALUE_TYPE_TEXT,
                cons.KEY_VALUE: '',
                cons.KEY_FREETEXTPREFIX: '',
                cons.KEY_FREETEXTPOSTFIX: '',
                cons.KEY_PLACEHOLDER: '',
            },
            {
                cons.KEY_LABEL: '酒量',
                cons.KEY_TYPE: cons.VALUE_TYPE_TEXT,
                cons.KEY_VALUE: '',
                cons.KEY_FREETEXTPREFIX: '',
                cons.KEY_FREETEXTPOSTFIX: '',
                cons.KEY_PLACEHOLDER: '',
            },
        ],
        cons.KEY_VALUE: '2'
    },
    '婚': {
        cons.KEY_LABEL: "已",
        cons.KEY_DISPLAY: "已婚：{已婚情况}",
        cons.KEY_PROPS: {
            cons.KEY_COLOR: "orange"
        },
        cons.KEY_ADDITION: [
            {
                cons.KEY_LABEL: "已婚情况",
                cons.KEY_TYPE: cons.VALUE_TYPE_RADIO,
                cons.KEY_VALUE: [
                    "0"
                ],
                cons.KEY_OPTIONS: [
                    {
                        cons.KEY_LABEL: "配偶健",
                        cons.KEY_DISPLAY: "配偶健",
                        cons.KEY_PROPS: {
                            cons.KEY_COLOR: "green"
                        },
                        cons.KEY_VALUE: "0",
                        cons.KEY_ADDITION: None
                    },
                    {
                        cons.KEY_LABEL: "配偶亡",
                        cons.KEY_DISPLAY: "配偶亡",
                        cons.KEY_PROPS: {
                            cons.KEY_COLOR: "red"
                        },
                        cons.KEY_VALUE: "1",
                        cons.KEY_ADDITION: None
                    },
                    {
                        cons.KEY_LABEL: "配偶在不健",
                        cons.KEY_DISPLAY: "配偶在不健",
                        cons.KEY_PROPS: {
                            cons.KEY_COLOR: "red"
                        },
                        cons.KEY_VALUE: "2",
                        cons.KEY_ADDITION: None
                    },
                ]
            }
        ],
        cons.KEY_VALUE: '1'
    },
    '育': {
        cons.KEY_LABEL: "已",
        cons.KEY_DISPLAY: "已育：足{足}，早{早}，流{流}，活{活}，子{子}，女{女}",
        cons.KEY_PROPS: {
            cons.KEY_COLOR: "orange"
        },
        cons.KEY_ADDITION: [
            {
                cons.KEY_LABEL: '足',
                cons.KEY_TYPE: cons.VALUE_TYPE_TEXT,
                cons.KEY_VALUE: '',
                cons.KEY_FREETEXTPREFIX: '',
                cons.KEY_FREETEXTPOSTFIX: '',
                cons.KEY_PLACEHOLDER: '',
            },
            {
                cons.KEY_LABEL: '早',
                cons.KEY_TYPE: cons.VALUE_TYPE_TEXT,
                cons.KEY_VALUE: '',
                cons.KEY_FREETEXTPREFIX: '',
                cons.KEY_FREETEXTPOSTFIX: '',
                cons.KEY_PLACEHOLDER: '',
            },
            {
                cons.KEY_LABEL: '流',
                cons.KEY_TYPE: cons.VALUE_TYPE_TEXT,
                cons.KEY_VALUE: '',
                cons.KEY_FREETEXTPREFIX: '',
                cons.KEY_FREETEXTPOSTFIX: '',
                cons.KEY_PLACEHOLDER: '',
            },
            {
                cons.KEY_LABEL: '活',
                cons.KEY_TYPE: cons.VALUE_TYPE_TEXT,
                cons.KEY_VALUE: '',
                cons.KEY_FREETEXTPREFIX: '',
                cons.KEY_FREETEXTPOSTFIX: '',
                cons.KEY_PLACEHOLDER: '',
            },
            {
                cons.KEY_LABEL: '子',
                cons.KEY_TYPE: cons.VALUE_TYPE_TEXT,
                cons.KEY_VALUE: '',
                cons.KEY_FREETEXTPREFIX: '',
                cons.KEY_FREETEXTPOSTFIX: '',
                cons.KEY_PLACEHOLDER: '',
            },
            {
                cons.KEY_LABEL: '女',
                cons.KEY_TYPE: cons.VALUE_TYPE_TEXT,
                cons.KEY_VALUE: '',
                cons.KEY_FREETEXTPREFIX: '',
                cons.KEY_FREETEXTPOSTFIX: '',
                cons.KEY_PLACEHOLDER: '',
            },

        ],
        cons.KEY_VALUE: '1'
    }
}

# 选项的分割线。以下相隔的文本视为选项
OPTION_SPLITS = ['/', '或']

# 不断句的标点符号
# 有些文本书写不规范，此处不能添加顿号
NOT_BROKEN_SENTENCE = ['°', ' ', '(', ')', '（', '）', '+', '-', '’', '：', ':'] + OPTION_SPLITS

# 经常会匹配错的文本，需要删除
# 某些文本满足“只要后面不是跟着 .*[:：] ，就继续匹配”的规则，但实际是不需要的，删除
ERROR_MATCH_TEXTS = [
    '/输入',
    '/$',
    '^/',
    '(?<=^.*[:：])(/)',  # 删除紧跟着type_name的 / 。eg：'既往史：/(与本疾病相关既往史)' --> '既往史：(与本疾病相关既往史)'
    '处理 辅助检查.+emr_reference.+',
    '辅助检查',
    '检验：\s*[无]?\s*$',
]

# 文本预处理，将一些语句增删细节
PRE_TREATMENT_CFG = [
    {
        # 删除非英文之间的空格
        'pat': '(?<=[^a-z])[ ]+(?=[^a-z])',
        'repl': ''
    },
    {
        'pat': '\xa0',
        'repl': '',
    },
    {
        'pat': '吸烟.*饮酒',
        'repl': '烟酒',
    },
    {
        'pat': '[有无]+烟酒\w*',
        'repl': '有无烟、酒等不良嗜好',
    },
    {
        'pat': 'PORT导管通畅',
        'repl': '通畅/不通畅',
    },
    {
        'pat': '导管是否完整： 是/否',
        'repl': '导管是否完整',
    },
    {
        'pat': '：冲管',
        'repl': '：冲管/未冲管',
    },
    {
        'pat': '压痛[、及]反跳痛',
        'repl': '压痛、反跳痛等',
    },
    {
        'pat': '压痛[、及]叩击痛',
        'repl': '压痛、叩击痛等',
    },
    {
        'pat': '左/右下肢足靴区',
        'repl': '左下肢足靴区/右下肢足靴区',
    },
    {
        'pat': '腰\d到腰\d棘突旁',
        'repl': '输入',
    },
    {
        'pat': 'C\d-\d棘突及棘旁两侧',
        'repl': '输入',
    },
    {
        'pat': 'L\d棘突及棘旁',
        'repl': '输入',
    },
    {
        'pat': '神情',
        'repl': '神清',
    },
    {
        'pat': '冷（.*）／（\+\－），叩（.*），松（.*）',
        'repl': '冷(+)，叩(+)，松(+)',
    },
    {
        'pat': '拔管过程\s*拔管过程',
        'repl': '拔管过程：拔管过程'
    },
    {
        'pat': '心率次/分',
        'repl': '心率输入次/分'
    },
    {
        # 将 HR88次/分 --> HR输入次/分
        'pat': '(\d+)(?=次/分)',
        'repl': '输入'
    },
    {
        # 将 BP120/80mmHg --> BP输入mmHg
        'pat': '([\d|/]+)(?=mmHg)',
        'repl': '输入'
    },
    {
        # 将 HR：111bpm --> HR：输入bpm
        'pat': '(\d+)(?=bpm)',
        'repl': '输入'
    },
    {
        # 将 37.8度 --> 输入度
        'pat': '([\d|.]+)(?=度)',
        'repl': '输入'
    },
    {
        # 将 0.2cm --> 输入cm
        'pat': '([\d|.]+)(?=cm)',
        'repl': '输入'
    },
    {
        # 将 伸直 度 --> 伸直输入度
        'pat': '(?<=(伸直|屈曲))()(?=度)',
        'repl': '输入'
    },
    {
        # 全文只有一个“无”字，则直接删除
        'pat': '^\s*无\s*$',
        'repl': ''
    },
    {
        # 冒号紧跟下划线的部分，替换为输入框
        # 1、先处理特殊情况
        'pat': '备注_____',
        'repl': '备注：_____'
    },
    {
        # 冒号后面紧跟的下换线，改为输入
        'pat': '(?<=[:：])([\s_]+)',
        'repl': '输入'
    },
    {
        # “边界|质地”直接以逗号结尾，需要添加输入框
        'pat': '(?<=(边界|质地|浮髌征|过伸试验|屈曲试验))([,，])',
        'repl': '：输入，'
    },
    {
        # “xx”直接以逗号结尾，需要添加阴阳选项
        'pat': '(?<=(浮髌征|过伸试验|屈曲试验|麦氏征|应力试验|研磨试验))(?=[,，。])',
        'repl': '(-)'
    },

    {
        # “形态”直接结尾，需要添加输入框
        'pat': '(?<=形态$)()',
        'repl': '：输入'
    },
    {
        # 直径约 mm --> 空格替换
        'pat': '([\d|/| ]+)(?=mm)',
        'repl': '输入'
    },
    {
        # 拔什么牙
        'pat': '拔　，',
        'repl': '拔输入，'
    },
    {
        # 糖尿病/高血压/下肢动脉硬化闭塞症/下肢血栓闭塞性脉管炎(与本疾病相关既往史) 后添加等
        'pat': '\(与本疾病相关既往史\)',
        'repl': '等'
    },

    {
        'pat': '(?<=(穿刺点及周围皮肤情况|导管评估|肝素封管|更换接头|更换敷料|穿刺点及周围皮肤处理|拔管依据|拔管过程|宫颈)：)([a-zA-Z\u4e00-\u9fa5 ]+)',
        'repl': '输入'
    },
    {
        # 3、肝素封管：肝素封管 ，  --> 3、肝素封管：输入，
        'pat': '港体及导管处皮肤情况\s*港体及导管处皮肤情况',
        'repl': '港体及导管处皮肤情况：输入'
    },
    {
        # 导管通畅：导管通畅  --> 导管通畅：通畅/不通畅
        'pat': '导管通畅：导管通畅',
        'repl': '导管通畅：通畅/不通畅'
    },

    {
        # 为了方便断句，如果是连续的标点符号，则只保留第一个。
        'pat': '(?<=[{punc}])([{punc}]+)'.format(punc='.。？?,，;；'),
        'repl': ''
    },
    {
        # 删除连续的回车，不能与上面的合并
        'pat': '(?<=[{punc}])([{punc}]+)'.format(punc='\n'),
        'repl': ''
    },
    {
        'pat': '长期生活于原籍',
        'repl': '长期生活于原籍'
    },
    {
        'pat': '活动明显受限，([\u4e00-\u9fa5]+?)压痛',
        'repl': '活动明显受限，输入压痛'
    },
    {
        'pat': '具体时间、输血量',
        'repl': '具体时间：输入、输血量：输入'
    },
    {
        'pat': '心率是/否齐',
        'repl': '心率齐'
    },
    {
        'pat': '，编辑，',
        'repl': '，'
    },
    {
        'pat': '可见一大小约溃疡',
        'repl': '可见一大小约输入溃疡'
    },
    {
        'pat': '虹膜虹膜病理类型',
        'repl': '虹膜病理类型：输入'
    },
    {
        'pat': '晶体清/浑浊,混浊晶体混浊类型',
        'repl': '晶体清/浑浊'
    },
    {
        'pat': '玻璃体清/浑浊视盘边界清/模糊',
        'repl': '玻璃体清/浑浊，视盘边界清/模糊'
    },
    {
        'pat': '右：\[0\]左：\[0\]输入mmHg',
        'repl': '右：输入mmHg，左：输入mmHg'
    },
    {
        # 角膜透明/文字描述，可以利用两个字符间的输入框兼容“文字描述”，所以直接删除
        'pat': '/文字描述',
        'repl': ''
    },
    {
        'pat': 'Tn/n\+1/n\+2/n-1',
        'repl': 'T：n/n+1/n+2/n-1'
    },
    {
        'pat': '口角左/右歪斜舌苔白腻',
        'repl': '口角左/右歪斜，舌苔白腻'
    },
    {
        'pat': '已/未婚',
        'repl': '已婚'
    },
    {
        'pat': '时间：输入地点：',
        'repl': '时间：输入，地点：'
    },
    {
        # （+）后添加标点符号
        'pat': '(（\+）|（\-）)(?![{}])'.format(zh_punc),
        'repl': r'\1，'
    },
    {
        # 口淡不渴，或渴喜热饮
        'pat': '，或',
        'repl': '或'
    },
    {
        'pat': '弥漫性充血，肿胀',
        'repl': '弥漫性充血/肿胀'
    },
    {
        'pat': '外耳道内有稀薄',
        'repl': '外耳道内有无稀薄'
    },
    {
        # 将以下文字删除
        'pat': '(具体情况，部位|/\s*$)',
        'repl': ''
    },
    {
        'pat': '部位有/无',
        'repl': '有/无'
    },
    {
        'pat': '皮疹，症状',
        'repl': '皮疹'
    },
    {
        'pat': '明显受限C5-7',
        'repl': '明显受限，C5-7'
    },
    {
        'pat': '宫体：宫体位置',
        'repl': '宫体：输入'
    },
    {
        'pat': '（—）',
        'repl': '（-）'
    },
    {
        'pat': '\(日期\)',
        'repl': '(输入)'
    },
    {
        'pat': '，充血红肿，',
        'repl': '，有无充血红肿，'
    },
    {
        'pat': 'G输入P输入',
        'repl': 'G输入，P输入'
    },
    {
        'pat': '1.湿热浸淫证2.脾虚湿盛证3.血虚风燥证',
        'repl': '湿热浸淫证/脾虚湿盛证/血虚风燥证'
    },
    {
        'pat': '左寸口弦滑，右寸口滑数',
        'repl': '左寸口弦滑'
    },
    {
        'pat': '有无既往疾病史，既往疾病史',
        'repl': '有无既往疾病史'
    },
    {
        'pat': '。治疗方式',
        'repl': ''
    },
    {
        'pat': '，具体因何疾病作何手术，手术\(输入\)及手术结果',
        'repl': ''
    },
    {
        'pat': '，外伤\(输入\)、部位、程度、诊疗结果',
        'repl': ''
    },
    {
        'pat': '是否可及',
        'repl': '可及'
    },
    {
        'pat': '等大.等圆',
        'repl': '等大等圆'
    },
    {
        'pat': '等大.等圆',
        'repl': '等大等圆'
    },
    {
        'pat': '，药物名称、计量、服用时间',
        'repl': ''
    },
    {
        'pat': '\[0\]输入',
        'repl': '输入'
    },
    {
        'pat': '/LHB',
        'repl': '/L，HB'
    },
    {
        'pat': '/LPLT',
        'repl': '/L，PLT'
    },
    {
        'pat': '/LMCV',
        'repl': '/L，MCV'
    },
    {
        'pat': '\]MCHC',
        'repl': ']，MCHC'
    },
    {
        'pat': '，致敏原名称、发生时间、反应类型和程度',
        'repl': '过敏史'
    },
    {
        'pat': '，外伤日期、部位、程度、诊疗结果',
        'repl': ''
    },
    {
        'pat': '具体因何疾病作何手术，手术日期及手术结果',
        'repl': ''
    },
    {
        'pat': '部位',
        'repl': ''
    },
    {
        'pat': '发病时间，慢性疾病史类型',
        'repl': ''
    },
    {
        'pat': '发病时间，传染性疾病史类型',
        'repl': ''
    },

]
_ENUM_DISEASES = ['高血压', '脑梗塞', '糖尿病', '哮喘病', '心脏病']
PRE_TREATMENT_CFG += [
    {
        # 高血压等关键词前面有特定标点符号，且后面没有跟“等”字，则自动添加“等”
        # 有无糖尿病、脑梗塞、高血压 --> 有无糖尿病、脑梗塞、高血压等
        # TODO：怎么把以下两个正则合并
        'pat': '(?<=、)({})(?![史、等])'.format('|'.join(_ENUM_DISEASES)),
        'repl': r'\1等'
    },
    {
        'pat': '(?<=、)({}史)(?![、等])'.format('史|'.join(_ENUM_DISEASES)),
        'repl': r'\1等'
    },

    {
        # 将xx,xx等，视为完整的一句话
        'pat': '(?<=等[\u4e00-\u9fa5]*)(，)',
        'repl': '。'
    },
]
# 以下内容直接展示在display中
DISPLAY_SENTENCE_TEXTS = [
    '末次月经',
    '留观半小时无殊后予离开诊室',
    '主动活动上举后弯较前好转',
    # '角膜光泽，前房清，虹瞳好，晶体清，眼底：视盘边界清，网膜平伏，黄斑中心反光可见',
    '今去龋尽，备洞，酒精消毒，VOCO垫底',
    '远中龈切/去骨/分牙，顺利，置明胶海绵，纱布咬合，告医嘱',
    '肌肉痉挛',
    '腰痛',
    '弯腰及转身活动受限',
    '生理弧度消失',
    '术顺',
    '深龋',
    '探诊疼痛',
    '2.今去龋，备洞，及穿髓点，置多聚甲醛失活剂',
    '流行病学史：',
    '四诊摘要：',
    '今去封，扩根至40#，测根长，氯双及NS冲洗，吸干，',
    '2、 维护情况：',
    '压框等疼痛刺激反应',
    '如有明显不适及时来院就诊',
    '减量或停药',
    '未发现明显异常',
    ' 1.龙胆泻心汤合五味消毒饮加减2.除湿胃苓汤或参苓白术散加减3.当归引子加减',
]

# 当遇到以下内容，需要临时调整jieba自定义词组
SPECIAL_WORDS = [
    ['/有阳性家族史', ['有阳性家族史', 'n']],
    ['体质一般', ['一般', 'option']],
    ['有无咽部红肿', ['咽部红肿', 'n']],
    ['关节无红肿畸形', ['红肿畸形', 'n']],
    ['输入压痛明显', ['压痛明显', 'n']],
]

# 无穷枚举中可能出现的前缀词，将相关的词放在display中
INFINITE_ENUM_FREFIX = ['服用', '长期生活于']

# HTML转纯文本时的特殊替换
HTML2TEXT_REPLACE = [
    {
        'pat': '有无\n',
        'repl': '有无'
    },
    {
        'pat': '\n地点',
        'repl': '地点'
    },
    {
        'pat': '\n四诊摘要',
        'repl': '四诊摘要'
    },
    {
        # 在这几个词前面加空格，要不然“4090100-门诊中医内科-中医内科(初诊)模板-门诊病历(初诊).html”不好分段
        'pat': '(患者神色|舌象|脉象)',
        'repl': r' \1',
    },

]
