# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SinanbaspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # 1、本新闻的所在网页链接
	newsUrl= scrapy.Field(serializer=str)
    # !!!!
	# 2、新闻所属分组 这里面包含了四个字段 格式定义为由 ">"连接起来  
	newsGroup = scrapy.Field(serializer=str)
    # 新闻所属分组的每一个层级对应的链接和名字,以字典形式显示
	newsGroupLink = scrapy.Field(serializer=dict)
    # 3、新闻标题
	newsTopic = scrapy.Field(serializer=str)
    # 4、新闻副标题
	newsSecondTopic = scrapy.Field(serializer=str)
    # 5、新闻发布时间
	newsPublishTime = scrapy.Field(serializer=str)
    # 6、新闻发布机构
	newsPublishOffice = scrapy.Field(serializer=str)
    # 7、新闻发布机构 链接
	newsPublishOfficaLink = scrapy.Field(serializer=str)
    # 8、标题出现的新闻访问评论数量
	newsFirstCommentCount = scrapy.Field(serializer=int)
    # 9、新闻配图!!!!!!
	newsPicture = scrapy.Field()
    # 10、新闻配图名称  考虑含有多个的额情况！！！！ 需要设计函数进行接收
	newsPictureName = scrapy.Field(serializer=str)
    # 11、新闻正文  设计函数对其中的是否含有广告链接进行判断
	newsContent = scrapy.Field(serializer=str)
    # 12、新闻作者 也要设计函数对数据的格式进行处理，有的作者格式是（）在括号内的
	newsAuthor = scrapy.Field(serializer=str)
    # 13、有关新闻的所有关键字  对关键字进行处理 使用","将关键字进行连接，
    # improvement:在这之前需要使用正则表达式判断关键字内不得包含分隔符，否则进行加密
	newsKeywords = scrapy.Field(serializer=str)
    # 14、有关新闻的关键字对应的链接(以列表的形式)进行存储!!!!!!!!!
	newsKeywordsAndLink = scrapy.Field(serializer=dict)
    # 15、新闻评论的数量
	newsSecondCommentCount = scrapy.Field(serializer=int)
    # 16、新闻评论数量对应的链接
	newsSecondCommentCountLink = scrapy.Field(serializer=str)
    # 17、新闻评论参与人数
	newsSecondCommentPeopleCount = scrapy.Field(serializer=int)
    # 18、新闻评论参与人数对应链接
	newsSecondCommentPeopleCountLink = scrapy.Field(serializer=str)
	# 19、与本新闻相关的所有评论所在的链接
	newsAllCommentsLink = scrapy.Field(serializer=str)
    # pass
