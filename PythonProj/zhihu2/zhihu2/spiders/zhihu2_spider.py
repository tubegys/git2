# -*- coding: utf-8 -*-
import scrapy


class Zhihu2SpiderSpider(scrapy.Spider):
    name = "zhihu2_spider"
    allowed_domains = ["www.zhihu.com"]
    start_urls = ['http://www.zhihu.com/']

    def parse(self, response):
        pass
