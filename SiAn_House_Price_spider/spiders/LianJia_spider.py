'''
@Author: MengHan
@Go big or Go home
@Date: 2020-09-25 15:25:38
@LastEditTime: 2020-09-25 15:25:39
'''
# -*- coding: utf-8 -*-
import scrapy
import time
from ..items import SianHousePriceSpiderItem

class LianjiaSpiderSpider(scrapy.Spider):
    name = 'LianJia_spider'
    allowed_domains = ['lianjia.com']
    start_urls = [f'https://xa.lianjia.com/ershoufang/pg{page}/' for page in range(1,101)]

    def parse(self, response):
        hose_url = response.css('a.title::attr(href)').getall()
        for url in hose_url:
            yield scrapy.Request(url,callback=self.pick_up_hose)
    
    def pick_up_hose(self, response):
        item = SianHousePriceSpiderItem()
        item['hose_url'] = response.url
        item['hose_img'] = response.css('.imgdiv > img::attr(src)').get()
        item['spider_add_time'] = int(time.time())
        item['lianjie_id'] = int(response.css('span.info:nth-child(2)::text').get())
        item['hose_title'] = response.css('h1::text').get()
        item['hose_position'] = response.xpath('.//div[@class="areaName"]//a[1]/text()').get()
        item['hose_community'] = response.css('a.info::text').get()
        item['hose_money'] = response.css('.total::text').get() #万元
        item['hose_money_m'] = response.css('.unitPriceValue::text').get() #元/m
        item['hose_unit_type'] = response.xpath('.//div[@class="base"]//li[1]/text()').get()
        item['hose_area'] = response.xpath('.//div[@class="base"]//li[3]/text()').get()
        item['hose_real_area'] = response.xpath('.//div[@class="base"]//li[5]/text()').get()
        item['hose_floor'] = response.xpath('.//div[@class="base"]//li[2]/text()').get()
        item['hose_added_time'] = response.xpath('.//div[@class="transaction"]//li[1]/span[2]/text()').get()
        item['hose_age_limit'] = response.xpath('.//div[@class="transaction"]//li[5]/span[2]/text()').get()
        item['hose_attributes'] = response.xpath('.//div[@class="transaction"]//li[2]/span[2]/text()').get()
        item['host_mortgage'] = response.xpath('.//div[@class="transaction"]//li[last()-1]/span[2]/text()').get().replace(' ','').replace('\n','')
        yield item
