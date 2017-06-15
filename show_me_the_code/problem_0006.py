# !/usr/bin/env python3
# encoding: utf-8


"""
@version: 0.1
@author: feikon
@license: Apache Licence 
@contact: crossfirestarer@gmail.com
@site: https://github.com/feikon
@software: PyCharm
@file: problem_0006.py
@time: 2017/6/14 15:42
"""

# Problem describe:count the key words
# Problem solve step:
# 1.Find all of txt file in a folder;
# 2.Open file and if word appear >5  difine it as key word;
# 3.print it;


import os
from os.path import join
import logging


def words_content(file):
    content = list()
    key_words = set()
    try:
        with open(file) as f:
            lines = f.readlines()        # return every row content and combine a list
            for line in lines:
                words = line.lower().replace('\n', '').replace(',', '').replace('.', '').split(' ')
                for word in words:
                    content.append(word)
    except IOError as e:
        logging.log(level=IOError, msg=e)
    for file_word in content:
        if content.count(file_word) > 5 and file_word != '':
            key_words.add(file_word)
    print('{} key words are {}'.format(file, key_words))
    return key_words


def walk_path(path):
    file_list = list()
    for root, dirs, files in os.walk(path):
        for name in files:
            filename = join(root, name)
            if filename.split('.')[1] == 'txt':
                file_list.append(filename)
    return file_list


def print_key_word(files):
    for file in files:
        words_content(file)

if __name__ == '__main__':
    dairy_flies = walk_path('D:/dairy')
    print_key_word(dairy_flies)
