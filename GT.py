#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from pprint import pprint
from colorama import Fore, init

init(autoreset=True)


class G_Translate():
    __url = 'http://translate.google.cn/translate_a/single'
    __headers = {'User-Agent': 'iOSTranslate'}

    def Translate_it(self, word):
        if self.__check_contain_chinese(word):
            data = {
                'dt': 't',
                'q': word,
                'tl': 'en',
                'ie': 'utf-8',
                'sl': 'auto',
                'client': 'ia',
                'dj': '1'
            }
        else:
            data = {
                'dt': 't',
                'q': word,
                'tl': 'zh-CN',
                'ie': 'utf-8',
                'sl': 'auto',
                'client': 'ia',
                'dj': '1'
            }
        res = requests.post(url=self.__url, headers=self.__headers, data=data)
        # pprint(res.json())
        json_content = res.json()
        trans = json_content['sentences'][0]['trans']
        # self.__Print_it(trans)
        return trans

    def __check_contain_chinese(self, check_str):
        for i in check_str:
            if ord(i) > 127:
                return True
        return False

    # def __Print_it(self, trans):
    #     print('输出：' + Fore.LIGHTGREEN_EX + trans + Fore.RESET)

if __name__ == '__main__':
    count = 0
    while 1:
        count += 1
        w = input('{}.输入：'.format(count))
        print('')
        cb = G_Translate()
        result = cb.Translate_it(w)
        print('{}.输出：'.format(count) + Fore.LIGHTGREEN_EX + result + Fore.RESET)
        print('\n**********************\n')
