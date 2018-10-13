import requests,threading,datetime
from bs4 import BeautifulSoup
import random

# 写入文档
def write(path,text):
	with open(path,'a',encoding='utf-8') as f:
		f.writelines(text)
		f.write('\n')

# 清空文档
def truncatefile(path):
	with open(path,'w',encoding='utf-8') as f:
		f.truncate()

# 读取文档
def read(path):
	with open(path,'r',encoding='utf-8') as f:
		txt = []
		for s in f.readlines():
			txt.append(s.strip())
	return txt

def gettimediff(start,end):
	seconds = (end - start).seconds
	m,s = divmod(seconds,60)
	h,m = divmod(m,60)
	diff = ("%02d:%02d:%02d"%(h,m,s))
	return diff

def getheaders():
	user_agent_list = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",\
	"Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11", \
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6", \
	"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6", \
	"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1", \
	"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5", \
	"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5", \
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
	"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
	"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
	"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
	"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
	"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", \
	"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", \
	"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
	]
	UserAgent = random.choice(user_agent_list)
	headers = {'User-Agent':UserAgent}
	return headers

def checkip(targeturl,ip):
	headers = getheaders()
	proxies = {"http":"http://"+ip,"https" : "https://"+ip}
	try:
		response = requests.get(url = targeturl,proxies=proxies,headers=headers,timeout=5).status_code
		if response == 200:
			return True 
		else:
			return False
	except:
		return False

def findip(typee,pagenum,targeturl,path):
	llist = {'1':'http://www.xicidaili.com/nt/',
			 '2':'http://www.xicidaili.com/nn/',
			 '3':'http://www.xicidaili.com/wn/',
			 '4':'http://www.xicidaili.com/wt/'
	}
	url = llist[str(typee)] + str(pagenum)
	headers = getheaders()
	html = requests.get(url=url,headers=headers,timeout = 5).text
	soup = BeautifulSoup(html,'lxml')
	alldata = soup.find_all('tr',class_='odd')
	for i in alldata:
		t = i.find_all('td')
		ip = t[1].text + ':' + t[2].text
		is_avail = checkip(targeturl,ip)
		if is_avail == True:
			write(path = path,text=ip)
			print(ip)

def getip(targeturl,path):
	truncatefile(path)
	start = datetime.datetime.now()
	threads = []
	for ttype in range(4):
		for pagenum in range(3):
			threads.append(threading.Thread(target = findip,args = (ttype+1,pagenum+1,targeturl,path)))
			# t = threading.Thread(target = findip,args = (ttype+1,pagenum+1,targeturl,path))
			# threads.append(t)
			# t = None
	print("start crawling proxy ip")
	for s in threads:
		s.start()
	for e in threads:
		e.join()
	print('finished')
	end = datetime.datetime.now()
	diff = gettimediff(start,end)
	ips = read(path)
	print("all links:%s, waste time:%s"%(len(ips),diff))

if __name__ == "__main__":
	path = '.\\ipPool\\ip.txt'
	targeturl = 'http://www.cnblogs.com/TurboWay/'
	getip(targeturl,path)
