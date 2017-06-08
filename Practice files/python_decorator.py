# !/usr/bin/env python
# encoding: utf-8

import functools

"""
@version: 0.1
@author: feikon
@license: Apache Licence 
@contact: crossfirestarer@gmail.com
@site: https://github.com/feikon
@software: PyCharm
@file: python_decorator.py
@time: 2017/6/6 16:21
"""


# decorator 第一种情况，不需要传入参数,直接进行操作进行
def log(func):
    def wraper():
        print('call %s:' % func.__name__)
        return func()
    return wraper


@log
def now():
    print('2017-6-6')

print(now())
print(now.__name__)     # 输入wraper，非now，函数签名有问题需要再次装饰
print('\n')


# decorator 第二种情况，对decorator传入参数，这里参数为text
# 只有调用的函数需要加括弧，比如func(),代表now(),而其他的装饰器东西不需要加括号，如：wraper,decorator
# 注意函数的返回层级，先返回要装饰的函数，然后一层一层向上推 func()-->wraper-->decorator
# 传入的参数可以看作装饰器对参数又加一层装饰
def arg_log(text):
    def decorator(func):
        def wraper():
            print('%s call begin %s:' % (text, func.__name__))
            return func()
        return wraper
    return decorator


@arg_log('Execute')
def now2():
    print('2017-6-7')

print(now2())
print(now2.__name__)                # 输出wraper，而不是真正的函数名now2，函数签名有问题，需要再次装饰


# 解决函数签名问题方案：引入functools中的functools.wraps
def log(func):
    @functools.wraps(func)          # 加入functools中的函数包装
    def wraper():
        print('call %s:' % func.__name__)
        return func()
    return wraper


@log
def now():
    print('2017-6-6')

print(now())
print(now.__name__)                 # 输入now，函数签名问题解决
print('\n')


def arg_log(text):
    def decorator(func):
        @functools.wraps(func)      # 需要装饰那个函数，就把它放在要装饰的下面
        def wraper():
            print('%s call begin %s:' % (text, func.__name__))
            return func()
        return wraper
    return decorator


@arg_log('Execute')
def now2():
    print('2017-6-7')

print(now2())
print(now2.__name__)                # 输出now2，函数签名问题解决
