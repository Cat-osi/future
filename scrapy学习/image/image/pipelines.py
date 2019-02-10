# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.http import Request

class ImagePipeline(object):
    def process_item(self, item, spider):
        for i in item['src']:
            print(str(i))
            yield  Request(i)
        return item
