# !/usr/bin/env python
# encoding: utf-8


"""
@version: 0.1
@author: feikon
@license: Apache Licence 
@contact: crossfirestarer@gmail.com
@site: https://github.com/feikon
@software: PyCharm
@file: inherit_poly.py
@time: 2017/6/7 8:51
"""


class Animal(object):
    @staticmethod
    def run(self):            # 没有使用到self，pycharm会提示你用静态方法，加@staticmethod前缀,self非必须使用
        print('Animal is running...')


class Dog(Animal):
    @staticmethod
    def run(self):
        print('Dog is running...')


class Cat(Animal):
    @staticmethod
    def run(self):              # 子类的run()覆盖了父类的run(),实现多态
        print('cat is running...')


dog = Dog()
cat = Cat()
print(dog.run(1))               # 输出：Dog is running...
print(cat.run(0))               # 输出：cat is running...

