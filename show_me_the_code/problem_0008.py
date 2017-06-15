# !/usr/bin/env python3
# encoding: utf-8


"""
@version: 0.1
@author: feikon
@license: Apache Licence 
@contact: crossfirestarer@gmail.com
@site: https://github.com/feikon
@software: PyCharm
@file: problem_0008.py
@time: 2017/6/15 10:26
"""

# Problem describe:Praser a html then find content
# Problem solve step:
# 1.Praser html;
# 2.Print content;

from bs4 import BeautifulSoup
import requests


def print_main_body(url):
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'lxml')
    print(soup.body.get_text())

if __name__ == '__main__':
    print_main_body('http://www.jianshu.com/p/4ad744ed955c')

