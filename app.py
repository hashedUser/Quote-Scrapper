from selenium import webdriver

from pages.quotes_page import QuotesPage

chrome = webdriver.Chrome(executable_path="C:/Users/Aditya Kulkarni/Documents/chromedriver/chromedriver.exe")
# get the content from the entire quotes page
chrome.get('https://quotes.toscrape.com/search.aspx')

# QuotesPage executed for parsing the page using bs4
page = QuotesPage(chrome)  # Parse using beautifulsoup

author = input("Enter the author you'd' like quotes from: ")
page.select_author(author)

tags = page.get_available_tags()
print("Select one of these [{}]".format(" | ".join(tags)))
selected_tag = input("Enter your tag: ")
page.select_tag(selected_tag)
page.search_button.click()
print(page.quotes)

