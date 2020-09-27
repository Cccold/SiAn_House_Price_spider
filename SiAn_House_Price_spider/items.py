'''
@Author: MengHan
@Go big or Go home
@Date: 2020-09-27 16:56:10
@LastEditTime: 2020-09-27 17:32:02
'''
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SianHousePriceSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    hose_url = scrapy.Field()
    hose_img = scrapy.Field()#户型图
    spider_add_time = scrapy.Field() #爬虫入库时间
    lianjie_id = scrapy.Field()#链家编号
    hose_title = scrapy.Field()#标题
    hose_position = scrapy.Field()#区域位置
    hose_community = scrapy.Field()#小区名字
    hose_money = scrapy.Field()#总价
    hose_money_m = scrapy.Field()#每平米
    hose_unit_type = scrapy.Field()#户型
    hose_area = scrapy.Field()#总面积
    hose_real_area = scrapy.Field()#真实面积
    hose_floor = scrapy.Field()#楼层
    hose_added_time = scrapy.Field()#链家挂牌时间
    hose_age_limit = scrapy.Field()# 房子年限 满三满2？
    hose_attributes = scrapy.Field()#房屋属性 商品房？
    host_mortgage = scrapy.Field()#抵押信息 是否贷款？

class SianHouseChengJiaoSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    hose_url = scrapy.Field()
    hose_img = scrapy.Field()#户型图
    spider_add_time = scrapy.Field() #爬虫入库时间
    chengjiao_time = scrapy.Field() #成交日期
    chengjiao_zhouqi = scrapy.Field() #成交周期
    chengjiao_money = scrapy.Field() # 成交价格
    hose_guapai_money = scrapy.Field() #挂牌价格
    lianjia_id = scrapy.Field()#链家编号
    hose_title = scrapy.Field()#标题
    hose_position = scrapy.Field()#区域位置
    hose_community = scrapy.Field()#小区名字
    hose_age = scrapy.Field() #房子建成年代
    hose_money_m = scrapy.Field()#每平米
    hose_unit_type = scrapy.Field()#户型
    hose_real_area = scrapy.Field()#真实面积
    hose_floor = scrapy.Field()#楼层
    hose_added_time = scrapy.Field()#链家挂牌时间
    hose_attributes = scrapy.Field()#房屋属性 商品房？


   

