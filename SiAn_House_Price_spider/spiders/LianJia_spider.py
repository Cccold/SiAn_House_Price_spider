# -*- coding: utf-8 -*-
import scrapy


class LianjiaSpiderSpider(scrapy.Spider):
    name = 'LianJia_spider'
    allowed_domains = ['lianjia.com']
    start_urls = ['http://lianjia.com/']

    def parse(self, response):
        pass
