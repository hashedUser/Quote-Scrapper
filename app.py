from selenium import webdriver
from pages.quotes_page import QuotesPage

author = input("Enter the author you'd' like quotes from: ")
tag = input("Enter your tag: ")

chrome = webdriver.Chrome(executable_path="C:/Users/Aditya Kulkarni/Documents/chromedriver/chromedriver.exe")
chrome.get('https://quotes.toscrape.com/search.aspx')
page = QuotesPage(chrome)  # Parse using beautifulsoup
print(page.search_for_quotes(author, tag))


