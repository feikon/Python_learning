# !/usr/bin/env python3
# encoding: utf-8


"""
@version: 0.1
@author: feikon
@license: Apache Licence 
@contact: crossfirestarer@gmail.com
@site: https://github.com/feikon
@software: PyCharm
@file: problem_0012.py
@time: 2017/6/16 10:53
"""

# Problem describe:replace filtered words
# Problem solve step:
# 1.Open the filtered_word.txt;
# 2.Find all the filter word;
# 3.Replace filter word by *

import logging


def replace_filtered_words_by_asterisk(filtered_file):
    filtered_words = list()
    try:
        with open(filtered_file, 'r', encoding='utf-8') as f:       # handle encode issue
            lines = f.readlines()
            for line in lines:
                filtered_words.append(line.rstrip('\n'))
    except IOError as e:
        logging.log(level=40, msg=e)
    print('filtered_words is {0}'.format(filtered_words))
    if filtered_words:
        while True:
            user_input = input('Please input your word:')
            if user_input == 'exit':
                break
            else:
                pass
            for filtered_word in filtered_words:
                if filtered_word in user_input:
                    user_input = user_input.replace(filtered_word, '*'*len(filtered_word))
                    print(user_input)

    else:
        logging.warning(msg='No filtered words')


if __name__ == '__main__':
    replace_filtered_words_by_asterisk('D:/show_me/filtered/filtered_words.txt')


