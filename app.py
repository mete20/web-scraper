import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    response = requests.get("http://quotes.toscrape.com")
    soup = BeautifulSoup(response.text, 'lxml')

    quotes = soup.find_all('div', class_='quote')
    for quote in quotes:
        text = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text
        print(f'"{text}" - {author}\n')

if __name__ == "__main__":
    scrape_quotes()
