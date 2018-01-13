# -*- coding: utf - 8  -*-

from PIL import Image
im = Image.open('2.jpg')
print(im.format, im.size, im.mode)
# PNG (400, 300) RGB
im.thumbnail((200, 100))
im.save('/Users/yoyo/Desktop/one.png', 'PNG')
