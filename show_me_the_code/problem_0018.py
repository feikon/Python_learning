# !/usr/bin/env python3
# encoding: utf-8


"""
@version: 0.1
@author: feikon
@license: Apache Licence 
@contact: crossfirestarer@gmail.com
@site: https://github.com/feikon
@software: PyCharm
@file: problem_0018.py
@time: 2017/6/19 9:50
"""

# Problem describe:Convert city.xlsx  file to city.xml
# Problem solve step:
# 1.Read the city.xlsx;
# 2.Write to city.xml;

import xlrd
import codecs
from lxml import etree
from collections import OrderedDict


def read_xlsx(xlsx_file):
    data = xlrd.open_workbook(xlsx_file)
    table = data.sheets()[0]
    c = OrderedDict()
    for i in range(table.nrows):
        c[table.cell(i, 0).value] = table.row_values(i)[1:]
    return c


def save_xml(data, xml_file):
    output = codecs.open(xml_file, 'w', 'utf-8')
    root = etree.Element('root')
    city_xml = etree.ElementTree(root)
    city = etree.SubElement(root, 'city')
    city.append(etree.Comment('城市信息'))
    city.text = str(data)
    output.write(etree.tounicode(city_xml.getroot()))
    output.close()

if __name__ == '__main__':
    xlsx_data = read_xlsx('D:/show_me/txt/city.xlsx')
    save_xml(xlsx_data, 'D:/show_me/txt/city.xml')

