#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/2 0002 9:20
# @Author  : HelloWorld
# @File    : get_word.py

import requests
from bs4 import BeautifulSoup
from save_mongo import Mongo


class SpiderText(object):
    @staticmethod
    def get_html(url):
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/76.0.3809.100 Safari/537.36'}
        response = requests.get(url, headers=headers)
        html_text = ''
        if response.status_code == 200:
            html_text = response.text

        return html_text

    @staticmethod
    def get_target_text(text):
        soup = BeautifulSoup(text, 'lxml')
        text1 = soup.find_all('div', class_='section')
        s2 = BeautifulSoup(str(text1[0]), 'lxml')
        text2 = s2.find_all(name='h2')
        text3 = s2.find_all(name='p')
        title_list = []
        content_list = []
        for title_name in text2:
            title_list.append({'fetch_data': title_name.text})

        for content in text3:
            content_list.append({'fetch_data': content.text})

        return title_list + content_list


# local_url = 'https://scikit-learn.org/stable/modules/linear_model.html'
# txt = get_html(local_url)
# list_txt = get_target_text(txt)
# client_connection(list_txt)
