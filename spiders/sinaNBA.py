# -*- coding: utf-8 -*-
import scrapy
from  sinaNBASpider.items import SinanbaspiderItem
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

# first class crawler spider
# class SinanbaSpider(scrapy.Spider):
# 	name = 'sinaNBA'
# 	allowed_domains = ['http://sports.sina.com.cn/']
    # start_urls = ['http://sports.sina.com.cn/']
	# start_urls = ['http://sports.sina.com.cn/basketball/nba/2018-08-19/doc-ihhxaafy3751096.shtml']

	# def parse(self, response):
	# 	# print("get in ")
	# 	# print(response)

	# 	# self.logger.info('A response from %s just arrived!',response.url)
	# 	# pass
	# 	for h3 in response.xpath('//h3').extract():
	# 		yield {"title":h3}

	# 	for url in response.xpath('//a/@href').extract():
	# 		print(url)
	# 		# yield scrapy.Request(url,callback=self.parse)
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

	# def start_requests(self):
	# 	yield scrapy.Request('http://sports.sina.com.cn/basketball/nba/2018-08-19/doc-ihhxaafy3751096.shtml',callback=self.parse)
	# def parse(self,response):
	# 	for h3 in response.xpath('//h3').extract():
	# 		yield SinanbaspiderItem(title=h3)
	# 	for url in response.xpath('//a/@href').extract():
	# 		print(url)
	# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

	# def __init__(self,category=None,*args,**kwargs):
	# 	super(SinanbaSpider,self).__init__(*args,**kwargs)
	# 	self.start_urls = ['http://sports.sina.com.cn/basketball/nba/2018-08-19/doc-ihhxaafy3751096.shtml']
	# def parse(self,response):
	# 	for h3 in response.xpath('//h3').extract():
	# 		yield SinanbaspiderItem(title=h3)
	# 	for url in response.xpath('//a/@href').extract():
	# 		print(url)

# second sitemap spider 

# https://docs.scrapy.org/en/latest/topics/selectors.html


