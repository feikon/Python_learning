# !/usr/bin/env python3
# encoding: utf-8


"""
@version: 0.1
@author: feikon
@license: Apache Licence 
@contact: crossfirestarer@gmail.com
@site: https://github.com/feikon
@software: PyCharm
@file: problem_0004.py
@time: 2017/6/12 16:05
"""

# Problem describe:Count the number of words in a text file
# Problem solve step:
# 1.Open and read the file;
# 2.Built a dic to store the word and the count of this word;
# Notice: word

import logging

"""
Test File:night_watch
Night gathers, and now my watch begins. 
It shall not end until my death. 
I shall take no wife, hold no lands, father no children. 
I shall wear no crowns and win no glory. 
I shall live and die at my post. 
I am the sword in the darkness. 
I am the watcher on the walls. 
I am the fire that burns against the cold, 
the light that wakes the sleepers, 
the shield that guards the realms of men. 
I pledge my life and honor to the Night's Watch, for this night, and all the nights to come.
"""


def words_content(file):
    content = list()
    try:
        with open(file) as f:
            lines = f.readlines()        # return every row content and combine a list
            for line in lines:
                words = line.lower().replace('\n', '').replace(',', '').replace('.', '').split(' ')
                for word in words:
                    content.append(word)
        return content
    except IOError as e:
        logging.log(level=IOError, msg=e)


if __name__ == '__main__':
    file_content = words_content('D:/night_watch.txt')
    # fixme:去掉''出现的次数,如何去掉重复输出，比如i出现几次，后面还会出现
    for file_word in file_content:
        print('{} appear {} times.'.format(file_word.ljust(10), file_content.count(file_word)).rjust(4))




