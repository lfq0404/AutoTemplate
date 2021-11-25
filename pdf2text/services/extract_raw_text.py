#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/22 16:40
# @File    : extract_raw_text.py
# @Software: Basebit
# @Description:
import os
import re
import pdf2text.constant as cons


def main():
    result = {}
    result_file = 'result.text'
    g = os.walk('{}/bookTexts'.format(cons.BASE_PATH))

    for path, _, file_list in g:
        for file in file_list:
            if '西医_内科' not in file:
                continue
            result[file] = {}

            with open('{}/{}'.format(path, file)) as f:
                for line in f.readlines():
                    no_space_line = re.sub('\s', '', line)
                    if no_space_line in cons.TITLES:
                        now_title = no_space_line
                        result[file][now_title] = {}
                    else:
                        pass




if __name__ == '__main__':
    main()
