# !/usr/bin/env python3
# encoding: utf-8


"""
@version: 0.1
@author: feikon
@license: Apache Licence 
@contact: crossfirestarer@gmail.com
@site: https://github.com/feikon
@software: PyCharm
@file: problem_0003.py
@time: 2017/6/12 15:26
"""

# Problem describe:generate active code to redis
# Problem solve step:
# 1.Connect to redis;
# 2.Insert generate code;

import string
import random
import redis

KEY_LEN = 20
KEY_ALL = 200


def base_str():
    # print(string.ascii_uppercase)       # A-Z
    # print(string.ascii_letters)         # A-Z a-z
    # print(string.digits)                # 0-9
    return string.ascii_uppercase + string.digits


def key_gen():
    keylist = [random.choice(base_str()) for i in range(KEY_LEN)]
    return "".join(keylist)


def key_num(num, result=None):
    if result is None:
        result = []
    for i in range(num):
        result.append(key_gen())
    return result


def redis_init():
    r = redis.Redis(host='localhost', port=6379, db=0)
    return r


def push_to_redis(key_list):
    for key in key_list:
        redis_init().lpush('key', key)


def get_from_redis():
    key_list = redis_init().lrange('key', 0, -1)
    for key in key_list:
        print(key)

if __name__ == "__main__":
    push_to_redis(key_num(200))
    get_from_redis(0)



