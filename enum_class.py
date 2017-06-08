# !/usr/bin/env python
# encoding: utf-8


"""
@version: 0.1
@author: feikon
@license: Apache Licence 
@contact: crossfirestarer@gmail.com
@site: https://github.com/feikon
@software: PyCharm
@file: enum_class.py
@time: 2017/6/8 14:39
"""


from enum import Enum, unique

# Enum建立的时候，第一个是要枚举的东西，比如月，第一个tuple为枚举项
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# for name, member in Month.__members__.items():
#     print(name, '=>', member, ',', member.value)    # value属性则是自动赋给成员的int常量，默认从1开始计数。


# 如果需要控制枚举，用Enum类进行派生
@unique                  # @unique装饰器可以帮助我们检查保证没有重复值
class Weekday(Enum):
    Sun = 0              # 此时Sun的值被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Weekday.Mon
print(day1)
print(day1.value)


