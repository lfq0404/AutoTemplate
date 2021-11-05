#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/2 11:30
# @File    : config.py.py
# @Software: Basebit
# @Description:
from zhon.hanzi import punctuation as zh_punc

# 默认的词频，设置的比较高，尽量让自定义的词组识别出来
DEFAULT_FREQUENCY = 99999999999999
# jieba自定义词组
JIEBA_USER_WORDS = [
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
    ['穿刺点及周围皮肤情况', DEFAULT_FREQUENCY * 10, 'n'],
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

    ['[0]', DEFAULT_FREQUENCY, 'text'],
    ['时间', DEFAULT_FREQUENCY // 10, 'text'],
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
    ['细', DEFAULT_FREQUENCY, 'option'],
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
    ['减轻', DEFAULT_FREQUENCY, 'option'],
    ['清', DEFAULT_FREQUENCY, 'option'],
    ['颈项部', DEFAULT_FREQUENCY, 'option'],
    ['广泛性', DEFAULT_FREQUENCY, 'option'],
    ['光泽', DEFAULT_FREQUENCY, 'option'],
    ['好', DEFAULT_FREQUENCY, 'option'],
    ['平伏', DEFAULT_FREQUENCY, 'option'],
    ['反光可见', DEFAULT_FREQUENCY, 'option'],
    ['有关节', DEFAULT_FREQUENCY, 'option'],
]

# 词性为指定的text，且需要在display中保留的词
RETAIN_TEXTS = ['时间']

# option对应的解析规则
# 1、阴性放前面
# 2、第二位表示开始的索引值。如果表示阴阳，从0开始；如果表示枚举，从1开始。
OPTION_MAP = {
    '有无': [['无', '有'], 0],
    '是否': [['否', '是'], 0],
    '左右双': [['左', '右', '双'], 1],
    '双': [['左', '右', '双'], 1],
    '两': [['左', '右', '两'], 1],
    '左右': [['左', '右'], 1],
    '右': [['左', '右'], 1],
    '左': [['左', '右'], 1],
    '无': [['无', '有'], 0],
    '(+)': [['(-)', '(+)'], 0],
    '(-)': [['(-)', '(+)'], 0],
    '（+）': [['（-）', '（+）'], 0],
    '（-）': [['（-）', '（+）'], 0],
    '（+-）': [['（-）', '（+）'], 0],
    '正常': [['正常', '不正常'], 0],
    '薄': [['正常', '薄', '厚'], 0],
    '厚': [['正常', '薄', '厚'], 0],
    '阴性': [['阴性', '阳性'], 0],
    '阳性': [['阴性', '阳性'], 0],
    '已': [['已', '未'], 0],
    '局部': [['局部'], 1],
    '齐': [['齐', '不齐'], 0],
    '不齐': [['齐', '不齐'], 0],
    '升高': [['正常', '升高', '降低'], 0],
    '未及': [['未及', '有'], 0],
    '阳阴性': [['阴性', '阳性'], 0],
    '淡红': [['淡红', '无淡红'], 0],
    '白腻': [['无白腻', '白腻'], 0],
    '脉滑': [['脉无滑', '脉滑'], 0],
    '可': [['可', '不可'], 0],
    '清': [['清', '不清'], 0],
    '细': [['细', '粗'], 0],
    '粗': [['细', '粗'], 0],
    '中上': [['右上', '中上', '左上', '右下', '中下', '左下'], 1],
    '平软': [['平软', '僵硬'], 0],
    '平': [['平', '不平'], 0],
    '紫绀': [['紫绀'], 0],
    '潮红': [['潮红'], 0],
    '软': [['软'], 0],
    '切题': [['切题', '不切题'], 0],
    '桶状': [['桶状'], 1],
    '轻度': [['轻度', '重度'], 1],
    '一般': [['一般'], 1],
    '减轻': [['减轻', '加重'], 1],
    '脓性粘性水样血性干酪样': [['脓性', '粘性', '水样', '血性', '干酪样'], 1],
    '息肉样乳头状桑葚状菜花样': [['息肉样', '乳头状', '桑葚状', '菜花样'], 1],
    '颈项部': [['颈项部'], 1],
    '广泛性': [['广泛性'], 1],
    '光泽': [['光泽'], 0],
    '好': [['好', '不好'], 0],
    '平伏': [['平伏'], 0],
    '反光可见': [['反光可见', '反光不可见'], 0],
    '有关节': [['无关节', '有关节'], 0],
}
# 针对OPTION_MAP拆解的词，作用在display中会有特殊的展示
SPECIAL_OPTION_DISPLAY = {
    '是': '',  # 一般来讲，“是”会省略。是可见 --> 可见
    '否': '不',
}
# 选项的分割线。以下相隔的文本视为选项
OPTION_SPLITS = ['/', '或']

# 不断句的标点符号
NOT_BROKEN_SENTENCE = ['°', ' ', '(', ')', '（', '）', '+', '-', '’', '：', ':'] + OPTION_SPLITS

# 经常会匹配错的文本，需要删除
ERROR_MATCH_TEXTS = [
    '/输入', '/$', '^/',
    '(?<=^.*[:：])(/)',  # 删除紧跟着type_name的 / 。eg：'既往史：/(与本疾病相关既往史)' --> '既往史：(与本疾病相关既往史)'
    '辅助检查', '检验：\s*[无]?\s*$',
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
        'pat': '[有|无]烟酒',
        'repl': '有无烟、酒',
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
        'pat': '冷（.*）／（\+\－），叩（.*），松（.*）',
        'repl': '冷(+)，叩(+)，松(+)',
    },
    {
        'pat': '拔管过程 拔管过程 ',
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
        # 将 伸直 度 --> 伸直输入度
        'pat': '(?<=(伸直 |屈曲))()(?=度)',
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
        'pat': '(?<=(浮髌征|过伸试验|屈曲试验|麦氏征|应力试验 |研磨试验))(?=[,，。])',
        'repl': '(-)'
    },

    {
        # “形态”直接结尾，需要添加输入框
        'pat': '(?<=[形态]$)()',
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
        # 3、肝素封管：肝素封管 ，  --> 3、肝素封管：输入，
        'pat': '(?<=(穿刺点及周围皮肤情况|导管评估|肝素封管|更换接头|更换敷料|穿刺点及周围皮肤处理|拔管依据|拔管过程)：)([a-zA-Z\u4e00-\u9fa5 ]+)',
        'repl': '输入'
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
        'repl': '长期是否生活于原籍'
    },
    {
        # （+）后添加标点符号
        'pat': '(（\+）|（\-）)(?![{}])'.format(zh_punc),
        'repl': r'\1，'
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
    '流行病学史',
]

# 当遇到以下内容，需要临时调整jieba自定义词组
SPECIAL_WORDS = [
    ['/有阳性家族史', ['有阳性家族史', 'n']],
    ['体质一般', ['一般', 'option']],
]
# 无穷枚举中可能出现的前缀词
INFINITE_ENUM_FREFIX = ['服用']
