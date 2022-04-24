from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from home_search import MilHomeSearchPage

serv = Service('./chromedriver')
driver = webdriver.Chrome(service=serv)

PHRASE = 'test'

search_page = MilHomeSearchPage(driver)
search_page.load()
search_page.search(PHRASE)
