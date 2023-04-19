import requests

from pages.quotes_page import QuotesPage

page_content = requests.get('https://qutoes.toscrape.com').content
page = QuotesPage(page_content)

for quote in page.quotes:
    print(quote)