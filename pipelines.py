# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.conf import settings
import pymongo

class SinanbaspiderPipeline(object):
	collection_name = "ddds"

	def __init__(self,mongo_uri,mongo_db,mongo_port):
		self.mongo_uri = mongo_uri
		self.mongo_db = mongo_db
		self.mongo_port = mongo_port
	@classmethod
	def from_crawler(cls,crawler):
		return cls(mongo_port = crawler.settings.get("MONGODB_PORT",27017),mongo_uri= crawler.settings.get('MONGODB_HOST','localhost'),mongo_db = crawler.settings.get("MONGODB_DBNAME",'items'))
	def open_spider(self,spider):
		self.client = pymongo.MongoClient(self.mongo_uri,self.mongo_port)
		self.db = self.client[self.mongo_db]

	def close_spider(self,spider):
		print("save successfully")
		print(self.db.collection_names(include_system_collections=False),"ddd")
		self.client.close()
	def process_item(self,item,spider):
		post = {'author':"mike",'text':"first post"}
		self.db[self.collection_name].insert_one(dict(item))
		return item
	# def __init__(self):
	# 	host = settings['MONGODB_HOST']
	# 	port = settings['MONGODB_PORT']
	# 	dbname = settings['MONGODB_DBNAME']

	# 	# 建立数据库连接
	# 	client = pymongo.MongoClient(host=host,port=port)
	# 	# 指向指定数据库   mdb = client['Douban']
	# 	mdb = client['sinaNBA']
	# 	# 表名,collection
	# 	self.post = mdb["sinaNBA"]

	# def process_item(self, item, spider):
	# 	data = dict(item)
	# 	self.post.insert(data)
	# 	print(self.mdb.collection_names(include_system_collections=False),"ddd")
	# 	return item
