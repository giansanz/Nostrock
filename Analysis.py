from textblob import TextBlob
from bs4 import BeautifulSoup
import requests
from sys import argv


class Analysis:
	def __init__(self, term):
		self.term = term
		self.sentiment = 0
		self.subjectivity = 0
		self.url = 'https://www.google.com/search?q={0}&source=lnms&tbm=nws'.format(self.term)

	def pages(self):
		response = requests.get(self.url)
		soup = BeautifulSoup(response.text, 'html.parser')
		headline_results = soup.find_all('div', class_='kCrYT')
		list_sites = []
		for links in headline_results:
			link = links.find('a')['href']
			site = link.strip('/url?q=')
			head, sep, tail = site.partition('&')
			list_sites.append(head)

		for pages in range(2):
			response = requests.get(list_sites[pages])
			soup = BeautifulSoup(response.text, 'html.parser')
			info = soup.find_all('p')
			for information in info:
				blob = TextBlob(information.get_text())
				self.sentiment += blob.sentiment.polarity / len(info)
				self.subjectivity += blob.sentiment.subjectivity / len(info)
				


						   
a = Analysis(argv[1])
print a.term, 'Subjectivity: ', a.subjectivity, 'Sentiment: ', a.sentiment

