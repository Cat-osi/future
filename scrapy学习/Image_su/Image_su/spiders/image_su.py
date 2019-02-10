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
        i['image_url']=response.url
        #i['image_url']=response.xpath('//div[@class="images"]/div[@id="jg"]//a/@href').extract()
        i['sentence']=response.xpath('//*[@id="single"]/div[2]/div[2]/div/h1/text()').extract()
        i['time']=response.xpath('//*[@id="single"]/div[2]/div[2]/div/div[1]/span[1]/text()').extract()
        i['read_num']=response.xpath('//*[@id="single"]/div[2]/div[2]/div/div[1]/span[2]/text()').extract()[0].split(' ')[1]
        i['word']=response.xpath('//*[@id="single"]/div[2]/div[2]/div/div[1]/span[3]/text()').extract()[0].split(' ')[1]
        i['comment']=response.xpath('//*[@id="single"]/div[2]/div[2]/div/div[1]/span[4]/text()').extract()[0].split(' ')[1]
        i['likee']=response.xpath('//*[@class="likeThis"]/span[2]/text()')[0].extract()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
