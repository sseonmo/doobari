import json
import crawl.libs.common as comm
from datetime import datetime
from time import sleep

# tmon parser
def tmonParser(bsObj):
	type = 'tmon'
	itemList = []
	collectTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

	jsonStr = json.loads(bsObj.text)
	searchDeals = jsonStr['data']['searchDeals']

	driver = comm.getDriver()

	for searchDeal in searchDeals:
		detailUrl = searchDeal['extraDealInfo']['detailUrl']
		pageTitle = ''
		pageStr = ''
		driver.get(detailUrl)

		# select box 갯수 파악
		div = driver.find_element_by_xpath('//*[@id="_optionScroll"]/div/div/div')
		detailDiv = div.find_elements_by_tag_name('div')

		pageTitle = driver.find_element_by_xpath(
			'//*[@id="view-default-scene-default"]/section[1]/div[3]/div[2]/h1').text

		if len(detailDiv) > 1:
			itemList = itemList + parseFormutilSelectBox(detailDiv, collectTime, pageTitle, detailUrl)
		else:
			try:
				sleep(1)
				pageStr = driver.page_source
			except Exception as ex:
				print('selenium crawl error', ex)

			#  참이 아니면 continue
			if not pageStr:
				continue

			bsObj = comm.htmlParser(pageStr)

			try:
				# select box 한개 인거
				ul = bsObj.find('ul', {'class': 'purchase_selector'})
				buttons = ul.findAll('button')

				for button in buttons:
					spans = button.findAll('span')
					item = dict(collectTime=collectTime, title=pageTitle,
					            item=spans[0].text, price=comm.convertPrice(spans[1].text), link=detailUrl)
					itemList.append(item)
			except AttributeError as ae:
				# select box가 없는거
				print('No select box : use chrome driver', ae)
				itemName = driver.find_element_by_xpath('//*[@id="_optionScroll"]/div/ul[1]/li/span[1]/span[1]').text
				price = driver.find_element_by_xpath(
					'//*[@id="_optionScroll"]/div/ul[1]/li/div/div[1]/div/div/span/strong').text
				itemList.append(
					dict(collectTime=collectTime, title=pageTitle, item=str(itemName), price=comm.convertPrice(price), link=detailUrl)
				)
			except Exception as ex:
				print('Exception', ex)
	# break

	driver.close()
	return itemList

def parseFormutilSelectBox(detailDiv, collectTime, pageTitle, detailUrl):
	itemList = []
	divCnt = len(detailDiv)
	div1 = detailDiv[0]
	ul = div1.find_element_by_tag_name('ul')
	lis = ul.find_elements_by_tag_name('li')

	for li in lis:
		try:
			# 첫번째 select box 선택하
			sleep(1)
			div1.find_element_by_tag_name('button').click()
			try:
				li.find_element_by_tag_name('button').click()
			except Exception as ex:
				print(ex)
			sleep(1)

			div2 = detailDiv[1]
			div2_ul = div2.find_element_by_tag_name('ul')
			div2_lis = div2_ul.find_elements_by_tag_name('li')

			for div2_li in div2_lis:

				if divCnt == 2:
					div2_spans = div2_li.find_elements_by_tag_name('span')
					itemList.append(
						dict(collectTime=collectTime, title=pageTitle, item=str(div2_spans[0].text),
						     price=comm.convertPrice(div2_spans[1].text), link=detailUrl)
					)

				elif divCnt == 3:
					div2_li.find_element_by_tag_name('button').click()
					sleep(1)

					div3 = detailDiv[2]
					div3_ul = div3.find_element_by_tag_name('ul')
					div3_lis = div3_ul.find_elements_by_tag_name('li')

					for div3_li in div3_lis:
						div3_spans = div3_li.find_elements_by_tag_name('span')
						itemList.append(
							dict(collectTime=collectTime, title=pageTitle, item=str(div3_spans[0].text),
							     price=comm.convertPrice(div3_spans[1].text), link=detailUrl)
						)
		except Exception as ex:
			continue

	return itemList
