import crawl.libs.common as comm
import crawl.libs.fileUtil as comFile

def main():
	type = comm.getSiteUrl()
	keywords = comFile.getKeywords()

	result = []
	for keyword in keywords:
		for i in range(1, 2):
			pageString = comm.crawl(type['tmon'], keyword, i)
			result = result + comm.parse('tmon', pageString)

	# pageString = comm.seleniumCrawlForScrollPaging(type['tmon'], keyword)
	comFile.saveCsv(result, 'tmon')

if __name__ == "__main__":
	main()

