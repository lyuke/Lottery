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
    frontNumberOne = scrapy.Field()
    frontNumberTwo = scrapy.Field()
    frontNumberThree = scrapy.Field()
    frontNumberFour = scrapy.Field()
    frontNumberFive = scrapy.Field()
    backNumberOne = scrapy.Field()
    backNumberTwo = scrapy.Field()
    openDate = scrapy.Field()
