# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ImageSuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    image_url=scrapy.Field()
    sentence=scrapy.Field()
    time=scrapy.Field()
    read_num=scrapy.Field()
    word=scrapy.Field()
    comment=scrapy.Field()
    likee=scrapy.Field()
    pass
