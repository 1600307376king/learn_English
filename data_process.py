#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/2 0002 11:35
# @Author  : HelloWorld
# @File    : data_process.py


from save_mongo import Mongo
import matplotlib.pyplot as plt
from PIL import Image
import collections
import wordcloud
import numpy as np
import jieba


init_data_obj = Mongo(db_name='skitlearning_site_data', table_name='words')
res = init_data_obj.search_data('fetch_data')
all_words = ''
for i in res:
    all_words += i['fetch_data']

all_words_list = jieba.cut(all_words, cut_all=False)

remove_words = [u'the', u'and', u'a', u'of', u'can', u'as', u'an', u'that', u'from']

obj_list = []

for w in all_words_list:
    if w not in remove_words:
        obj_list.append(w)

word_counts = collections.Counter(obj_list)
word_counts_top10 = word_counts.most_common(10)

mask = np.array(Image.open('./heart.jpg'))
wc = wordcloud.WordCloud(
    font_path='C:/Windows/Fonts/simhei.ttf',  # 设置字体格式
    mask=mask,  # 设置背景图
    max_words=200,  # 最多显示词数
    max_font_size=100  # 字体最大值
)

wc.generate_from_frequencies(word_counts)  # 从字典生成词云
image_colors = wordcloud.ImageColorGenerator(mask)  # 从背景图建立颜色方案
wc.recolor(color_func=image_colors)  # 将词云颜色设置为背景图方案
plt.imshow(wc)  # 显示词云
plt.axis('off')  # 关闭坐标轴
plt.show()  # 显示图像
