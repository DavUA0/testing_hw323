from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from ministry import MinistryPage

serv = Service('./chromedriver')
driver = webdriver.Chrome(service=serv)

ministry_page = MinistryPage(driver)
ministry_page.load()
name = ministry_page.get_minister()
assert name == 'Suren Papikyan'
