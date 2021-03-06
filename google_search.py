from textblob import TextBlob
from bs4 import BeautifulSoup
import requests
from datetime import date
import re

today = str(date.today())

def googlesearch(news):
	url = 'https://www.google.com/search?q={0}&source=lnms&tbm=nws'.format(news)
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')
	headline_results = soup.find_all('div', class_='kCrYT')
	list_sites = []
	try:
		for links in headline_results:
			website = links.find('a')['href']
			site = website.strip('/url?q=')
			head, sep, tail = site.partition('&')
			list_sites.append(head)
	except:
		pass
		
	list_sites = list(dict.fromkeys(list_sites))
	latest_news = []
	sentiment = 0
	subjectivity = 0

	for pages in range(len(list_sites)):
		response = requests.get(list_sites[pages])
		soup = BeautifulSoup(response.text, 'html.parser')
		info = soup.find_all('meta')
		today = str(date.today())
		search = re.findall(today, str(info))

		if len(search) > 0:
			latest_news.append(list_sites[pages])
			info = soup.find_all('p')
			for findings in info:
				blob = TextBlob(findings.get_text())
				sentiment += blob.sentiment.polarity / len(info)
				subjectivity += blob.sentiment.subjectivity / len(info)

	
	return sentiment / len(latest_news), subjectivity / len(latest_news), latest_news


