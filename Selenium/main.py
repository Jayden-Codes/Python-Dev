import os
from selenium import webdriver
os.environ['PATH'] += r"C:/Users/Jayden/Code/Python-Dev/Selenium/"

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://www.youtube.com/channel/UC9VIE4nX3fDPPeic0MX0aeQ")
about = driver.find_element_by_css_selector("Playlists")
about.click()

