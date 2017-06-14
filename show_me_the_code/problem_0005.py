# !/usr/bin/env python3
# encoding: utf-8


"""
@version: 0.1
@author: feikon
@license: Apache Licence 
@contact: crossfirestarer@gmail.com
@site: https://github.com/feikon
@software: PyCharm
@file: problem_0005.py
@time: 2017/6/12 19:54
"""

# Problem describe:format picture pixal
# Problem solve step:
# 1.Find all of pictures in a folder;
# 2.Fiter pictures who large 1136p×640p;
# 3.Handle them;

from PIL import Image
import os
from os.path import join


def change_size(path):
    for root, dirs, files in os.walk(path):
        for name in files:
            filename = join(root, name)
            # 解决非jpg和png格式图片乱入问题，还可以加其他图片类型
            if filename.split('.')[1] == 'jpg' or filename.split('.')[1] == 'png':
                print(filename)
                change_size_operation(filename)


def change_size_operation(filename):
    iphone5_size = (1136, 640)                    # [0]width  [1]height
    with Image.open(filename) as im:
        picture_height = im.height
        picture_width = im.width
        # TODO: 如何按比例进行调整,从而不让
        if picture_width > iphone5_size[0]:
            im = im.resize((iphone5_size[0], picture_height))         # ajust heigth
        else:
            pass
        if picture_height > iphone5_size[1]:
            im = im.resize((im.width, iphone5_size[1]))               # ajust width
        else:
            pass
        im.save(filename.split('.')[0] + '_changed.jpg')


if __name__ == '__main__':
    change_size('D:/test')













