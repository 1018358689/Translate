#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import win32con
import win32clipboard as clip
from GT import G_Translate
from colorama import Fore, init
from PIL import ImageGrab, Image
from aip import AipOcr
from io import BytesIO
import pytesseract
import re

init(autoreset=True)
APP_ID = '10693105'
API_KEY = 'uL9tgRmnNy5cOvqwvO4vqdze'
SECRET_KEY = 'PI2nSH8vsFOutC2e0Qx2vzKfrTWAlWMm'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


def getFile(filePath):
    with open(filePath, 'rb') as file:
        content = file.read()
        return content


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
        re_str = re.sub('\W', ' ', ocr_word)  # 将所有非字符变成空格（除了下划线）（包括空格）
        re_str = ' '.join(re_str.split())  # 将连续空格变成一个空格
        print(re_str)
    else:
        clip.OpenClipboard()
        clip_text = clip.GetClipboardData(win32con.CF_TEXT)
        clip.CloseClipboard()
        return clip_text.decode('gbk')


get_clip()
