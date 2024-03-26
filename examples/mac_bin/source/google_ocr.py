#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by chenhao2020-07-19 23:36:34
# https://github.com/tesseract-ocr/tesseract

import os, sys

file=sys.argv[1]

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(filename))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text

print(ocr_core(file))
