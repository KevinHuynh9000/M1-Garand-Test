from selenium import webdriver
import os
import time
import sys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from selenium.webdriver import ActionChains

options = Options()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)


driver.get('http://usriflecal30m1.com/Default.aspx')
time.sleep(2)
pro = driver.find_element_by_link_text('Production').click()
driver.execute_script("window.scrollTo(0,100)")
time.sleep(3)
driver.execute_script("window.scrollTo(0,700)")
time.sleep(3)
driver.execute_script("window.scrollTo(0,1100)")
time.sleep(3)

time.sleep(2)

com = driver.find_element_by_link_text('My Garand')
hover = ActionChains(driver).move_to_element(com)
hover.perform()
time.sleep(1)
com2= driver.get('http://usriflecal30m1.com/Parts/PartsList.aspx')

serial = driver.find_element_by_xpath("//*[@id='ctl00_cphBody_txtSerialBegin']")
time.sleep(2)
serial.send_keys("5746876")
time.sleep(1.5)
driver.find_element_by_xpath("//*[@id='cphBody_ddlMFG']/option[text()='Harrington & Richardson Arms Company']").click()
time.sleep(1.5)
driver.find_element_by_xpath("//*[@id='cphBody_lbtnSave']").click()
time.sleep(2)
driver.execute_script("window.scrollTo(0,600)")
time.sleep(2)
driver.execute_script("window.scrollTo(0,1200)")
time.sleep(2)
driver.execute_script("window.scrollTo(0,1800)")
time.sleep(2)
driver.get('https://www.youtube.com/watch?v=9QeKsXTPAPw')

