#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/3 0003 17:03
# @Author  : HelloWorld
# @File    : tencent_news_data.py
import requests
from bs4 import BeautifulSoup


class SpiderText(object):
    @staticmethod
    def get_html(url):
        headers = {
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'zh-CN,zh;q=0.9',
                    'connection': 'keep-alive',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
                   }
        response = requests.get(url, headers=headers)
        html_text = ''
        if response.status_code == 200:
            html_text = response.text

        return html_text

    @staticmethod
    def get_target_text(text):
        soup = BeautifulSoup(text, 'lxml')
        text1 = soup.find_all('div', class_='detail')
        for i in text1:
            print(i.a.text)

        # return title_list + content_list


url = 'https://new.qq.com/rolls/?ext=sports&day=20191203'
s = SpiderText()
t = s.get_html(url)
print(t)
print('-----------')
print(s.get_target_text(t))