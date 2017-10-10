# -*- coding: utf-8 -*-
import scrapy


class JobboleSpiderSpider(scrapy.Spider):
    name = "jobbole_spider"
    allowed_domains = ["www.jobbole.com"]
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        with open('D:\jobbole.html', 'wb') as f:
            f.write(response.text.encode('utf-8'))
        pass

