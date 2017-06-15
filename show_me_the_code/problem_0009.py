# !/usr/bin/env python3
# encoding: utf-8


"""
@version: 0.1
@author: feikon
@license: Apache Licence 
@contact: crossfirestarer@gmail.com
@site: https://github.com/feikon
@software: PyCharm
@file: problem_0009.py
@time: 2017/6/15 16:19
"""

# Problem describe:Prase a html then find link
# Problem solve step:
# 1.Praser html;
# 2.Print link;

from bs4 import BeautifulSoup
import requests


def print_link(url):
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'lxml')
    print(soup.prettify())
    for link in soup.find_all('a'):
        print(link.get('href'))


if __name__ == '__main__':
    print_link('http://www.jianshu.com/p/4ad744ed955c')


