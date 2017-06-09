# !/usr/bin/env python
# encoding: utf-8


"""
@version: 0.1
@author: feikon
@license: Apache Licence 
@contact: crossfirestarer@gmail.com
@site: https://github.com/feikon
@software: PyCharm
@file: Dict_unittest.py
@time: 2017/6/9 9:02
"""


class Dict(dict):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError as e:
            print(e, 'keyerror')
            raise AttributeError(r"'Dict' object has no attribute {}".format(key))

    def __setattr__(self, key, value):
        self[key] = value
