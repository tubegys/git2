# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class jobboleItem(scrapy.Item):
    title = scrapy.Field()
    create_date = scrapy.Field()
    fav_nums = scrapy.Field()
    praise_nums = scrapy.Field()
    comment_nums = scrapy.Field()
    url = scrapy.Field()
    