from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity,TakeFirst,MapCompose,Join

	# 获取到的信息是列表形式，只取出第一个使用，在之前要进行判空操作
def extractOneEle(self,values):
	if(len(values) >= 1):
		return values[0]
	else:
		return "did not catch value"

class MyItemLoader(ItemLoader):
	default_output_processor = Identity()
	default_input_processor = Identity()


	newsUrl_out= extractOneEle
	# out 是默认输出
	# 判断有无获取到数据，判断固定位置是不是空值！？最终格式 名字1>name2>name3
	newsGroup_out = Join('>')
    # 最终格式 addr1>addr2>addr3
	newsGroupLink_out = Join('<')
    # 3、新闻标题
	newsTopic_out = extractOneEle
    # 4、新闻副标题
	newsSecondTopic_out = extractOneEle
    # 5、新闻发布时间
	newsPublishTime_out = extractOneEle
    # 6、新闻发布机构
	newsPublishOffice_out = extractOneEle
    # 7、新闻发布机构 链接
	newsPublishOfficaLink_out = extractOneEle
    # 8、标题出现的新闻访问评论数量
	newsFirstCommentCount_out = extractOneEle
    # 9、新闻配图!!!!!!
	newsPicture_out = extractOneEle
    # 10、新闻配图名称  考虑含有多个的额情况！！！！ 需要设计函数进行接收
	newsPictureName_out = extractOneEle
    # 11、新闻正文  设计函数对其中的是否含有广告链接进行判断,!!!!需要再次处理！！！
	newsContent_out = Join("<<<<")
    # 12、新闻作者 也要设计函数对数据的格式进行处理，有的作者格式是（）在括号内的 !!!!需要再次处理！！！
	newsAuthor_out = Join("<<<<")
    # 13、有关新闻的所有关键字  对关键字进行处理 使用","将关键字进行连接，
    # improvement:在这之前需要使用正则表达式判断关键字内不得包含分隔符，否则进行加密
	newsKeywords_out = Join(',')
    # 14、有关新闻的关键字对应的链接(以列表的形式)进行存储!!!!!!!!!
	newsKeywordsAndLink_out = Join("<")
    # 15、新闻评论的数量
	newsSecondCommentCount_out = extractOneEle
    # 16、新闻评论数量对应的链接
	newsSecondCommentCountLink_out = extractOneEle
    # 17、新闻评论参与人数
	newsSecondCommentPeopleCount_out = extractOneEle
    # 18、新闻评论参与人数对应链接
	newsSecondCommentPeopleCountLink_out = extractOneEle
	# 19、与本新闻相关的所有评论所在的链接
	newsAllCommentsLink_out = extractOneEle


