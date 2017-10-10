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
    url = scrapy.Field()
    url_object_id = scrapy.Field()  # md5
    fav_nums = scrapy.Field()
    praise_nums = scrapy.Field()
    comment_nums = scrapy.Field()
    front_image_url = scrapy.Field()
    front_image_url_path = scrapy.Field()
    tags = scrapy.Field()

    