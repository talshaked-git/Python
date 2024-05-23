import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Taking input from user
search_string = input("Input the URL or string you want to search for:")

# This is done to structure the string
# into search url.(This can be ignored)
search_string = search_string.replace(' ', '+')

options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)
browser = webdriver.Edge(options=options)

for i in range(1):
    matched_elements = browser.get("https://www.google.com/search?q=" +
                                   search_string + "&start=" + str(i))
    
    # Wait until the title contains the search string, indicating that the page has loaded
    WebDriverWait(browser, 10).until(EC.title_contains(search_string))

####
# To keep the browser open, comment out the following line
# options = webdriver.EdgeOptions()
# options.add_experimental_option("detach", True)
# browser = webdriver.Edge(options=options)