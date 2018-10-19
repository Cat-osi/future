# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
class ImageSuPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='localhost',user='root',password='hybaba',db='image_su',use_unicode=True,charset='utf8')
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        for i in item['image_temp']:
            self.cur.execute("INSERT INTO image_suu (image_url) VALUES (%s)", i)
            self.conn.commit()
            print(item['image_temp'])
        return item

    def close_spider(self, spider):
        self.conn.close()
