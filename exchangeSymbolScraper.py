import requests
from bs4 import BeautifulSoup

exchanges = ["nyse", "nasdaq"]

urls = ['https://www.advfn.com/nyse/newyorkstockexchange.asp?companies={letter}',
		"https://www.advfn.com/nasdaq/nasdaq.asp?companies={letter}"]

for i in range(0,2):
	print(i)
	fileName = "htmls/{exchange}/{letter}.html"
	symbols = "ABCDEFGHIJKLMNOPQUSTUVWXYZ+"

	for c in symbols:
		curUrl = urls[i].format(letter = c)
		curFile = fileName.format(exchange = exchanges[i],letter = c)
		print(curUrl)
		data = requests.get(curUrl)
		html = data.text
		file = open(curFile, 'w')
		file.write(html)
		file.close()
