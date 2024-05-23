from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()

driver.get("https://www.google.com")

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "gLFyf")))

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.clear()
input_element.send_keys("speedtest" + Keys.ENTER)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Speedtest by Ookla")))

link = driver.find_element(By.PARTIAL_LINK_TEXT, "Speedtest by Ookla")
link.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Go")))

link = driver.find_element(By.PARTIAL_LINK_TEXT, "Go")
link.click()
time.sleep(60)
#click on the search bar by using Xpath
# search_bar = driver.find_element("xpath", '//*[@id="APjFqb"]').click()

time.sleep(10)
