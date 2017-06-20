# !/usr/bin/env python3
# encoding: utf-8


"""
@version: 0.1
@author: feikon
@license: Apache Licence 
@contact: crossfirestarer@gmail.com
@site: https://github.com/feikon
@software: PyCharm
@file: problem——0020.py
@time: 2017/6/19 14:29
"""

# Problem describe:Count telephone fare
# Problem solve step:
# 1.Read the fare.xlsx;
# 2.Analyse it;

import xlrd
import datetime


def fare_analyse(fare_xls):
    infos = []
    info_file = xlrd.open_workbook(fare_xls)
    info_table = info_file.sheets()[0]
    row_count = info_table.nrows
    for row in range(7, row_count):
        time_string = info_table.cell(row, 4).value
        time_s_sp = time_string.split(':')
        infos.append(
            {
                'type': info_table.cell(row, 2).value,
                'number': info_table.cell(row, 3).value,
                'timespan': datetime.timedelta(
                    seconds=int(time_s_sp[2]),
                    minutes=int(time_s_sp[1]),
                    hours=int(time_s_sp[0])),
                'class': info_table.cell(row, 5).value
            }
        )

    time_all = datetime.timedelta(seconds=0)
    time_types = {}
    time_classes = {}
    time_numbers = {}
    for infor in infos:
        time_all += infor['timespan']

        infor_type = infor['type']
        if infor_type in time_types:
            time_types[infor_type] += infor['timespan']
        else:
            time_types[infor_type] = infor['timespan']

        infor_class = infor['class']
        if infor_class in time_classes:
            time_classes[infor_class] += infor['timespan']
        else:
            time_classes[infor_class] = infor['timespan']

        infor_number = infor['number']
        if infor_number in time_numbers:
            time_numbers[infor_number] += infor['timespan']
        else:
            time_numbers[infor_number] = infor['timespan']

    print('总通话时间：%s' % time_all)
    print('通信方式分类：')
    for (k, v) in time_types.items():
        print(k.encode('utf-8'), v)
    print('通信类型分类：')
    for (k, v) in time_classes.items():
        print(k.encode('utf-8'), v)
    print('对方号码分类：')
    for (k, v) in time_numbers.items():
        print(k.ljust(20), v)

if __name__ == '__main__':
    fare_analyse('D:/show_me/test/fare.xls')

