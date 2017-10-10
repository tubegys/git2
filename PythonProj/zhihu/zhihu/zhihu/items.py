# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Identity
import datetime
from scrapy.loader import ItemLoader


class ZhihuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ZhihuItemLoader(ItemLoader):
    """自定义ItemLoader"""
    default_output_processor = TakeFirst()


def prefix_zhihu(value):
    """给title字段添加zhihu-spider的前缀"""
    return 'zhihu-spider:'+value


def date_formatter(value):
    """转换时间的格式为  XXXX-XX-XX xx:xx:xx """
    try:
        formatter_date = datetime.datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
    except Exception as e:
        formatter_date = datetime.datetime.now()
    return formatter_date


class ZhihuQuestionItem(scrapy.Item):
    # 文章的标题
    title = scrapy.Field(
        # input_processor=MapCompose(prefix_zhihu)  # 默认将解析到的title作为参数传入prefix中进行处理
    )
    zhihu_id = scrapy.Field()
    topics = scrapy.Field()
    url = scrapy.Field()

    content = scrapy.Field()
    # create_time = scrapy.Field(
    #     # input_processor=MapCompose(date_formatter),
    #     # output_processor=TakeFirst()
    # )
    # update_time = scrapy.Field()
    answer_num = scrapy.Field()
    comments_num = scrapy.Field()
    watch_user_num = scrapy.Field()
    click_num = scrapy.Field(
        output_processor=Identity()
    )
    crawl_time = scrapy.Field()


class ZhihuAnswerItem(scrapy.Item):
    zhihu_id = scrapy.Field()
    url = scrapy.Field()
    question_id = scrapy.Field()
    author_id = scrapy.Field()
    content = scrapy.Field()
    parise_num = scrapy.Field()
    comments_num = scrapy.Field()
    create_time = scrapy.Field()
    update_time = scrapy.Field()
    crawl_time = scrapy.Field()
