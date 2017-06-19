# !/usr/bin/env python3
# encoding: utf-8


"""
@version: 0.1
@author: feikon
@license: Apache Licence 
@contact: crossfirestarer@gmail.com
@site: https://github.com/feikon
@software: PyCharm
@file: problem_0017.py
@time: 2017/6/19 9:12
"""

# Problem describe:Convert student.xlsx  file to student.xml
# Problem solve step:
# 1.Read the student.xlsx;
# 2.Write to student.xml;

import xlrd
import codecs
from lxml import etree
from collections import OrderedDict


def read_xlsx(filename):
    data = xlrd.open_workbook(filename)
    table = data.sheets()[0]
    c = OrderedDict()
    for i in range(table.nrows):
        c[table.cell(i, 0).value] = table.row_values(i)[1:]
    return c


def save_xml(xml_file, data):
    output = codecs.open(xml_file, 'w', 'utf-8')
    root = etree.Element('root')
    student_xml = etree.ElementTree(root)
    student = etree.SubElement(root, 'student')
    student.append(etree.Comment('学生信息表\n\"id\": [名字，数学，语文，英语]'))
    student.text = str(data)
    output.write(etree.tounicode(student_xml.getroot()))
    output.close()

if __name__ == '__main__':
    xlsx_file_data = read_xlsx('D:/show_me/txt/student.xlsx')
    save_xml('D:/show_me/txt/student.xml', xlsx_file_data)




