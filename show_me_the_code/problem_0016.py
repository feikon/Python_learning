# !/usr/bin/env python3
# encoding: utf-8


"""
@version: 0.1
@author: feikon
@license: Apache Licence 
@contact: crossfirestarer@gmail.com
@site: https://github.com/feikon
@software: PyCharm
@file: problem_0016.py
@time: 2017/6/19 9:01
"""

# Problem describe:Convert number txt file to xls
# Problem solve step:
# 1.Read the txt;
# 2.Write to xlsx;

import xlsxwriter
import logging
import json


def txt_to_xls(txt_file):
    workbook = xlsxwriter.Workbook('D:/show_me/txt/numbers.xlsx')
    worksheet = workbook.add_worksheet()
    try:
        with open(txt_file, 'r', encoding='utf-8') as f:
            lines = f.read()
            json_txt = json.loads(lines)
            for x in range(len(json_txt)):
                for y in range(len(json_txt[x])):
                    worksheet.write(x, y, json_txt[x][y])
    except IOError as e:
        logging.log(level=40, msg=e)

if __name__ == '__main__':
    txt_to_xls('D:/show_me/txt/numbers.txt')




