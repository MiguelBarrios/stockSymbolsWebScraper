from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

fileName = 'htmls/{letter}.html'

f = open('symbols.txt', 'a')

symbols = "ABCDEFGHIJKLMNOPQUSTUVWXYZ+"

for symbol in symbols:
	file = fileName.format(letter = symbol)
	raw_html = open(file).read()
	soup = BeautifulSoup(raw_html, 'html.parser')
	content = soup.find_all("table", {"class", "market tab1"})
	rows = content[0].find_all("tr")
	for i in range(2,len(rows)):
		td = rows[i].find_all("td")
		symbol = td[1].getText()
		if len(symbol) != 0:
			f.write(symbol)
			f.write("\n")
f.close()





