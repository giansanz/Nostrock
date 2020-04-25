import re
import requests
from bs4 import BeautifulSoup

def stocktwit(stock):
    source = requests.get('https://stocktwits.com/symbol/' + stock)
    soup = BeautifulSoup(source.text, 'html.parser')
    sentiment = re.search(r'(\"sentimentChange\":).{6}', str(soup))
    sentiment = sentiment.group()
    sentiment = sentiment.replace("\"sentimentChange\":", '')
    sentiment = sentiment.replace(",", '')
    sentiment = sentiment.replace("\"", '')
    return sentiment


