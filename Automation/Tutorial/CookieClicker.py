from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.get("https://orteil.dashnet.org/cookieclicker/")

WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='langSelect-EN']")))
driver.find_element(By.XPATH, "//*[@id='langSelect-EN']").click()

time.sleep(5)
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "bigCookie")))
cookie = driver.find_element(By.ID, "bigCookie")
cookie.click()

productPrice_prefix = "productPrice"
product_prefix = "product"

while True:
    cookie.click()
    cookies_count = driver.find_element(By.ID, "cookies").text.split(" ")[0]
    cookies_count = int(cookies_count.replace(",", ""))
    for i in range(6):
        product_price = driver.find_element(By.ID, productPrice_prefix + str(i)).text.replace(",", "")
        if not product_price.isdigit():
            continue
        product_price = int(product_price)
        if product_price <= cookies_count:
            driver.find_element(By.ID, product_prefix + str(i)).click()
            break
