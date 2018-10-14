# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 11:55:43 2018

@author: ASUS
"""
from PIL import Image
import PIL

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]


img=Image.open("C:\\Users\\ASUS\\Desktop\\1.jpg")

width,height=img.size
with open("C:\\Users\\ASUS\\Desktop\\1.txt","w") as f:
    for x in range(height):
        for y in range(width):
            pixel =img.getpixel((y,x))
            f.write(get_char(pixel[0],pixel[1],pixel[2]))