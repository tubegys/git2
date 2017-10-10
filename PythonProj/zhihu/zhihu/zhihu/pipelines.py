# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class ZhihuPipeline(object):
    def process_item(self, item, spider):
        return item


class ZhihuQuestionPipeline(object):
    def __init__(self):
        self.db = pymysql.connect(host='127.0.0.1',
                                  user='root', passwd='123456',
                                  charset='utf8', db='db_gys')
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        insert_sql = 'insert into tb_zhihu_question(zhihu_id,url,title,crawl_time) values(%s,%s,%s,%s)'
        self.cursor.execute(insert_sql, (item['zhihu_id'], item['url'], item['title'], item['crawl_time']))
        self.db.commit()

    def spider_closed(self, spider):
        self.db.close()
