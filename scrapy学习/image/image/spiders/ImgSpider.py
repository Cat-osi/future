# -*- coding: utf-8 -*-
import scrapy
from image.items import ImageItem
from scrapy.http import Request

class ImgspiderSpider(scrapy.Spider):
    name = 'ImgSpider'
    allowed_domains = ['lab.scrapyd.cn']
    start_urls = ['http://lab.scrapyd.cn/archives/55.html']
    def start_requests(self):
        heads={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, cko) Chromlike Gee/54.0.2840.87 Safari/537.36"}
        yield  Request("http://lab.scrapyd.cn/archives/55.html",headers=heads)

    def parse(self, response):
        a=ImageItem()
        a['src']=response.xpath('//p/img[@src]').extract()
        yield a
