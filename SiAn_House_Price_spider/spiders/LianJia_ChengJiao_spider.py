'''
@Author: MengHan
@Go big or Go home
@Date: 2020-09-27 13:25:50
@LastEditTime: 2020-09-27 17:31:23
'''
import scrapy
import time
import re
from ..items import SianHouseChengJiaoSpiderItem

class LianjiaSpiderSpider(scrapy.Spider):
    name = 'LianJia_ChengJiao_spider'
    allowed_domains = ['lianjia.com']
    start_urls = [f'https://xa.lianjia.com/chengjiao/']

    def parse(self, response):
        hose_url = response.xpath('.//div[@data-role="ershoufang"]/div[1]/a/@href').getall() #.position > dl:nth-child(2) > dd:nth-child(2) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)
        for url in hose_url:
            yield scrapy.Request('https://xa.lianjia.com' + url, callback=self.pick_up_index_link)

    def pick_up_index_link(self, response):
        page_r = re.compile('\d{2,3}')
        page = page_r.search( response.xpath('.//div[@class="page-box fr"]').get())
        if bool(page):
            url_list = [response.url + f'pg{p}/' for p in page.group()]
            for url in url_list:
                yield scrapy.Request(url=url, callback=self.get_detail_link)
    def get_detail_link(self,response):
        hose_url = response.css('.title > a::attr(href)').getall()
        for url in hose_url:
            yield scrapy.Request(url,callback=self.pick_up_hose)


    
    def pick_up_hose(self, response):
        item = SianHouseChengJiaoSpiderItem()
        item['hose_url'] = response.url
        item['hose_img'] = response.css('.imgContainer > img::attr(src)').get()
        item['spider_add_time'] = int(time.time())
        item['lianjia_id'] = int(response.xpath('.//div[@class="transaction"]//li[1]/text()').get())
        item['hose_title'] = response.css('.wrapper::text').get()
        item['chengjiao_time'] = self.get_time(response.css('.wrapper > span::text').get())
        item['chengjiao_zhouqi'] = response.xpath('.//div[@class="msg"]/span[2]/label/text()').get()
        item['chengjiao_money'] = response.xpath('.//span[@class="dealTotalPrice"]//i/text()').get()
        item['hose_guapai_money'] = response.xpath('.//div[@class="msg"]/span[1]/label/text()').get()
        item['hose_position'] = self.get_postition(response.xpath('.//div[@class="deal-bread"]/a[3]/text()').get())
        item['hose_community'] = self.get_postition(response.xpath('.//div[@class="deal-bread"]/a[5]/text()').get())
        item['hose_age'] = response.xpath('.//div[@class="transaction"]/div[2]//li[5]/text()').get()
        item['hose_money_m'] = response.xpath('.//span[@class="dealTotalPrice"]/i/text()').get()
        item['hose_unit_type'] = response.xpath('.//div[@class="introContent"]/div//li/text()').get()
        item['hose_real_area'] = response.xpath('.//div[@class="introContent"]/div//li[3]/text()').get()
        item['hose_floor'] = response.xpath('.//div[@class="introContent"]/div//li[2]/text()').get()
        item['hose_added_time'] = response.xpath('.//div[@class="transaction"]//li[3]/text()').get()
        item['hose_attributes'] = response.xpath('.//div[@class="transaction"]//li[2]/text()').get()
        yield item

    def get_time(self, conn):
        conn = conn.replace('.','-')
        time_r = re.compile('\d+-\d+-\d+')
        time_conn = time_r.search(conn)
        if bool(time_conn):
            return time_conn.group()
    
    def get_postition(self,conn):
        conn = conn.replace('二手房成交','')
        return conn
        