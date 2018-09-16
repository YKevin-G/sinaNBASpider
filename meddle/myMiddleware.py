from selenium import webdriver
from scrapy.http import HtmlResponse
import time

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
			return HtmlResponse(driver.current_url,body=content,encoding='utf-8',request=request)