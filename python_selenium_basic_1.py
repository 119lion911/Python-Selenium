'''
python selenium basic lesson 1:
open google.com and search something
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

wd = os.getcwd()
wbd = os.path.join(wd, "chromedriver.exe")

#open chromedriver.exe before python script
driver = webdriver.Chrome(os.path.join(wd, "chromedriver.exe"))
driver.get("http://www.google.com")

element = driver.find_element_by_class_name("gLFyf.gsfi")
element.send_keys("selenium python")
element.send_keys(Keys.ENTER)
# element.clear()

# button =driver.find_element_by_class_name("gNO89b")
# button.click()

driver.back() #previous page
driver.forward()

driver.close()