import bs4
import requests
from bs4 import BeautifulSoup

def stock_watch(stock):
    source = requests.get('http://money.cnn.com/quote/quote.html?symb=' + stock)
    soup = BeautifulSoup(source.text, 'html.parser')
    container = soup.find('td', class_='wsod_last')
    return container.find("span", {'streamformat':'ToHundredth'}).text



