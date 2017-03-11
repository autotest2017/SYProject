#!/usr/bin/env python
#encoding:utf-8

from PIL import ImageGrab


def get_screen_shot(image_name):
    shot = ImageGrab.grab()
    shot.save('./screen_shot/%s.jpg' % image_name)

if __name__=='__main__':
    get_screen_shot('test')