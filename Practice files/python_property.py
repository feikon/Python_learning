# !/usr/bin/env python3
# encoding: utf-8


"""
@version: 0.1
@author: feikon
@license: Apache Licence 
@contact: crossfirestarer@gmail.com
@site: https://github.com/feikon
@software: PyCharm
@file: python_property.py
@time: 2017/6/7 19:46
"""


class Student(object):

    # It's generally considered a good practice to
    # explicitly define/declare all your attributes in the __init__ function
    def __init__(self):
        self._score = None      # 对于后面要用的可以先设置为None

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError("score must be an integer")
        if value < 0 or value > 100:
            raise ValueError("score must be 0~100")
        self._score = value

if __name__ == '__main__':
    s = Student()
    s.score = 10
    print(s.score)
    s.score = 101
    print(s.score)

