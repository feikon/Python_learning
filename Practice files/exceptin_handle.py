# !/usr/bin/env python
# encoding: utf-8


"""
@version: 0.1
@author: feikon
@license: Apache Licence 
@contact: crossfirestarer@gmail.com
@site: https://github.com/feikon
@software: PyCharm
@file: exceptin_handle.py
@time: 2017/6/8 21:20
"""

import logging


try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:                        # finally有就一定会执行
    print('finally...')
print('END')


# case1:记录错误:不仅显示所有的错误信息，并且会继续执行
def foo1(s):
    return 10/int(s)


def bar1(s):
    return foo1(s) * 2


def main1():
    try:
        bar1('0')
    except Exception as e:
        logging.exception(e)
main1()
print('GO ON 1')


# case2:对比记录错误:不会显示所有错误的地方，会继续运行
def foo2(s):
    return 10/int(s)


def bar2(s):
    return foo2(s) * 2


def main2():
    try:
        bar2('0')
    except ZeroDivisionError as e:
        print('ZeroDivisionError:', e)
main2()
print('GO ON 2')


# 对比3：不会继续运行，显示所有错误的地方
def foo3(s):
    return 10/int(s)


def bar3(s):
    return foo3(s)*2


def main3():
        bar3('0')
main3()
print('GO ON 3')


# rasie
def foo4(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n


def bar4():
    try:
        foo4('0')
    except ValueError as e:
        print('ValueError!')
        raise                   # raise语句如果不带参数，就会把当前错误原样抛出

bar4()
print('GO ON 4')
# 结论：
# 会继续运行的是有错误返回的，如except ZeroDivisionError..
# 显示所有错误的：
# 1.运用Loggging
# 2.不做错误处理

