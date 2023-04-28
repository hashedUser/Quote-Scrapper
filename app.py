from selenium import webdriver

from pages.quotes_page import QuotesPage

chrome = webdriver.Chrome(executable_path="C:/Users/Aditya Kulkarni/Documents/chromedriver/chromedriver.exe")
# get the content from the entire quotes page
chrome.get('https://quotes.toscrape.com/search.aspx')

# QuotesPage executed for parsing the page using bs4
page = QuotesPage(chrome)  # Parse using beautifulsoup

for quote in page.quotes:
    print(quote)
