#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/6 11:14
# @File    : manual_template.py
# @Software: Basebit
# @Description:
import json


def radio_add_text(radio, text_keys):
    """
    选项中添加text
    :param radio:{
  "label": "诱因下出现部位发绀",
  "type": "RADIO",
  "value": [
    "0"
  ],
  "options": [
    {
      "label": "无",
      "display": "无诱因下出现部位发绀",
      "props": {
        "color": "green"
      },
      "value": "0",
      "addition": null
    },
    {
      "label": "有",
      "display": "有诱因下出现部位发绀",
      "props": {
        "color": "red"
      },
      "value": "1",
      "addition": null
    }
  ]
}
    :param text_keys: ['部位']
    :return:
    """
    radio = json.loads(radio)
    addtion = [{"label": text_key, "type": "TEXT", "value": "", "freetextPrefix": "", "freetextPostfix": "",
                "placeholder": text_key} for text_key in text_keys]
    for option in radio['options']:
        update = False
        for text_key in text_keys:
            if text_key in option['display']:
                update = True
                option['display'] = option['display'].replace(text_key, '{{{}}}'.format(text_key))
        if update:
            option['addition'] = addtion

    print(json.dumps(radio, ensure_ascii=False))


def orange2green(radio):
    """
    将非阴阳的选项改为阴阳选项
    :param radio:
    :return:
    """
    radio = json.loads(radio)
    radio['value'] = ['0']
    for ind, i in enumerate(radio['options']):
        i['value'] = str(ind)
        i['props']['color'] = 'green' if ind == 0 else 'red'

    print(json.dumps(radio, ensure_ascii=False))


if __name__ == '__main__':
    radio = """
    {"label": "前囟", "type": "RADIO", "value": ["1"], "options": [{"label": "平坦", "display": "前囟平坦", "props": {"color": "orange"}, "value": "1", "addition": null}, {"label": "隆起", "display": "前囟隆起", "props": {"color": "orange"}, "value": "2", "addition": null}, {"label": "凹陷", "display": "前囟凹陷", "props": {"color": "orange"}, "value": "3", "addition": null}]}
    """
    orange2green(radio)
    # radio_add_text(
    #     '{"label": "病理反射", "type": "RADIO", "value": ["0"], "options": [{"label": "无", "display": "无病理反射", "props": {"color": "green"}, "value": "0", "addition": null}, {"label": "有", "display": "有病理反射，部位、性质", "props": {"color": "red"}, "value": "1", "addition": null}]}',
    #     ['部位','性质']
    # )
