#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests

Key = '8D839B7337F3B8ED6AB6E68CF8DDE827'
Type = 'json'
raw_url = 'http://dict-co.iciba.com/api/dictionary.php'


class CB_Translate():
    def __init__(self, Key, Type, raw_url):
        self.Key = Key
        self.Type = Type
        self.raw_url = raw_url

    def Translate_it(self, word):
        json_content = self.__get_json_content(word)
        code = self.__Get_code(json_content)
        if code == 'is_English':
            ph, means = self.__E2C(json_content)
            self.__Print_it(ph, means)
        elif code == 'is_Chinese':
            ph, means = self.__C2E(json_content)
            self.__Print_it(ph, means)
        else:
            print('未查到该词')

    def __get_json_content(self, word):
        res = requests.get(url=self.raw_url, params={'w': word, 'type': self.Type, 'key': self.Key})
        json_content = res.json()
        # pprint(json_content)
        return json_content

    def __E2C(self, json_content):
        symbol = json_content['symbols'][0]
        ph = [symbol['ph_am'], symbol['ph_en']]
        ph = [i for i in ph if len(i) != 0]
        means = symbol['parts']
        means = ['[{0}]{1}'.format(i['part'], ','.join(i['means'])) for i in means]
        return ph, means

    def __C2E(self, json_content):
        symbol = json_content['symbols'][0]
        ph = symbol['word_symbol']
        ph = ph.split('@@')
        means = symbol['parts'][0]['means']
        means = [i['word_mean'] for i in means]
        return ph, means

    def __Print_it(self, ph, means):
        if len(ph) != 0:
            print('发音：{}\n'.format(' , '.join(ph)))
        print('翻译：{}'.format('\n     '.join(means)))

    def __Get_code(self, json_content):
        if 'word_name' in json_content.keys():
            if 'exchange' in json_content.keys():
                return 'is_English'
            else:
                return 'is_Chinese'
        else:
            return '404'


if __name__ == '__main__':
    while 1:
        w = input('输入你要查的词语：')
        print('')
        cb = CB_Translate(Key, Type, raw_url)
        cb.Translate_it(w)
        print('\n**********************\n')
