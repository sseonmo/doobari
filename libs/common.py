import requests
import crawl.libs.tmonUtil as tmonUtil
from bs4 import BeautifulSoup
from crawl.libs.chromedriver77 import getDriver
from time import sleep

def getSiteUrl():
	# 티몬,위메프,11번가
	siteUrl = {
		# 'tmon': 'http://search.tmon.co.kr/search/?keyword={}&thr=ts'
		'tmon': 'http://search.tmon.co.kr/api/search/v4/deals?_=2582161742&keyword={}&useTypoCorrection=true&mainDealOnly=true&page={}&sort=POPULAR&order=DESC&thr=ts'
	}
	return siteUrl

def getPageString(url):
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
	data = requests.get(url, headers=headers)
	print('request http status code: ', data)
	# validation check
	if data.status_code != 200:
		return None
	return data.content

def crawl(url, keyword, pageNum):
	# url set
	url = url.format(keyword, pageNum)
	print('page url  : ', url)
	return getPageString(url)

def seleniumCrawlForScrollPaging(url, keyword):
	url = url.format(keyword)
	print(url)
	driver = getDriver()
	driver.get(url)
	# div = driver.find_element_by_xpath('//*[@id="search_app"]/div[2]/section/div/ul/div/div')
	div = driver.find_element_by_class_name('infinite-scroll-component ')
	lis = div.find_elements_by_tag_name('li')
	liCnt = len(lis)

	pageSource = ''

	while True:
		try:
			li = lis[liCnt - 1]
			# li.sendKeys(Keys.PAGE_DOWN)
			driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			sleep(1)
			newDiv = driver.find_element_by_class_name('infinite-scroll-component ')
			newlis = newDiv.find_elements_by_tag_name('li')
			newlisCnt = len(newlis)

			# 스크롤 이전 item 과 갯수 비교
			if liCnt == newlisCnt:
				break

			lis = newlis
			liCnt = newlisCnt
		except Exception as ex:
			print('tmon scroll error : ', ex)
			continue
	#
	# pageSource = driver.page_source
	# driver.close()
	# return pageSource
	return driver



def crawlWithOutKeyword(url):
	# url set
	# call
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
	data = requests.get(url, headers=headers)
	print('request http status code: ', data)
	# validation check
	if data.status_code != 200:
		return None
	return data.content

# html parser
def htmlParser(pageString):
	return BeautifulSoup(pageString, 'html.parser')

def convertPrice(strPrice):
	return str(strPrice).replace(',', '').replace('원', '')

def parse(type, pageString):
	bsObj = htmlParser(pageString)
	if type == 'tmon':
		return tmonUtil.tmonParser(bsObj)
