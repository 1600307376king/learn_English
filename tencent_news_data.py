#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/3 0003 17:03
# @Author  : HelloWorld
# @File    : tencent_news_data.py
import requests
from save_mongo import Mongo
import json
from bs4 import BeautifulSoup
from selenium import webdriver
import datetime
import time
import random
import matplotlib.pyplot as plt
from PIL import Image
import collections
import wordcloud
import numpy as np
import jieba


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
        # soup = BeautifulSoup(text, 'lxml')
        # text1 = soup.find_all('div', class_='detail')
        # for i in text1:
        #     print(i.a.text)
        pass

        # return title_list + content_list


# url = 'https://pacaio.match.qq.com/openapi/json?key=sports:20191204&num=15&page=0&expIds=&callback=__jp1'
# browser = webdriver.Chrome()
# browser.get(url)
#
# s = SpiderText()
# print(s.get_target_text(browser.page_source))
# browser.close()
s = SpiderText()
m = Mongo('tencent_news', 'title_data')


def save_title(url):
    try:
        text = s.get_html(url)
        article_list = eval(text.lstrip('__jp1(').rstrip(')'))['data']
        title_list = [{'title': i['title']} for i in article_list]
        m.insert_data(title_list)
        print('save_success')
    except:
        print('error')


def fetch_data():
    category_parameter = ['sports', 'ent', 'sport_nba', 'finance', 'fashion', 'tech']
    now_date = datetime.datetime.now()
    date_list = [''.join((now_date - datetime.timedelta(days=i)).strftime('%Y-%m-%d').split('-')) for i in range(14)]

    for i in category_parameter:
        for j in date_list:
            url = 'https://pacaio.match.qq.com/openapi/json?key={}:{}&num=15&page=0&expIds=&callback=__jp1'.format(i, j)
            save_title(url)
            time.sleep(1)


all_title_list = m.search_data('title')
all_title_str = ','.join([i['title'] for i in all_title_list])
res = jieba.lcut(all_title_str, cut_all=True)
print(res)
print(type(res))
# wc = wordcloud.WordCloud(max_font_size=66).generate(res)
# plt.imshow(wc)  # 显示词云
# plt.axis('off')  # 关闭坐标轴
# plt.show()  # 显示图像

