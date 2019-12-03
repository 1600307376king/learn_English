#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/2 0002 10:00
# @Author  : HelloWorld
# @File    : save_mongo.py


import pymongo


class Mongo(object):
    def __init__(self, db_name, table_name):
        self.client = pymongo.MongoClient('mongodb://localhost:27017/')
        self.my_db = self.client[db_name]  # create db
        self.words = self.my_db[table_name]  # create table

    def insert_data(self, data):
        self.words.insert_many(data)

    def search_data(self, field):
        return [x for x in self.words.find({}, {field: 1})]


