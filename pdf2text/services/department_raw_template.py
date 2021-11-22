#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/19 10:29
# @File    : department_raw_template.py
# @Software: Basebit
# @Description: 根据科室分类，获取原始的文本
import json
import os
import re

import pdf2text.constant as cons


def get_all_ocr_files():
    """
    获取所有OCR的结果文件
    :return:
    """
    g = os.walk('{}/bookJsons'.format(cons.BASE_PATH))

    # 获取OCR出来的所有文件
    # 由于walk出来的无序，需要先排序
    json_files_path = []
    for path, _, file_list in g:
        for file in file_list:
            if '.json' not in file:
                continue
            json_files_path.append('{}/{}'.format(path, file))
    json_files_path = sorted(json_files_path)

    return json_files_path


def extract_lines_with_department(json_files_path):
    """
    按顺序遍历json_files_path，根据科室合并成独立文件，并按行输出
    :param json_files_path: 已经排过序的filepath
    :return: list(根据科室命名的文件们)
    """
    page = []
    for json_file_path in json_files_path:
        print('处理文件：{}'.format(json_file_path))
        with open(json_file_path, 'r') as f:
            data = f.read()
        data = json.loads(data)
        page_lines = get_page_lines(data['prism_wordsInfo'])
        # 如果是
        for page_line in page_lines:
            if not filter_valid_line(page_line):
                continue
            department = re.findall('^(.+科.*)入院记录$', page_line.replace(' ', ''))
            if department:
                # 如果是新的科室，则记录之前的科室内容
                if page:
                    with open('{}/bookTexts/{}'.format(cons.BASE_PATH, file_name), 'w') as f:
                        for i in page:
                            f.write(i + '\n')

                page_num = int(re.findall('(\d+)\.json', json_file_path)[0])
                for r, _type in cons.VALID_PAGES.items():
                    if page_num in r:
                        break
                file_name = '{}_{}.txt'.format(_type, department[0])
                page = []
            elif page_line:
                page.append(page_line)
    else:
        if page:
            with open('{}/bookTexts/{}'.format(cons.BASE_PATH, file_name), 'w') as f:
                for i in page:
                    f.write(i + '\n')


def filter_valid_line(page_line):
    """
    筛选有效的行
    eg：“附：各专科入院记录书写格式” 则需要删除
    :param page_line:
    :return:
    """
    page_line = page_line.replace(' ', '')
    for patt in [
        '^附[:：]',
        '、.+科入院记录书写格式',
        '^医院$',
        '^姓名：科别：床号：住院号：病区：$',
        '^姓名：职业：$',
        '^姓名：职业：$',
        '^性别：工作单位：$',
        '^年龄：住址：$',
        '^婚姻：供史者：可靠程度：$',
        '^出生地：入院时间：$',
        '^军$',
        '^分$',
        '^民族：记录时间：时分$',
    ]:
        if re.search(patt, page_line):
            return False

    return True


def get_page_lines(words) -> list:
    """
    获取每页的信息
    :param words: 包含position信息的文本
    :return:[第一行文本, 第二行文本, ...]
    """
    lines = []
    line = ''
    last_y = 0  # 上一堆话的y坐标
    last_x = None  # 上一个词的x坐标

    for word in words:
        # 切边，剔除不需要的部分
        if not word_check_valid(word['pos']):
            print('该文本不满足正文范围，剔除 --> {}'.format(word['word']))
            continue

        # print('成功', word['word'])
        # 以左下角的坐标判断是否为一行
        bottom_left_pos = word['pos'][-1]
        if not (last_y - cons.Y_ALLOW_FLOAT_PIXEL <= bottom_left_pos['y'] <= last_y + cons.Y_ALLOW_FLOAT_PIXEL):
            # 如果y方向差距太大，表示一行已经结束
            lines.append(line)
            last_y = bottom_left_pos['y']
            last_x = None
            line = ''

        # 在同一个word中，肯定在同一行，不用判断y
        for char in word['charInfo']:
            # 计算空格的个数
            if last_x:
                line += ' ' * int((char['x'] - last_x) // cons.SPACE_MIN_PIXEL)
            else:
                line += ' ' * int((char['x'] - cons.LEFT_MIN_PIXEL) // cons.SPACE_MIN_PIXEL)
            line += char['word']
            last_x = char['x']
    else:
        if line:
            lines.append(line)

    return lines


def word_check_valid(word_pos):
    """
    判断文本是否是正文（剔除书本边缘的文本）
    :param word_pos:  [{"x":269,"y":725},{"x":1758,"y":728},{"x":1755,"y":1407},{"x":222,"y":1404}]
    :return:
    """
    if word_pos[0]['x'] < cons.LEFT_MIN_PIXEL:
        print('与最左边的距离太小，忽略')
        return False
    if word_pos[0]['y'] < cons.TOP_MIN_PIXEL:
        print('与最上面的距离太小，忽略')
        return False
    if word_pos[2]['y'] > cons.BOTTOM_MAX_PIXEL:
        print('与下面的距离太小，忽略')
        return False
    if word_pos[2]['x'] > cons.RIGHT_MAX_PIXEL:
        print('与右边的距离太小，忽略')
        return False

    return True

    # 文本左上角的坐标，需要大于最小值
    # 文本右下角的坐标，需要小于最高值
    # return word_pos[0]['x'] >= cons.LEFT_MIN_PIXEL \
    #        and word_pos[0]['y'] >= cons.TOP_MIN_PIXEL \
    #        and word_pos[2]['x'] <= cons.BOTTOM_MAX_PIXEL \
    #        and word_pos[2]['y'] <= cons.RIGHT_MAX_PIXEL


if __name__ == '__main__':
    json_files_path = get_all_ocr_files()
    extract_lines_with_department(json_files_path)
