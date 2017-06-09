# !/usr/bin/env python3
# encoding: utf-8


"""
@version: 0.1
@author: feikon
@license: Apache Licence 
@contact: crossfirestarer@gmail.com
@site: https://github.com/feikon
@software: PyCharm
@file: module_common.py
@time: 2017/6/9 16:45
"""

from datetime import datetime, timedelta, timezone      # 时间模块
from collections import namedtuple                      # 集合模块
from collections import deque                           # deque 双向列表
from collections import defaultdict                     # dict key不存在时，返回一个默认值，就可以用defaultdict
from collections import OrderedDict                     # 保持dict中Key的顺序，可以用OrderedDict
from collections import Counter                         # 计数
import base64                                           # base64编码
import struct                                           # 处理字节
import hashlib                                          # 摘要算法
import itertools                                        # 操作迭代对象

now = datetime.now()                            # 获取当前时间，now方法
print(now)                                      # 输出：2017-06-09 16:46:53.502087
print(now.strftime('%a, %b %d %H:%M'))          # 输出：Fri, Jun 09 17:01 格式化字符串
print(now + timedelta(days=1, hours=12))        # 输出：2017-06-11 05:03:37.383608 timedelta进行时间加减

set_time = datetime(2016, 6, 6, 6, 6)           # 设定指定时间
print(set_time)                                 # 输出：2016-06-06 06:06:00

timestamp = set_time.timestamp()                # 时间戳 相对1970-1-1 00:00:00 UTC+0:00
print(timestamp)                                # 输出：1465164360.0 小数点后为毫秒

t_timestamp = 1465164360.0
t_datetime = datetime.fromtimestamp(t_timestamp)  # timestamp 转换为datetime 本地时间
print(t_datetime)                                # 输出：2016-06-06 06:06:00
t_utc_datetime = datetime.utcfromtimestamp(t_timestamp)  # timestamp 转换为utc datetime utc时间
print(t_utc_datetime)                            # 输出：2016-06-05 22:06:00 可以用于时区转换

# 时区转换相关
# 拿到UTC时间，并强制设置时区为UTC+0:00:
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print('utc_dt is {}'.format(utc_dt))

# astimezone()将转换时区为北京时间:
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print('bj_dt is {}'.format(bj_dt))

# astimezone()将转换时区为东京时间:
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print('tokyo_dt is {}'.format(tokyo_dt))

# astimezone()将bj_dt转换时区为东京时间:
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print('tokyo_dt2 is {}'.format(tokyo_dt2))
# 上述输出：
# utc_dt is 2017-06-09 09:09:19.497633+00:00
# bj_dt is 2017-06-09 17:09:19.497633+08:00
# tokyo_dt is 2017-06-09 18:09:19.497633+09:00
# tokyo_dt2 is 2017-06-09 18:09:19.497633+09:00

# ------collections module namedtuple--------
Point = namedtuple('Point', ['x', 'y'])         # 可以把namedtuple看作为一个类,因为Point大写
point = Point(1, 2)
print('point position is ({},{})'.format(point.x, point.y))
print(isinstance(point, tuple))

# namedtuple('名称', [属性list])
Circle = namedtuple('Circle', ['x', 'y', 'r'])
circle = Circle(1, 1, 2)
print(circle)

# ------collections module deque--------
# 双向列表，能实现高效插入和删除，list线性，插入删除慢
q = deque(['a', 'b', 'c'])
q.append('d')               # 正常插入
q.appendleft('o')           # 左侧插入
print(q)                                        # 输出：deque(['o', 'a', 'b', 'c', 'd'])
q.pop()                     # 删除
print(q)
q.popleft()                 # 左侧删除
print(q)

# ------collections module defaultdict--------
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。
# 如果希望key不存在时，返回一个默认值，就可以用defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])               # 输出：abc
print(dd['key2'])               # 返回默认值N/A

# ------collections module OrderedDict--------
# 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序
# 如果要保持Key的顺序，可以用OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)                        # 为毛测试时有序的……
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)

# ------collections module Counter--------
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)                    # Counter({'r': 2, 'g': 2, 'm': 2, 'p': 1, 'o': 1, 'a': 1, 'i': 1, 'n': 1})

# ------base64--------
s = base64.b64encode('在Python中使用BASE 64编码'.encode('utf-8'))
print(s)
d = base64.b64decode(s).decode('utf-8')
print(d)
s = base64.urlsafe_b64encode('在Python中使用BASE 64编码'.encode('utf-8'))
print(s)
d = base64.urlsafe_b64decode(s).decode('utf-8')
print(d)

# -------struct 处理字节---------
# struct.unpack(格式, 要处理的字节)
print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))    # 输出：(4042322160, 32896)

# ------hashlib 摘要算法---------
# 应用在设置密码等功能上，输入的密码的hash和数据库中hash比对
# 加盐 the-Salt提高存储密码的难以破解度
# 摘要算法又称哈希算法、散列算法。它通过一个函数，
# 把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。
md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())      # 输出：d26a53750bc40b38b65a520292f69306

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())     # 输出：2c76b57293ce30acef38d98f6046927161b46a44

# ----itertools 迭代对象操作-------
# 常用方法 count(),cycle(),repeat(),chain(),groupby()
for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print(key, list(group))

