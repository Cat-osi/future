# -*- coding: utf-8 -*-
import scrapy
from aa.items import AaItem
from scrapy.http import Request

class QsbkSpider(scrapy.Spider):
    name = 'qsbk'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['http://qiushibaike.com/']
    def start_requests(self):
        heads={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, cko) Chromlike Gee/54.0.2840.87 Safari/537.36"}
        yield  Request("http://qiushibaike.com/",headers=heads)
    def parse(self, response):
        it=AaItem()
        it["content"]=response.xpath("//div[@class='content']/span/text()").extract()
        it["link"]=response.xpath("//a[@class='contentHerf']/@href").extract()
        yield  it
