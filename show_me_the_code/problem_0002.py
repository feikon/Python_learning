# !/usr/bin/env python3
# encoding: utf-8


"""
@version: 0.1
@author: feikon
@license: Apache Licence 
@contact: crossfirestarer@gmail.com
@site: https://github.com/feikon
@software: PyCharm
@file: problem_0002.py
@time: 2017/6/11 15:24
"""

# Problem describe:generate active code to mysql
# Problem solve step:
# 1.Connect to mysql;
# 2.Insert generate code;


import pymysql.cursors
import pymysql
import uuid


def generate_activation_code(num):
    code_list = []
    for i in range(num):
        code = str(uuid.uuid4()).replace('-', '').upper()
        while code in code_list:
            code = str(uuid.uuid4()).replace('-', '').upper()
        code_list.append(code)

    return code_list


def store_in_mysql(code_list):
    try:
        conn = pymysql.connect(host='127.0.0.1', user='root', passwd='518518', db='mysql')
        cur = conn.cursor()
    except BaseException as e:
        print(e)
    else:
        try:
            cur.execute('CREATE DATABASE IF NOT EXISTS activation_code')
            cur.execute('USE activation_code')
            cur.execute('''CREATE TABLE IF NOT EXISTS code(
                            id INT NOT NULL AUTO_INCREMENT,
                            code VARCHAR(32) NOT NULL,
                            PRIMARY KEY(id)
                        )''')
            for code in code_list:
                print(code)
                cur.execute('INSERT INTO code(code) VALUES({})'.format(code))
                cur.connection.commit()
        except BaseException as e:
            print(e)
    finally:
        cur.close()
        conn.close()

if __name__ == '__main__':
    store_in_mysql(generate_activation_code(200))
    print('OK!')

