'''
python selenium basic lesson 1:
open google.com and search something
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os
import time

wd = os.getcwd()
wbd = os.path.join(wd, "chromedriver.exe")

#open chromedriver.exe before python script
driver = webdriver.Chrome(os.path.join(wd, "chromedriver.exe"))
driver.get("http://www.google.com")

element = driver.find_element_by_class_name("gLFyf.gsfi")
element.send_keys("selenium python")
element.send_keys(Keys.ENTER)

# button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "btnK")))
# button.click()

driver.back() #previous page
driver.forward()

htmltext = driver.page_source
driver.close()
