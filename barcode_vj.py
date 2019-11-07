# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import barcode
import random

def barcode_generator():
    num = random.randrange(1,10000000000000000000)
    print(num)
    image = barcode.get_barcode_class('ean13')
    image_bar = image(u'{}' .format(num))
    file = open('annajoen:\\vj1.svg', "wb")
    image_bar.writer(file)
    return "Barcode Generated Successfully!"
