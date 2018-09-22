# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.conf import settings
import pymongo

class SinanbaspiderPipeline(object):
	def __init__(self):
		host = settings['MONGODB_HOST']
		port = settings['MONGODB_PORT']
		dbname = setting['MONGODB_DBNAME']

		# 建立数据库连接
		client = pymongo.MongoCLient(host=host,port=port)
		# 指向指定数据库   mdb = client['Douban']
		mdb = dbname
		# 表名
		self.post = mdb[settings['MONGODB_DOCNAME']]

    def process_item(self, item, spider):
    	data = dict(item)
    	self.post.insert(data)
        return item
