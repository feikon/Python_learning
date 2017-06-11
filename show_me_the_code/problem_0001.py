# !/usr/bin/env python3
# encoding: utf-8


"""
@version: 0.1
@author: feikon
@license: Apache Licence 
@contact: crossfirestarer@gmail.com
@site: https://github.com/feikon
@software: PyCharm
@file: problem_0001.py
@time: 2017/6/11 10:14
"""

# Problem describe:generate active code
# Problem solve step:
# 1.Generate random;
# 2.Cannot same(use dict erase the same one);


import random
import string


def generate_active_code(code_length, code_numbers=200):
    result = {}
    # Done: append #$%^... to character_pole (have any simple method to add #%^&*?)
    character_pole = list(string.ascii_uppercase)       # append A-Z to pole
    other_character = ['!', '@', '#', '$', '%', '^', '&', '*']
    for ch in other_character:
        character_pole.append(ch)
    for num in range(0, 10):
        character_pole.append(str(num))                 # append 0-9 to pole
    while len(result) < code_numbers:
        key = ''
        for i in range(code_length):
            key += random.choice(character_pole)
        if key in result:
            pass
        else:
            result[key] = 1
    for key in result:
        print(key)

if __name__ == '__main__':
    # generate_active_code(10, 10)
    generate_active_code(16)

