# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
import pymysql
class TutorialPipeline(object):
    def process_item(self, item, spider):

        return item


class JsonWithEncodingPipeline(object):
    def __init__(self):
        self.file = codecs.open('article.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        lines = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(lines)
        return item

    def spider_closed(self, spider):
        self.file.close()


class MysqlPipeline(object):
    def __init__(self):
        self.db = pymysql.connect(host='127.0.0.1', user='gys', passwd='123', db='db_gys', charset="utf8")
        self.cur = self.db.cursor()

    def process_item(self, item, spider):
        ins_sql = 'insert into tb_jobbole(title,create_date,fav_nums,praise_nums,' \
                  'comment_nums)values(%s,%s,%s,%s,%s)'
        self.cur.execute(ins_sql, (item['title'], item['create_date'], item['fav_nums']
                                  , item['praise_nums'], item['comment_nums']))
        self.db.commit()

    def spider_closed(self, spider):
        self.db.close()