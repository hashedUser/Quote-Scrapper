from selenium import webdriver
from pages.quotes_page import QuotesPage, InvalidTagForAuthorError

try:
    author = input("Enter the author you'd' like quotes from: ")
    tag = input("Enter your tag: ")

    chrome = webdriver.Chrome(executable_path="/chromedriver/path")
    chrome.get('https://quotes.toscrape.com/search.aspx')
    page = QuotesPage(chrome)  # Parse using beautifulsoup
    print(page.search_for_quotes(author, tag))
except InvalidTagForAuthorError as e:
    print(e)
except Exception as e:
    print(e)
    print("An unknown error occurred. Please try again.")



