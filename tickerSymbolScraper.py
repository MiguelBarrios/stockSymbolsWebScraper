import requests
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from tqdm import tqdm

def saveSymbolsByExchange(exchange, outputFileName):
	exchange = exchange.lower()
	exchanges = {
	"nyse":'https://www.advfn.com/nyse/newyorkstockexchange.asp?companies={letter}',
	"nasdaq": "https://www.advfn.com/nasdaq/nasdaq.asp?companies={letter}",
	"amex": "https://www.advfn.com/amex/americanstockexchange.asp?companies={letter}"}

	url = exchanges.get(exchange)
	f = open(outputFileName, 'a')

	symbols = "ABCDEFGHIJKLMNOPQUSTUVWXYZ+"
	for c in tqdm(symbols):
		curUrl = url.format(letter = c)
		data = requests.get(curUrl)
		raw_html = data.text
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

saveSymbolsByExchange("nasdaq", "nasdaq.txt")
saveSymbolsByExchange("nyse", "nyse.txt")