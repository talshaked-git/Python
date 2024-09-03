from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import re
import tkinter as tk
from tkinter import messagebox

# Function to convert price text to numerical value
def parse_price(price_text):
    try:
        # Remove any characters (except numbers and the decimal point)
        price_text = re.sub(r'[^\d.]', '', price_text)
        return float(price_text) if price_text else None
    except ValueError:
        return None

def start_scraping():
    global min_price, max_price, search_term
    
    try:
        min_price = float(min_price_entry.get())
        max_price = float(max_price_entry.get())
        search_term = search_term_entry.get().strip()
        
        if min_price < 0 or max_price < 0:
            raise ValueError("Prices must be non-negative")
        if min_price > max_price:
            raise ValueError("Minimum price cannot be greater than maximum price")
        if not search_term:
            raise ValueError("Search term cannot be empty")
        
    except ValueError as e:
        messagebox.showerror("Input Error", f"Invalid input: {e}")
        return
    
    # Close the Tkinter window
    root.destroy()

    # Selenium scraping part
    driver = webdriver.Chrome()
    driver.get('https://www.ebay.com/')

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'gh-ac'))
        )
        search_box = driver.find_element(By.ID, 'gh-ac')
        search_box.send_keys(search_term)
        search_button = driver.find_element(By.ID, 'gh-btn')
        search_button.click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 's-item'))
        )

        items = driver.find_elements(By.CLASS_NAME, 's-item')
        data = []

        for item in items:
            try:
                title = item.find_element(By.CLASS_NAME, 's-item__title').text
                price_text = item.find_element(By.CLASS_NAME, 's-item__price').text
                price = parse_price(price_text)
                link = item.find_element(By.CLASS_NAME, 's-item__link').get_attribute('href')

                if price is not None and min_price <= price <= max_price:
                    data.append({'Title': title, 'Price': price_text, 'Link': link})
            except:
                continue

        df = pd.DataFrame(data)
        df.to_csv(f'ebay_{search_term}_filtered.csv', index=False)
        print(f"Data has been saved to 'ebay_{search_term}_filtered.csv'")

    finally:
        driver.quit()

root = tk.Tk()
root.title("eBay Scraper")

# Create and place widgets
tk.Label(root, text="Search Term:").grid(row=0, column=0, padx=10, pady=10)
search_term_entry = tk.Entry(root)
search_term_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Min Price:").grid(row=1, column=0, padx=10, pady=10)
min_price_entry = tk.Entry(root)
min_price_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Max Price:").grid(row=2, column=0, padx=10, pady=10)
max_price_entry = tk.Entry(root)
max_price_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Button(root, text="Start Scraping", command=start_scraping).grid(row=3, column=0, columnspan=2, pady=20)

root.mainloop()
