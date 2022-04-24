from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from constants import BASE_URL_SEARCH

base_url = BASE_URL_SEARCH

class MilHomeSearchPage:
  URL = base_url

  SEARCH_BUTTON = (By.CLASS_NAME, 'btn.search-news-button')
  SEARCH_INPUT = (By.CLASS_NAME, 'search-field')

  def __init__(self, browser):
    self.browser = browser

  def load(self):
    self.browser.get(self.URL)

  def search(self, phrase):
    search_button = self.browser.find_element(*self.SEARCH_BUTTON)
    search_button.click()
    search_input = self.browser.find_element(*self.SEARCH_INPUT)
    search_input.send_keys(phrase + Keys.RETURN)
