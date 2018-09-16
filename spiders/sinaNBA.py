# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from  sinaNBASpider.items import SinanbaspiderItem
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from sinaNBASpider.MyItemLoader import MyItemLoader
import time

class SinanbaSpider(scrapy.Spider):
	name = "sinaNBA"
	allowed_domains = ['sports.sina.com.cn/']
	start_urls = ['http://sports.sina.com.cn/basketball/nba/2018-08-19/doc-ihhxaafy3751096.shtml']

	# def parse(self,response):
	# 	urls = start_urls
	# 	for url in urls:
	# 		request = Request(url=url,callback=self.parse_post,dont_filter=True)
	# 		request.meta['sinaNBA'] = True
	# 		yield request


	def parse(self,response):
		time.sleep(3)
		itemload = MyItemLoader(SinanbaspiderItem(),response=response)
		itemload.add_value('newsUrl',response.url)
		# 2、新闻所属分组 这里面包含了四个字段 ,以列表形式返回 
		itemload.add_xpath('newsGroup','//div[@class = "channel-path"]/a/text()')
		# SinanbaspiderItem.newsGroup = response.xpath('//div[@class == "channel-path"]/a/text()').extract()
		# 新闻所属分组的每一个层级对应的链接和名字,以列表形式显示
		itemload.add_xpath('newsGroupLink','//div[@class="channel-path"]/a/@href')
		# SinanbaspiderItem.newsGroupLink = response.xpath('//div[@class=="channel-path"]/a/@href').extract()
	    # 3、新闻标题
		itemload.add_xpath('newsTopic','//h1[@class="main-title"]/text()')
		# SinanbaspiderItem.newsTopic = response.xpath('//h1[@class=="main-title"]/text()').extract()
	    # 4、新闻副标题
		itemload.add_xpath('newsSecondTopic','//div[@class="second-title"]/text()')
		# SinanbaspiderItem.newsSecondTopic = response.xpath('//div[@class=="second-title"]/text()').extract()
	    # 5、新闻发布时间
		itemload.add_xpath('newsPublishTime','//span[@class="date"]/text()')
		# SinanbaspiderItem.newsPublishTime = response.xpath('//span[@class=="date"]/text()').extract()
	    # 6、新闻发布机构
		itemload.add_xpath('newsPublishOffice','//div[@class="date-source"]/a[@class="source ent-source"]/text()')
		# SinanbaspiderItem.newsPublishOffice = response.xpath('//span[@class=="date"]/a[@class=="source ent-source"]/text()').extract()
	    # 7、新闻发布机构 链接
		itemload.add_xpath('newsPublishOfficaLink','//div[@class="date-source"]/a[@class="source ent-source"]/@href')
		# SinanbaspiderItem.newsPublishOfficaLink = response.xpath('//span[@class=="date"]/a[class="source ent-source"]/@href').extract()
	    # 8、标题出现的新闻访问评论数量!!!!!!!!!!!!!!
# !!!!数字不对	
		itemload.add_xpath('newsFirstCommentCount','//span[@class="tool-icon tool-cmt"]/a/span[@class="num"]/text()')
		# SinanbaspiderItem.newsFirstCommentCount = response.xpath('//span[@class=="num"]/text()').extract()
	    # 9、新闻配图!!!!!!将配图保存到本地，然后将本地地址保存起来,文件保存地址 root+新闻连接中的日期+图片名(即该链接中的最后一部分)
		itemload.add_xpath('newsPicture','//div[@class="img_wrapper"]/img/@src')
		# SinanbaspiderItem.newsPicture = response.xpath('//div[@class=="img_wraper"]/img/@src').extract()
	    # 10、新闻配图名称  考虑含有多个的额情况！！！！ 需要设计函数进行接收//需要对文字进行清洗
		itemload.add_xpath('newsPictureName','//div[@class="img_wrapper"]/span[@class="img_descr"]/text()')
		# SinanbaspiderItem.newsPictureName = response.xpath('//div[@class=="img_wraper"]/span[@class=="img_descr"]/text()').extract()
	    # 11、新闻正文  设计函数对其中的是否含有广告链接进行判断
		itemload.add_xpath('newsContent','//div[@id="artibody"]/p/text()')
		# SinanbaspiderItem.newsContent = response.xpath('//div[@class = "article-content-left"]/p/text()').extract()[:-1]
	    # 12、新闻作者 也要设计函数对数据的格式进行处理，有的作者格式是（）在括号内的
		itemload.add_xpath('newsAuthor','//div[@id="artibody"]/p/text()')
		# SinanbaspiderItem.newsAuthor = response.xpath('//div[@class = "article-content-left"]/p/text()').extract()[-1]
	    # 13、有关新闻的所有关键字  对关键字进行处理 使用","将关键字进行连接，
	    # improvement:在这之前需要使用正则表达式判断关键字内不得包含分隔符，否则进行加密
		itemload.add_xpath('newsKeywords','//div[@class = "keywords"]/a/text()')
		# SinanbaspiderItem.newsKeywords = response.xpath('//div[@class="keywords",@id=="keywords"]/a/text()').extract()
	    # 14、有关新闻的关键字对应的链接(以列表的形式)进行存储!!!!!!!!!
		itemload.add_xpath('newsKeywordsAndLink','//div[@class="keywords"]/a/@href')
		# SinanbaspiderItem.newsKeywordsAndLink = response.xpath('//div[@class="keywords",@id=="keywords"]/a/@href').extract()
	    # 15、新闻评论的数量

		itemload.add_xpath('newsSecondCommentCount','//div[@class="hd clearfix"]/span[@class="count"]/em/a[@data-sudaclick="comment_sum_p"]/text()')
		# SinanbaspiderItem.newsSecondCommentCount = response.xpath('//div[@class="hd clearfix"]/span[@class=="count"/em/a/text()]').extract()[0]
	    # 16、新闻评论数量对应的链接

		itemload.add_xpath('newsSecondCommentCountLink','//div[@class="hd clearfix"]/span[@class="count"]/em/a[@data-sudaclick="comment_sum_p"]/@href')
		# SinanbaspiderItem.newsSecondCommentCountLink = response.xpath('//div[@class="hd clearfix"]/span[@class=="count"/em/a/@href]').extract()[0]
	    # 17、新闻评论参与人数

		itemload.add_xpath('newsSecondCommentPeopleCount','//div[@class="hd clearfix"]/span[@class="count"]/em/a[@data-sudaclick="comment_participatesum_p"]/text()')
		# SinanbaspiderItem.newsSecondCommentPeopleCount = response.xpath('//div[@class="hd clearfix"]/span[@class=="count"/em/a/text()]').extract()[1]
	    # 18、新闻评论参与人数对应链接

		itemload.add_xpath('newsSecondCommentPeopleCountLink','//div[@class="hd clearfix"]/span[@class="count"]/em/a[@data-sudaclick="comment_participatesum_p"]/@href')
		# SinanbaspiderItem.newsSecondCommentPeopleCountLink = response.xpath('//div[@class="hd clearfix"]/span[@class=="count"/em/a/@href]').extract()[1]
	    # 19、与本新闻相关的所有评论所在的链接

		itemload.add_xpath('newsAllCommentsLink','//div[@class="list-ft"]/a[@class="more"]/@href')
		# SinanbaspiderItem.newsAllCommentsLink = response.xpath('//div[@class=="list-ft"]/a[class=="more"]/@href').extract()
		s = itemload.load_item()
		print(s)



# first class crawler spider
# class SinanbaSpider(scrapy.Spider):
# 第一种
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
# 第二种
	# def start_requests(self):
	# 	yield scrapy.Request('http://sports.sina.com.cn/basketball/nba/2018-08-19/doc-ihhxaafy3751096.shtml',callback=self.parse)
	# def parse(self,response):
	# 	for h3 in response.xpath('//h3').extract():
	# 		yield SinanbaspiderItem(title=h3)
	# 	for url in response.xpath('//a/@href').extract():
	# 		print(url)
	# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 第三种
	# def __init__(self,category=None,*args,**kwargs):
	# 	super(SinanbaSpider,self).__init__(*args,**kwargs)
	# 	self.start_urls = ['http://sports.sina.com.cn/basketball/nba/2018-08-19/doc-ihhxaafy3751096.shtml']
	# def parse(self,response):
	# 	for h3 in response.xpath('//h3').extract():
	# 		yield SinanbaspiderItem(title=h3)
	# 	for url in response.xpath('//a/@href').extract():
	# 		print(url)

# https://docs.scrapy.org/en/latest/topics/selectors.html


