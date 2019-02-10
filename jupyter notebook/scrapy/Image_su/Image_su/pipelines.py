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

        self.cur.execute("INSERT INTO image_suuz (sentence,image_url,time,word,comment,likee,read_num) VALUES (%s,%s,%s,%s,%s,%s,%s)", (item['sentence'],item['image_url'],item['time'],item['word'],item['comment'],item['likee'],item['read_num']))
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.conn.close()
