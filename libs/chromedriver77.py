from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import crawl.libs.fileUtil as fileUtil
def getDriver():
	rootPath = "."
	chrome_option = Options()

	rootPath = fileUtil.getRootPath()
	driver = webdriver.Chrome(
		executable_path=rootPath+'crawl/webDriver/chromedriver77',
		options=chrome_option
	)
	return driver
