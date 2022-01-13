#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/31 09:47
# @File    : depart_statistics.py
# @Software: Basebit
# @Description:
import pandas as pd


def main():
    raw_datas = pd.read_excel('../660_templates_disease_map.xlsx', sheet_name='Sheet1', engine='openpyxl', dtype=str)
    raw_datas = raw_datas.fillna('')
    datas = raw_datas[['depart_code', 'depart_name']].drop_duplicates()
    datas = datas.sort_values(by=['depart_code'])
    datas[['depart_num', 'undeal_num', 'file_eg']] = ''
    for ind, line in datas.iterrows():
        depart_num = len(raw_datas.loc[(raw_datas['depart_code'] == line.depart_code)])
        undeal_num = len(raw_datas.loc[(raw_datas['depart_code'] == line.depart_code) & (raw_datas['batch'] == '')])
        datas.loc[ind, 'depart_num'] = depart_num
        datas.loc[ind, 'undeal_num'] = undeal_num
        datas.loc[ind, 'file_eg'] = raw_datas.loc[raw_datas['depart_code']==line.depart_code, 'file_name'].iloc[0]

    datas.to_excel('depart_statistics.xlsx')


if __name__ == '__main__':
    main()
