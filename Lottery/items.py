# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#超级大乐透
class LotteryItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    issue = scrapy.Field()
    front_number_one = scrapy.Field()
    front_number_two = scrapy.Field()
    front_number_three = scrapy.Field()
    front_number_four = scrapy.Field()
    front_number_five = scrapy.Field()
    back_number_one = scrapy.Field()
    back_number_two = scrapy.Field()
    date = scrapy.Field()
