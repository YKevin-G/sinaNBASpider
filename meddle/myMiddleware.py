from selenium import webdriver
from scrapy.http import HtmlResponse
import time
import random
from ..meddle.userAgent import userAgent 
from ..meddle.ipPool.ip import ip

class PhantomJSMiddleware(object):
	@classmethod
	def process_request(cls,request,spider):
		# if "sinaNBA" in request.meta:
		if spider.name == 'sinaNBA':
			driver = webdriver.PhantomJS("D:\\phantomjs-2.1.1-windows-install\\bin\\phantomjs.exe")
			# driver = webdriver.PhantomJS()
			# driver = webdriver.Chrome("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
			# 隐试等待2S
			# time.sleep(5)
			# driver.implicitly_wait(10)
			driver.implicitly_wait(5)
			driver.get(request.url)
			content = driver.page_source
			print('getdata')
			print('success')
			# print(request.meta['proxy'])
			return HtmlResponse(driver.current_url,body=content,encoding='utf-8',request=request)

class UserAgentMiddleware(object):
	def process_request(self,request,spider):
		if spider.name == 'sinaNBA':
			agent = random.choice(userAgent)
			request.headers['User-Agent'] = agent

class IpProxyMiddleware(object):
	def process_request(self,request,spider):
		if spider.name == 'sinaNBA':
			ipp = random.choice(ip)
			request.meta['proxy'] = ipp
			print(request.meta['proxy'])