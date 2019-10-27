f = open('keywords.txt', 'r')
while True:
	line = f.readline()
	if not line:
		break

	print('ㅁ', line)

f.close()
#
#
# # url = 'http://www.tmon.co.kr/deal/2582161742?keyword=자가점착+밴드&tl_area=SALDEAL&tl_ord=16&searchClick=DL%7CND%7COMM&thr=ts'
# #  2
# # url = 'http://www.tmon.co.kr/deal/1806448034?keyword=%EC%9E%90%EA%B0%80%EC%A0%90%EC%B0%A9+%EB%B0%B4%EB%93%9C&tl_area=SALDEAL&tl_ord=6&searchClick=DL%7CND%7COMM&thr=ts'
# # 3
# url = 'http://www.tmon.co.kr/deal/2582161742?keyword=%EC%9E%90%EA%B0%80%EC%A0%90%EC%B0%A9+%EB%B0%B4%EB%93%9C&tl_area=SALDEAL&tl_ord=16&searchClick=DL%7CND%7COMM&thr=ts'
#
# driver = comm.getDriver()
# driver.get(url)
#
# lev1 = driver.find_elements_by_xpath('//*[@id="_optionScroll"]/div/div/div/div[1]/ul/li')
# lev2 = driver.find_elements_by_xpath('//*[@id="_optionScroll"]/div/div/div/div[2]/ul/li')
# lev3 = driver.find_elements_by_xpath('//*[@id="_optionScroll"]/div/div/div/div[3]/ul/li')
#
# print(lev1)
# print(lev2)
# print(lev3)
#
# # 1 - select box가 몇개인지 파악
# div = driver.find_element_by_xpath('//*[@id="_optionScroll"]/div/div/div')
# detailDiv = div.find_elements_by_tag_name('div')
# detailDivCnt = len(detailDiv)
# print(detailDivCnt)
#
# sleep(0.3)
#
# def getResult(detailDiv):
# 	divCnt = len(detailDiv)
# 	div1 = detailDiv[0]
# 	div1.find_element_by_tag_name('button').click()
# 	ul = div1.find_element_by_tag_name('ul')
# 	lis = ul.find_elements_by_tag_name('li')
#
# 	for li in lis:
# 		# 첫번째 select box 선택하
# 		li.find_element_by_tag_name('button').click()
# 		sleep(0.3)
#
# 		div2 = detailDiv[1]
# 		div2_ul = div2.find_element_by_tag_name('ul')
# 		div2_lis = div2_ul.find_elements_by_tag_name('li')
#
# 		for div2_li in div2_lis:
#
# 			if divCnt == 2:
# 				div2_spans = div2_li.find_elements_by_tag_name('span')
# 				print(div2_spans[0].text, div2_spans[1].text)
#
# 			elif divCnt == 3:
# 				div2_li.find_element_by_tag_name('button').click()
# 				sleep(0.3)
#
# 				div3 = detailDiv[2]
# 				div3_ul = div3.find_element_by_tag_name('ul')
# 				div3_lis = div3_ul.find_elements_by_tag_name('li')
#
# 				for div3_li in div3_lis:
# 					div3_spans = div3_li.find_elements_by_tag_name('span')
# 					print(div3_spans[0].text, div3_spans[1].text)
#
#
#
#
# getResult(detailDiv)
#
# # for i in range(0, detailDivCnt):
# # 	selectDiv = detailDiv[i]
# # 	selectDiv.find_element_by_tag_name('button').click()
# # 	ul = selectDiv.find_element_by_tag_name('ul')
# # 	lis = ul.find_elements_by_tag_name('li')
# # 	for li in lis:
# # 		li.find_element_by_tag_name('button').click()
#
#
# # selectDiv.find_element_by_xpath('//*[@id="_optionScroll"]/div/div/div/div[1]/button').click()
# # print(li)
#
# # //*[@id="_optionScroll"]/div/div/div
# # //*[@id="_optionScroll"]/div/div/div/div[1]®
# # //*[@id="_optionScroll"]/div/div/div/div[2]
#
#
# #  sel1 - selectbox 열기
# # driver.find_element_by_xpath('//*[@id="_optionScroll"]/div/div/div/div[1]/button').click()
# # #  select box 선택
# # driver.find_element_by_xpath('//*[@id="_optionScroll"]/div/div/div/div[1]/ul/li/button').click()
# #
# # # sel2
# # lis = driver.find_elements_by_xpath('//*[@id="_optionScroll"]/div/div/div/div[2]/ul/li')
#
# # for li in lis:
# # 	print(li.page_source)
#
# print(url)
#
# # driver.close()
# # driver.find_element_by_xpath('//*[@id="_optionScroll"]/div/div/div/div[1]/ul/li[1]/button').click()
# # driver.find_element_by_xpath('//*[@id="_optionScroll"]/div/div/div/div[1]/ul/li/button').click()
#
# # //*[@id="_optionScroll"]/div/div/div/div[1]/ul/li
# # //*[@id="_optionScroll"]/div/div/div/div[1]/ul/li/button
#
#
# #  [] 에러가 아니면 element가 있다고 판단.
# # //*[@id="_optionScroll"]/div/div/div/div[2]/ul/li[1]
# # //*[@id="_optionScroll"]/div/div/div/div[2]/ul/li[2]
# # //*[@id="_optionScroll"]/div/div/div/div[2]/ul/li/button
# #
# # //*[@id="_optionScroll"]/div/div/div/div[1]/ul/li
# # //*[@id="_optionScroll"]/div/div/div/div[2]/ul/li
# # //*[@id="_optionScroll"]/div/div/div/div[3]/ul/li
# # //*[@id="_optionScroll"]/div/div/div/div[3]/ul/li/button
