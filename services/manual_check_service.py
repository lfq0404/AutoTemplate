#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/30 15:10
# @File    : manul_check_service.py
# @Software: Basebit
# @Description:
import json
import os
import re
import pandas as pd
import numpy as np

import constant as cons
import config as conf
from myUtils import read_excel, get_check_file_datas


class ManualCheck:
    def __init__(self, excel_result_for_check_path, extract_template_files, standard_file_path):
        """
        :param excel_result_for_check_path: 前一步生成check_templates.xlsx的路径
        :param extract_template_files: 需要解析的文件名，传空则所有
        :param standard_file_path: 已经人工校验过的模板文件
        """
        self.excel_result_for_check_path = excel_result_for_check_path
        self.extract_template_files = extract_template_files
        self.standard_file_path = standard_file_path

    def check_recent_segments(self):
        """
        人工校验可能有问题的segment，并修改到Excel中
        :return:
        """
        update_segments = {}
        temp_repeat_labels = {}
        need_update = False
        not_care_labels = ['delete']

        datas = read_excel(self.excel_result_for_check_path, cons.SHEET_NAME)
        for num, line in enumerate(datas.itertuples()):
            num += 1
            # 如果没有模板信息，则不管
            raw_content = line._4
            if pd.isna(raw_content) or type(raw_content) is not str or '{' not in raw_content:
                continue
            # 只提取需要的文件
            if self.extract_template_files and line._1 not in self.extract_template_files:
                continue

            raw_label = line._3
            update_label = '' if pd.isna(line._8) else line._8
            update_content = '' if pd.isna(line._9) else line._9

            update_segments[raw_content] = {
                'raw_label': raw_label,
                'update_label': update_label,
                'update_content': update_content,
            }

            label = update_label or raw_label
            content = (update_content or raw_content).replace('\n', '').replace(' ', '')
            temp_repeat_labels.setdefault(label, [])
            for lines, v in temp_repeat_labels[label]:
                if content == v:
                    lines.append(num)
                    break
            else:
                temp_repeat_labels[label].append([[num], content])

        # 人工判读功能，与控制台交互
        for label, contents in temp_repeat_labels.items():
            if label in not_care_labels:
                continue
            if len(contents) > 1:
                need_update = True
                # {'[1, 3, 4]': content}
                line_infos = {}
                print('label = "{}"还存在多个segment：'.format(label))
                for i in contents:
                    lines, c = i
                    lines_text = json.dumps(lines)
                    line_infos[lines_text] = c
                    print(lines_text, c)
                print('------------------')
                update = False

                # 将所有的以right_lines为准
                right_lines = input('请输入正确的行号们（没有请直接回车）：')
                if right_lines:
                    for lines_text, _ in line_infos.items():
                        if lines_text == right_lines:
                            continue
                        for n in json.loads(lines_text):
                            datas.loc[n - 1][8] = line_infos[right_lines]
                    print('label = "{}"合并成功1'.format(label))
                    update = True

                # 将所有的以输入的为准
                if not update:
                    right_content = input('请输入正确的内容（没有请直接回车）：')
                    if right_content:
                        for lines_text in line_infos:
                            for n in json.loads(lines_text):
                                datas.loc[n - 1][8] = right_content
                        print('label = "{}"合并成功2'.format(label))
                        update = True

                # 手动指定内容
                if not update:
                    while True:
                        lines_text = input('请输入需要修改的行号们（没有请直接回车）：')
                        if not lines_text:
                            break
                        right_label = input('请输入正确的label：')
                        right_content = input('请输入正确的content：')
                        # if right_label or right_content:
                        for n in json.loads(lines_text):
                            if right_content:
                                datas.loc[n - 1][8] = right_content
                                update = True
                            if right_label:
                                datas.loc[n - 1][7] = right_label
                                update = True

                if update:
                    datas.to_excel(self.excel_result_for_check_path, sheet_name=cons.SHEET_NAME, index=False,
                                   header=False)
                else:
                    not_care_labels.append(label)

        not_care_labels.remove('delete')
        print('\n需要人工处理的labels：{}'.format(not_care_labels))
        if need_update:
            raise ValueError('请再次检查check_excel中的label与segment')

        return update_segments

    def _dataframe_insert(self, df, i, df_add):
        # 指定第i行插入一行数据
        df1 = df.iloc[:i, :]
        df2 = df.iloc[i:, :]
        df_new = pd.concat([df1, df_add, df2], ignore_index=True)
        return df_new

    def _update_standard(self, standard_datas, query, new_datas):
        """
        更新标准数据
        :param query:
        :return:
        """
        standard_query = pd.Series([True for _ in range(len(standard_datas))])
        new_query = pd.Series([True for _ in range(len(new_datas))])
        for i in query:
            standard_query = standard_query & (standard_datas[i[0]] == i[1])
            new_query = new_query & (new_datas[i[0]] == i[1])

        # 整行替换
        index = standard_datas.loc[standard_query].index[0]
        standard_datas = standard_datas.drop(standard_datas[standard_query].index)
        standard_datas = self._dataframe_insert(standard_datas, index, new_datas.loc[new_query, [0, 1, 2, 3, 4, 5, 6]])
        return standard_datas

    def contrast_segments(self):
        """
        对比最新数据与人工判读后的准确数据做对比，如果不一致，则需要人工介入
        :return:
        """

        if not os.path.exists(self.standard_file_path):
            # 如果不存在，则人工校验后，创建文件
            self._manual_check_package()
            datas = get_check_file_datas(self.excel_result_for_check_path)
            datas[[0, 1, 2, 3, 4, 5, 6]].to_excel(self.standard_file_path, sheet_name=cons.SHEET_NAME,
                                                  index=False,
                                                  header=False)
        else:
            is_pass = True
            # 如果存在，则需要对比新生成的文件与标准数据的区别
            new_datas = get_check_file_datas(self.excel_result_for_check_path)
            standard_datas = read_excel(self.standard_file_path, cons.SHEET_NAME)

            # 先根据new_label修改template_content
            checked_file_name = ''
            for _, line in enumerate(new_datas.itertuples()):
                file_name = line._1
                label = line._3
                if not re.search('\d+-.+', file_name):
                    continue
                if pd.isna(label):
                    continue
                template_display = line._2
                segment_content = line._4
                category_text = line._7
                # 1、判断每个类型下的display是否一样
                if checked_file_name != file_name:
                    checked_file_name = file_name
                    standard_display = standard_datas.loc[
                        (standard_datas[0] == file_name)
                        & (standard_datas[6] == category_text)].iloc[0][1]
                    if standard_display != template_display:
                        is_pass = False
                        print('文件《{}》还需要检查'.format(file_name))
                        print('1、最新的display：{}'.format(template_display))
                        print('2、标准的display：{}'.format(standard_display))
                        text = input('若要用最新数据更新标准数据，请输入1：')
                        if text == '1':
                            standard_datas = self._update_standard(
                                standard_datas,
                                query=[
                                    [0, file_name],
                                    [6, category_text],
                                ],
                                new_datas=new_datas)

                # 2、检查label对应的content是否一样
                try:
                    standard_content = standard_datas.loc[
                        (standard_datas[0] == file_name)
                        & (standard_datas[6] == category_text)
                        & (standard_datas[2] == label)
                        ].iloc[0][3]
                    if standard_content != segment_content:
                        is_pass = False
                        print('文件《{}》的 {} 还需要检查'.format(file_name, label))
                        print('1、最新的content：{}'.format(segment_content))
                        print('2、标准的content：{}'.format(standard_content))
                        text = input('若要用最新数据更新标准数据，请输入1：')
                        if text == '1':
                            standard_datas = self._update_standard(
                                standard_datas,
                                query=[
                                    [0, file_name],
                                    [6, category_text],
                                    [2, label],
                                ],
                                new_datas=new_datas)
                except IndexError:
                    is_pass = False
                    print('文件《{}》的 {} 还需要检查，出现了新label'.format(file_name, label))
                    text = input('若要用最新数据更新标准数据，请输入1：')
                    if text == '1':
                        standard_datas = self._update_standard(
                            standard_datas,
                            query=[
                                [0, file_name],
                                [6, category_text]
                            ],
                            new_datas=new_datas)

            standard_datas.to_excel(self.standard_file_path, sheet_name=cons.SHEET_NAME, index=False,
                                    header=False)
            if not is_pass:
                raise ValueError('请修改后重新执行')

    def _manual_check_package(self):
        """
        人工对最终的package进行校验
        只要不报错即可
        :return:
        """
        sign = None
        for file in self.extract_template_files:
            # print('file:///Users/jeremy.li/Basebit/Documents/develop/smart/20211013-瑞金门急诊模板配置/rawTemplates/{}'.format(file))
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
            print('打开医院提供的原始HTML与aiwizard.html，对比效果')
            sign = input('如果没有问题，请直接回车；如果有问题，请输入任意字符，并修改代码逻辑')

        if sign:
            # 表示之前的结果解析有问题，需要重新跑数据
            raise ValueError('解析结果有问题，修改解析规则后，请重新跑main.py')


def _bug_check(file):
    """
    用于处理bug的临时代码，与解析无关
    :return:
    """
    print('file:///Users/jeremy.li/Basebit/Documents/develop/smart/20211013-瑞金门急诊模板配置/rawTemplates/{}'.format(file))
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
    print('打开医院提供的原始HTML与aiwizard.html，对比效果')
    print()


if __name__ == '__main__':
    file = '4350100-营养门诊-营养门诊病历(复诊)-门诊病历(复诊).html'
    _bug_check(file)
