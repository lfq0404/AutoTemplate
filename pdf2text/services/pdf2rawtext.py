#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/18 16:13
# @File    : pdf2rawtext.py
# @Software: Basebit
# @Description:

import base64
import json
import os
import fitz
import requests
import pdf2text.constant as cons


def pdf2image(pdf_path, img_path, page_ranges, *, zoom_x=5, zoom_y=5, rotation_angle=0):
    """
    将PDF转化为图片
    :param pdf_path: pdf文件的路径
    :param img_path: 图像要保存的文件夹
    :param page_ranges: 需要处理的页码
    :param zoom_x: x方向的缩放系数。zoom_x和zoom_y一般取相同值，值越大，图像分辨率越高
    :param zoom_y: y方向的缩放系数
    :param rotation_angle: 旋转角度
    :return:
    """
    # 打开PDF文件
    pdf = fitz.open(pdf_path)
    # 逐页读取PDF
    for page_range in page_ranges:
        for pg in page_range:
            page = pdf[pg]
            page_num = str(pg + 1)

            # 如果已经存在，则continue
            img_file = img_path + page_num + ".png"
            if os.path.exists(img_file):
                continue

            # 设置缩放和旋转系数
            trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotation_angle)
            pm = page.getPixmap(matrix=trans, alpha=False)
            # 开始写图像
            pm.writePNG(img_file)
            print('处理完成', page_num)
    pdf.close()


def image2text():
    """
    图片转为纯文本
    文档地址：https://market.aliyun.com/products/57124001/cmapi028554.html
    :return:
    """
    url = 'https://gjbsb.market.alicloudapi.com/ocrservice/advanced'
    AppCode = "1fc0cf3c0cfb48d5b2662e6ce686bad9"
    headers = {
        'Authorization': 'APPCODE ' + AppCode,
        'Content-Type': 'application/json; charset=UTF-8'
    }
    g = os.walk('{}/bookImgs'.format(cons.BASE_PATH))

    for path, _, file_list in g:
        for file in file_list:
            if 'png' not in file:
                continue
            img_path = '{}/{}'.format(path, file)
            text_path = '{}/bookJsons/{}.json'.format(cons.BASE_PATH, file).replace('.png', '')

            # 如果已经识别过的，则continue
            if os.path.exists(text_path):
                continue

            with open(img_path, 'rb') as f:  # 以二进制读取本地图片
                data = f.read()
                encodestr = str(base64.b64encode(data), 'utf-8')
            # params = json.dumps({'img': encodestr}).encode(encoding='UTF8')
            params = {
                # 图像数据：base64编码，要求base64编码后大小不超过4M，最短边至少15px，最长边最大4096px，支持jpg/png/bmp格式
                'img': encodestr,
                # 是否需要单字识别功能
                'charInfo': True,
                # 是否需要表格识别功能
                'table': True,
                # 是否需要图案检测功能
                'figure': True,
                # 是否需要成行返回功能
                'row': True,
            }
            try:
                response = requests.post(url, json=params, headers=headers, timeout=60)
            except:
                continue
            if response.json().get('error_code'):
                print('{}识别失败'.format(text_path))
                continue

            print('成功 - {}'.format(text_path))
            with open(text_path, 'w') as f:
                f.write(response.text)


def main():
    # 将PDF转为高清图片
    pdf2image(
        '{}/pdf2text/病历书写规范.pdf'.format(cons.BASE_PATH),
        '{}/pdf2text/bookImgs/'.format(cons.BASE_PATH),
        list(cons.VALID_PAGES)
    )

    # 将图片转为文本
    image2text()


if __name__ == '__main__':
    pass
    main()
