from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from constants import BASE_URL_MINISTRY

base_url = BASE_URL_MINISTRY

class MinistryPage:
  URL = base_url

  MINISTER_PRGRPH = (By.CLASS_NAME, "name")

  def __init__(self, browser):
    self.browser = browser

  def load(self):
    self.browser.get(self.URL)

  def get_minister(self):
    return self.browser.find_element(*MINISTER_PRGRPH).text
