# !/usr/bin/env python3
# encoding: utf-8


"""
@version: 0.1
@author: feikon
@license: Apache Licence 
@contact: crossfirestarer@gmail.com
@site: https://github.com/feikon
@software: PyCharm
@file: problem_0014.py
@time: 2017/6/16 17:09
"""

# Problem describe:Convert txt file to xls
# Problem solve step:
# 1.Read the txt;
# 2.Write to xlsx;

import xlsxwriter
import logging
import json


def txt_to_xls(txt_file):
    workbook = xlsxwriter.Workbook('D:/show_me/txt/student.xlsx')
    worksheet = workbook.add_worksheet()
    try:
        with open(txt_file, 'r', encoding='utf-8') as f:
            lines = f.read()
            json_txt = json.loads(lines)
            for x in range(len(json_txt)):
                worksheet.write(x, 0, x + 1)
                for y in range(len(json_txt[str(x + 1)])):
                    worksheet.write(x, y + 1, json_txt[str(x + 1)][y])
    except IOError as e:
        logging.log(level=40, msg=e)

if __name__ == '__main__':
    txt_to_xls('D:/show_me/txt/student.txt')


