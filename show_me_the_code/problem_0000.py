# !/usr/bin/env python3
# encoding: utf-8


"""
@version: 0.1
@author: feikon
@license: Apache Licence 
@contact: crossfirestarer@gmail.com
@site: https://github.com/feikon
@software: PyCharm
@file: problem_0000.py
@time: 2017/6/10 9:39
"""

# Problem describe:add number to top right of a image
# Problem solve step:
# 1.Use PIL load image(in this file PIL version is 4.1.1);
# 2.Use PIL method operate the image(number font,color and so on);
# 3.Save the processed image


from PIL import Image, ImageDraw, ImageFont
import logging


def add_num_to_image(image, number=44):
    try:
        with Image.open(image) as img:
            width, height = img.size
            # TODO:Adjust position and
            draw_position_width = 0.8 * width
            draw_position_height = 0.08 * height
            draw_font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf')
            draw = ImageDraw.Draw(img)
            draw.text((draw_position_width, draw_position_height), str(number), fill=(255, 33, 33), font=draw_font)
            img_save_name = image.split('.')[0] + '_processed.jpg'
            img.save(img_save_name, 'JPEG')
            img.show(img_save_name)
    except IOError as e:
        logging.exception(e)


def show_image_info(image):
    try:
        with Image.open(image) as img:
            print(img.format, img.size, img.mode)
    except IOError as e:
        # print(e, 'IOerror')       # 不会显示所有错误的地方，会继续运行
        logging.exception(e)        # 不仅显示所有的错误信息，并且会继续执行, 不用try...except的话，程序不会继续执行
    finally:
        print('finally...')


if __name__ == '__main__':
    add_num_to_image('D:/wechat.jpg', 99)





