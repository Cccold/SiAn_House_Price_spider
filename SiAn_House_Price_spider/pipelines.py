'''
@Author: MengHan
@Go big or Go home
@Date: 2020-09-25 15:12:20
@LastEditTime: 2020-09-25 16:06:27
'''
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from itemadapter import ItemAdapter

class SianHousePriceSpiderPipeline:
    def __init__(self, MONGO_HOST, MONGO_PORT, MONGO_DB, MONGO_COLL, MONGO_USER, MONGO_PWD):  
        # self.client = pymongo.MongoClient(host=MONGO_HOST, port=MONGO_PORT)  
        # self.mongo_db = self.client[MONGO_DB]  # 获得数据库的句柄  
        # self.mongo_db.authenticate(MONGO_USER, MONGO_PWD)  
        # self.collection_name = self.mongo_db[MONGO_COLL]  # 获得collection的句柄  
        client = pymongo.MongoClient(host=MONGO_HOST, port=MONGO_PORT)  
        self.db = client[MONGO_DB]  # 获得数据库的句柄  
        self.coll = self.db[MONGO_COLL]  # 获得collection的句柄  
        # 数据库登录需要帐号密码的话  
        self.db.authenticate(MONGO_USER, MONGO_PWD)  
  

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            MONGO_HOST=crawler.settings.get('MONGO_HOST'),
            MONGO_PORT=crawler.settings.get('MONGO_PORT'),
            MONGO_DB=crawler.settings.get('MONGO_DB'),
            MONGO_COLL=crawler.settings.get('MONGO_COLL'),
            MONGO_USER=crawler.settings.get('MONGO_USER'),
            MONGO_PWD=crawler.settings.get('MONGO_PWD')
        )

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        postItem = dict(item)  # 把item转化成字典形式  
        self.coll.insert(postItem)  # 向数据库插入一条记录  
        return item  # 会在控制台输出原item数据，可以选择不写
    