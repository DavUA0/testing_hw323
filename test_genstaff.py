from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from gen_staff import GeneralStaffPage

serv = Service('./chromedriver')
driver = webdriver.Chrome(service=serv)

genstaff_page = GeneralStaffPage(driver)
genstaff_page.load()
name = genstaff_page.get_gs_chief()
assert name == 'Kamo'
