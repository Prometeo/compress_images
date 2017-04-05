#!/usr/bin/python

import os
from PIL import Image


img = Image.open("/home/prometeo/Python/resize_images/dados.png")
img = img.convert('RGBA').convert('P', palette=Image.ADAPTIVE)
img.save("/home/prometeo/Python/resize_images/dados-1.png", compress_level=9, bits=8)
