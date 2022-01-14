import os

import pandas as pd
from selenium import webdriver
import time
import re

check_files = [
    "门诊病历(初诊)-矮小症(4100200)门诊病历(初诊)32f2bead-82f8-4b3d-9d2d-1dc925374152.html",
    "门诊病历(初诊)-川崎病(4100200)门诊病历(初诊)673cfa66-16d7-4409-901b-fc5f9d743d8b.html",
    "儿科门诊(初诊)(4100200)门诊病历(初诊)703ccfdf-4e4e-4e89-b9d6-38f4893495b8.html",
    "门诊病历(初诊)-发绀(4100200)门诊病历(初诊)502cd87b-ea33-4f8d-b719-fd8f5cc0e454.html",
    "门诊病历(初诊)-发热(4100200)门诊病历(初诊)91b5fe76-b9a4-4921-a8a2-0ba9d5c4e171.html",
    "门诊病历(初诊)-肥胖(4100200)门诊病历(初诊)0a7cc1d9-0233-45d2-a839-6794aef0bac0.html",
    "门诊病历(初诊)-腹泻(4100200)门诊病历(初诊)9c82fe0f-991c-4fd2-90fb-59f3bc0047ab.html",
    "门诊病历(初诊)-呼吸困难(4100200)门诊病历(初诊)f3a76ffe-91cb-41c9-ab94-ad2686d000a3.html",
    "门诊病历(初诊)-昏迷(4100200)门诊病历(初诊)013ce9dc-bade-4fc8-bc83-645b61b6774b.html",
    "门诊病历(初诊)-甲亢(4100200)门诊病历(初诊)6b428835-09df-4d21-ad2c-63f014b8ec9b.html",
    "门诊病历(初诊)-甲亢危象(4100200)门诊病历(初诊)0d23328a-3335-486c-8d1d-d7884a2e8309.html",
    "门诊病历(初诊)-甲状腺炎(4100200)门诊病历(初诊)c5fc7a9d-03b6-4e4d-8926-3fee657c405f.html",
    "门诊病历(初诊)-惊厥(4100200)门诊病历(初诊)ebd1797f-34e4-4015-976a-90ea77c75a82.html",
    "门诊病历(初诊)-剧烈啼哭(4100200)门诊病历(初诊)b8e53328-cf28-4b02-a467-043592ec109e.html",
    "门诊病历(初诊)-咳嗽(4100200)门诊病历(初诊)c6086902-699b-4a01-a880-78bfd1777e10.html",
    "门诊病历(初诊)-淋巴结肿大(4100200)门诊病历(初诊)8cf66c96-e6d0-40cb-95fb-0d7a7be72875.html",
    "门诊病历(初诊)-尿路感染(4100200)门诊病历(初诊)45d9927b-a354-4fb4-b703-9a6f1afdc0b7.html",
    "门诊病历(复诊)-复诊(4100200)门诊病历(复诊)ea348fbf-64a0-4301-a3c2-b5e156420602.html",
    "门诊病历(初诊)-溶血危象(4100200)门诊病历(初诊)a4611126-9d5a-4a1d-a127-d9b09d608a30.html",
    "门诊病历(初诊)-肾上腺(4100200)门诊病历(初诊)c156f07d-0c61-4283-a986-24bda69d096a.html",
    "门诊病历(初诊)-肾上腺危象(4100200)门诊病历(初诊)a03575bd-5100-4753-afb0-d2eb82c7adc6.html",
    "门诊病历(初诊)-四肢麻木(4100200)门诊病历(初诊)f34f2a54-37d1-40eb-af49-4bf5e1f07052.html",
    "门诊病历(初诊)-糖尿病(4100200)门诊病历(初诊)0b06a3ed-db63-4131-a0ce-9fcd2f4f95eb.html",
    "门诊病历(初诊)-糖尿病酮症(4100200)门诊病历(初诊)e10b8ab4-6099-4159-948f-1c112ad80682.html",
    "门诊病历(初诊)-头痛(4100200)门诊病历(初诊)1b9eb8f0-17db-45f2-b0ad-10a813cdfaf8.html",
    "门诊病历(初诊)-性发育异常(4100200)门诊病历(初诊)4c7f6977-5cfb-4925-9ce2-3d5bc4fdbb37.html",
    "门诊病历(初诊)-胸闷(4100200)门诊病历(初诊)2dc03c6b-51b1-4526-aa4a-03a04160c313.html",
    "门诊病历(初诊)-胸痛(4100200)门诊病历(初诊)57d12cd2-e937-4076-95ad-ff24b40f491b.html",
    "门诊病历(初诊)-血尿(4100200)门诊病历(初诊)cf17be78-6b93-436b-934d-8551f1e6b51d.html",
    "儿科门诊(复诊)(4100200)门诊病历(复诊)142595dc-35b1-4567-98c1-c2670ceed1e5.html",
    "门诊病历(复诊)-矮小症(4100200)门诊病历(复诊)a51d64b0-b07e-4c0a-8757-f3ad3aebce93.html"
]


def manual_check(server):
    '''
    测试流程
    按文件依次模拟点击
    需要在https://sites.google.com/chromium.org/driver/下载驱动
    :return:
    '''
    datas = pd.read_excel('template_disease_map.xlsx', sheet_name='Sheet1', engine='openpyxl', dtype=str)
    browser = webdriver.Chrome()
    browser.set_window_position(**{'x': -1255, 'y': -2135})
    browser.set_window_size(**{'width': 1200, 'height': 2000})
    time.sleep(1)
    browser2 = webdriver.Chrome()
    browser2.set_window_position(**{'x': -54, 'y': -2135})
    browser2.set_window_size(**{'width': 1200, 'height': 2000})
    time.sleep(1)

    for line in datas.itertuples():
        type_ = line.type_  # 初诊、复诊
        disease_id = line.disease_id_eg
        disease_code = line.disease_code_eg
        disease_name = line.disease_name_eg
        depart_code = line.depart_code
        file_name = line.file_name

        if file_name not in check_files:
            continue

        if type_ == '初诊':
            _type = 'INITIAL'
        elif type_ == '复诊':
            _type = 'SUBSEQUENT'
        else:
            _type = 'MEDICINE'

        with open('aiwizard.html', 'r') as f:
            html = f.read()
        html = re.sub('deptCode: "(\d+)"', 'deptCode: "{}"'.format(depart_code), html)
        html = re.sub('tplType: "(.+)"', 'tplType: "{}"'.format(_type), html)
        html = re.sub('"name": "(.+)"', '"name": "{}"'.format(disease_name), html)
        html = re.sub('"code": "(.+)"', '"code": "{}"'.format(disease_code), html)
        html = re.sub('"id": "(.+)"', '"id": "{}"'.format(disease_id), html)
        html = re.sub('height="(\d+)px"', 'height="{}px"'.format(1200), html)
        html = re.sub(
            'src="http.*',
            'src="http://{}/?type=iframe&visitId=707010491&orgCode=00000002&patientId=1646184620231"'.format(server),
            html)
        with open('aiwizard.html', 'w') as f:
            f.write(html)

        # 对比
        browser.get('file:///' + os.path.abspath('aiwizard.html'))
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/div[1]/button[1]').click()
        time.sleep(2)
        browser2.get('file:///' + os.path.abspath(file_name))
        time.sleep(2)

        # 等待人工校验
        next_ = input('直接输入回车继续，否则任意键退出：')
        if next_ != '':
            break

    browser.close()
    browser2.close()


if __name__ == '__main__':
    server = '172.18.0.76:8116'
    manual_check(server)
