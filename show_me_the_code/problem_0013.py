# !/usr/bin/env python3
# encoding: utf-8


"""
@version: 0.1
@author: feikon
@license: Apache Licence 
@contact: crossfirestarer@gmail.com
@site: https://github.com/feikon
@software: PyCharm
@file: problem_0013.py
@time: 2017/6/16 15:21
"""

# Problem describe:Download pictures
# Problem solve step:
# 1.Open the filtered_word.txt;
# 2.Find all the filter word;
# 3.Replace filter word by *

import requests
from bs4 import BeautifulSoup
import os
import logging


def download_pictures(url, save_path):
    # os.mkdir(save_path)
    os.chdir(save_path)
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'lxml')
    # print(soup.prettify())
    imgs = soup.find_all('img')     # #post_content_29397251028 > img:nth-child(1)
    picture_name = 0
    for img in imgs:
        picture_name += 1
        print(img.get('src'))
        img_url = img.get('src')
        ir = requests.get(img_url, timeout=2)
        # fixme: download failed, timeout
        if ir.status_code == '200':
            with open(str(picture_name)+'.jpg', 'wb') as f:
                f.write(ir.content)
        else:
            logging.error(msg='Timeout')


if __name__ == '__main__':
    download_pictures('http://tieba.baidu.com/p/2166231880', 'D:/show_me/download')

