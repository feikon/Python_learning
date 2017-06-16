# !/usr/bin/env python3
# encoding: utf-8


"""
@version: 0.1
@author: feikon
@license: Apache Licence 
@contact: crossfirestarer@gmail.com
@site: https://github.com/feikon
@software: PyCharm
@file: problem_0010.py
@time: 2017/6/15 16:36
"""

# Problem describe:Generate a picture code
# Problem solve step:
# 1.Open a file;
# 2.Generete 4 letter in it;

import string
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter


# generate 4 bit code
def generate_code():
    num = ''.join(random.sample(string.ascii_letters + '0123456789', 4))
    print(num)
    return num


def random_col():
    return random.randint(50, 200)


def verification_code(generated_code, width=400, height=200):
    im = Image.new('RGB', (width, height), (255, 255, 255))              # 400*200 blank white canvas
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype('verdana.ttf', width // 4)
    font_width, font_height = font.getsize(generated_code)
    generated_code_len = len(generated_code)
    x = (width - font_width) // 2
    y = (height - font_height) // 2
    total_dex = 0
    for i in generated_code:
        draw.text((x, y), i, random_col(), font)
        temp = random.randint(-30, 30)
        total_dex += temp
        im = im.rotate(temp)
        draw = ImageDraw.Draw(im)
        x += font_width / generated_code_len                              # generated_code translation to next str
    im = im.rotate(-total_dex)
    draw = ImageDraw.Draw(im)
    # add 3 random lines in canvas
    draw.line(
        [(random.randint(0, width // 4),
          random.randint(0, height // 4)
          ),
         (random.randint(width // 4 * 3, width),
          random.randint(height // 4 * 3, height)
          )],
        fill=random_col(),
        width=width // 80
    )
    draw.line(
        [(random.randint(0, width // 4),
          random.randint(height // 4 * 3, height)
          ),
         (random.randint(width // 3 * 2, width),
          random.randint(0, height // 3)
          )],
        fill=random_col(),
        width=width // 80
    )
    draw.line(
        [(random.randint(width // 4 * 3, width),
          random.randint(height // 4 * 3, height)
          ),
         (random.randint(width // 3 * 2, width),
          random.randint(0, height // 3)
          )],
        fill=random_col(),
        width=width // 80
    )
    # generate points in the canvas
    for x in range(width):
        for y in range(height):
            col = im.getpixel((x, y))
            if col == (255, 255, 255) or col == (0, 0, 0):
                draw.point((x, y), fill=random_col())
    im = im.filter(ImageFilter.FIND_EDGES)                      # add picture filter
    im.save('D:/verification_code.jpg')


if __name__ == '__main__':
    generated_code = generate_code()
    verification_code(generated_code)






