#!/usr/bin/python

import os
from PIL import Image


def compress_image(file, type=None):
    filepath = os.path.join(os.getcwd(), file)
    # filepath = os.path.join("/var/www/nginx/jockey/jockey_website/public/img/", file)
    if type == 'png':
        picture = Image.open(filepath)

        if picture.mode =='RGBA':
            # print('Es: RGBA')
            picture = picture.convert('RGBA', palette=Image.WEB)
            picture.save("/var/www/nginx/jockey_web/jockey_website/images/" + file, compress_level=7, bits=8)
        if picture.mode == 'P':
            # print('Es: P')
            picture = picture.convert('RGBA').convert('P', palette=Image.ADAPTIVE)
            picture.save("/var/www/nginx/jockey_web/jockey_website/images/" + file, compress_level=7, bits=8)


    else:
        picture = Image.open(filepath).convert('RGB')
        picture.save("/var/www/nginx/jockey_web/jockey_website/images/" + file,
                      "png", optimize=True, quality=75)


def main():
    # finds present working dir
    pwd = os.getcwd()
    #pwd = "/var/www/Jockey/jockey_website/public/img/"
    num = 0

    for file in os.listdir(pwd):
        if os.path.splitext(file)[1].lower() in ('.jpg', '.jpeg',):
            num += 1
            compress_image(file)
        if os.path.splitext(file)[1].lower() in ('.png',):
            num += 1
            compress_image(file, 'png')
    print "Done"


if __name__ == "__main__":
    main()
