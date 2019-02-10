# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from qsauto.items import QsautoItem
from scrapy.http import Request

class QsbkSpider(CrawlSpider):
    name = 'qsbk'
    allowed_domains = ['miaosha.jd.com']
    start_urls = ['https://miaosha.jd.com/category.html?cate_id=29']

    rules = (
        Rule(LinkExtractor(allow='cate_id'), callback='parse_item', follow=True),
    )
    def start_requests(self):
        heads={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, cko) Chromlike Gee/54.0.2840.87 Safari/537.36"}
        yield  Request("http://qiushibaike.com/",headers=heads)

    def parse_item(self, response):
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        it=QsautoItem()
        it["content"] = response.xpath("/h4[@class='seckill_mod_goods_title']/text()").extract()
        it["link"] = response.xpath("//i[@class='seckill_mod_goods_price_now']/text()").extract()
        return it
