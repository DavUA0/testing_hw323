from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from constants import BASE_URL_GS

base_url = BASE_URL_GS

class GeneralStaffPage:
  URL = base_url

  GS_CHIEF_DIV = (By.XPATH, "//*[contains(text(), 'FIRST DEPUTY CHIEF OF ARMED FORCES GENERAL STAFF')]/..")
  ANCHORS= (By.TAG_NAME, 'a')

  def __init__(self, browser):
    self.browser = browser

  def load(self):
    self.browser.get(self.URL)

  def get_gs_chief(self):
    gs_chief_div = self.browser.find_elements(GS_CHIEF_DIV)
    return gs_chief_div[0].find_elements(ANCHORS)[0].text
