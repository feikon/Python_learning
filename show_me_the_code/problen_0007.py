# !/usr/bin/env python3
# encoding: utf-8


"""
@version: 0.1
@author: feikon
@license: Apache Licence 
@contact: crossfirestarer@gmail.com
@site: https://github.com/feikon
@software: PyCharm
@file: problen_0007.py
@time: 2017/6/15 9:19
"""

# Problem describe:count code lines,inlude comment and blank lines
# Problem solve step:
# 1.Open and read the file;
# 2.count all the lines, count begin with #(comment),count blank lines;

import logging
import os
from os.path import join
import re


def lines_count(file):
    count_lines = 1
    count_comment_lines = 0
    count_blank_lines = 0
    try:
        with open(file) as f:
            lines = f.readlines()        # return every row content and combine a list
            for line in lines:
                count_lines += 1
                # fixme:re表达式的匹配
                if re.match(r'^#', line) is None:
                    pass
                else:
                    count_comment_lines += 1
                if line[0] == '\n':
                    count_blank_lines += 1
                else:
                    pass
    except IOError as e:
        logging.log(level=IOError, msg=e)
    print('{} file lines are {},comment lines are {},blank lines are {}'
          .format(file, count_lines, count_comment_lines, count_blank_lines))


def walk_path(path):
    file_list = list()
    for root, dirs, files in os.walk(path):
        for name in files:
            filename = join(root, name)
            if filename.split('.')[1] == 'py':
                file_list.append(filename)
    return file_list


if __name__ == '__main__':
    code_files = walk_path('D:/show_me/code_files')
    for code_file in code_files:
        lines_count(code_file)
