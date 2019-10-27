import datetime
import pandas as pd
# import openpyxl
import os.path

def getRootPath():
	return '/Users/guseonmo/Documents/study/python/doobari/'

def getDataFrame(result):
	return pd.DataFrame(data=result)

def complateFileName(fileName):
	dt = datetime.datetime.now()
	dt.strftime('%Y-%m-%d')

	filePath = getRootPath()+"data/{}_{}"
	return filePath.format(dt.strftime('%Y-%m-%d'), fileName)

# csv
def saveCsv(result, fileName):
	df = getDataFrame(result)
	fileName = complateFileName(fileName) + '.csv'
	# print(fileName)
	if os.path.isfile(fileName):
		df.to_csv(fileName, mode='a', header=None)
	else:
		df.to_csv(fileName, mode='a')

def saveExcel(result, fileName):
	df = getDataFrame(result)
	complateFileName(fileName) + '.xsls'
	writer = pd.ExcelWriter(fileName)
	df.to_excel(writer, 'Sheet2')
	writer.save()

def test(fileName):
	if os.path.isfile(fileName):
		print("Yes. it is a file")
	else:
		print("No. it is not file")

def getKeywords():
	keywords = []
	# f = open('../keywords.txt', 'r')

	f = open(getRootPath()+'keywords.txt', 'r')
	while True:
		line = f.readline()
		if not line:
			break

		keywords.append(line.strip())
	f.close()
	return keywords
