# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request
import re
from Image_su.items import  ImageSuItem

class ImageSuSpider(CrawlSpider):
    name = 'image_su'
    allowed_domains = ['isujin.com']
    start_urls = ['https://isujin.com/']

    rules = (
        Rule(LinkExtractor(allow='^\d*'), callback='parse_item', follow=True),
    )

    def start_requests(self):
        heads={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, cko) Chromlike Gee/54.0.2840.87 Safari/537.36"}
        yield  Request("https://isujin.com/",headers=heads)

    def parse_item(self, response):
        i=ImageSuItem()
        i['image_temp']=response.xpath('//div[@class="images"]/div[@id="jg"]//a/@href').extract()
        '''i['sentence']=response.xpath('//div[@class="show"]/div[@class="article"]/h1[@class="title"]/text()').extract()
        i['time']=response.xpath('//div[@class="show"]/div[@class="article"]/div[@class="stuff"]/span[1]/text()').extract()
        i['read_num']=response.xpath('//div[@class="show"]/div[@class="article"]/span[2]/text()').extract()
        i['word']=response.xpath('//div[@class="show"]/div[@class="article"]/span[3]/text()').extract()
        i['comment']=response.xpath('//div[@class="show"]/div[@class="article"]/span[4]/text()').extract()
        i['like']=response.xpath('//*[@id="single"]/div[2]/div[2]/div/div[1]/span[5]/text()').extract()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()'''
        return i
