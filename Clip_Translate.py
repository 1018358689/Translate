#!/usr/bin/env python
# -*- coding:utf-8 -*-

# import requests
import win32con
import win32clipboard as clip
from GT import G_Translate
from colorama import Fore, init
from PIL import ImageGrab
# from PIL import Image
from io import BytesIO
from aip import AipOcr
import re

init(autoreset=True)

APP_ID = '10693105'
API_KEY = 'uL9tgRmnNy5cOvqwvO4vqdze'
SECRET_KEY = 'PI2nSH8vsFOutC2e0Qx2vzKfrTWAlWMm'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def get_clip():
    im = ImageGrab.grabclipboard()
    if im:
        s = BytesIO()
        im.save(s, format='bmp')
        # img = Image.open(s)
        # ocr_word = pytesseract.image_to_string(img, lang='chi_sim')
        # print(ocr_word)
        ocr_word = client.basicGeneral(s.getvalue())
        ocr_word = ' '.join([i['words'] for i in ocr_word['words_result']])
        return ocr_word
    else:
        clip.OpenClipboard()
        clip_text = clip.GetClipboardData(win32con.CF_TEXT)
        clip.CloseClipboard()
        return clip_text.decode('gbk')


def word_convert(word):
    re_str = re.sub('\W', ' ', word)  # 将所有非字符变成空格（除了下划线）（包括空格）
    re_str = ' '.join(re_str.split())  # 将连续空格变成一个空格
    return re_str.replace('_', ' ').replace('\n', ' ').replace('\r','')


if __name__ == '__main__':
    count = 0
    while 1:
        count += 1
        start = input('{}.回车识别剪贴板 ->'.format(count))
        w = len(start) and start or get_clip()
        w = word_convert(w)
        cb = G_Translate()
        result = cb.Translate_it(w)
        print('\n输入：'+ w)
        print('\n输出：'+ Fore.LIGHTGREEN_EX + result + Fore.RESET)
        print('\n**********************\n')
