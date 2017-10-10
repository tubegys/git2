# -*- coding: utf-8 -*-
import scrapy
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from selenium import webdriver
import time
import json
import re
from urllib import parse
from items import ZhihuAnswerItem, ZhihuQuestionItem
from scrapy.loader import ItemLoader
from datetime import datetime
from items import ZhihuItemLoader

class ZhihuSpider(scrapy.Spider):
    name = "zhihu"
    allowed_domains = ["www.zhihu.com"]
    start_urls = ['https://www.zhihu.com/']
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36(KHTML, like Gecko)"
                      " Chrome/59.0.3071.104 Safari/537.36",
        "Host": "www.zhihu.com",
        "Referer": "https://www/zhihu.com"
    }

    def __init__(self):
        self.browser = webdriver.Chrome(executable_path='D:\chromedriver.exe')
        self.browser.get('https://www.zhihu.com/#signin')
        self.browser.implicitly_wait(10)
        self.browser.find_element_by_css_selector('.view-signin input[name="account"]').send_keys('17701683279')
        self.browser.find_element_by_css_selector('.view-signin input[name="password"]').send_keys('coekie')
        time.sleep(10)
        print('TIMES UP...............')
        self.init_url = self.browser.current_url
        # get_cookies  返回的是list
        self.cookies = self.browser.get_cookies()

        super(ZhihuSpider, self).__init__()
        # 当爬虫结束的时候，发送一个spider_closed信号，并调用self.spider_closed函数
        dispatcher.connect(self.spider_closed, signals.spider_closed)
        print("__INIT__  finished....")

    def spider_closed(self):
        print('zhihu spider is closed....')
        self.browser.close()

    def start_requests(self):
        return [scrapy.Request('https://www.zhihu.com/#signin', cookies=self.cookies,
                               headers=self.headers, callback=self.check_login)]

    def check_login(self, response):
        # json_text = json.loads(response.text)
        for url in self.start_urls:
            yield scrapy.Request(url, dont_filter=True, cookies=self.cookies, headers=self.headers)

    def parse(self, response):
        # 获取当前页面所有的url
        all_urls = response.css('a::attr(href)').extract()
        # 由于提取到的url不包含域名，需要添加域名
        all_urls = [parse.urljoin(response.url, url) for url in all_urls]
        # 过滤不需要的url
        all_urls = filter(lambda x: True if x.startswith('https') else False, all_urls)
        for url in all_urls:
            match_obj = re.match('(.*www.zhihu.com/question/(\d+))(/|$).*', url)
            if match_obj:
                request_url = match_obj.group(1)
                question_id = match_obj.group(2)
                yield scrapy.Request(request_url, headers=self.headers,
                                     meta={'question_id': question_id},
                                     callback=self.parse_question)
            else:
                yield scrapy.Request(url, headers=self.headers, callback=self.parse)

    def parse_question(self, response):
        item_loader = ZhihuItemLoader(item=ZhihuQuestionItem(), response=response)
        item_loader.add_css('title', '.QuestionHeader-main h1::text')
        item_loader.add_css('content', '.QuestionRichText span::text')
        item_loader.add_value('url', response.url)
        item_loader.add_value('zhihu_id', response.meta.get('question_id'))
        item_loader.add_css('answer_num', '.List-headerText span::text')
        item_loader.add_css('comments_num', '.QuestionHeader-Comment .Button::text')
        item_loader.add_css('topics', '.QuestionHeader-topics .Popover div::text')
        item_loader.add_css('watch_user_num', '.QuestionFollowStatus .Button .NumberBoard-value::text')
        item_loader.add_css('click_num', '.QuestionFollowStatus .NumberBoard-item .NumberBoard-value::text')
        item_loader.add_value('crawl_time', datetime.now())
        question_item = item_loader.load_item()

        yield question_item
