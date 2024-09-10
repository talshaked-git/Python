from selenium import webdriver
import spacy
from bs4 import BeautifulSoup

# Function to extract and save HTML
def collect_html(url, filename):
    driver = webdriver.Chrome()
    driver.get(url)
    
    # Get the page's raw HTML
    page_html = driver.page_source
    
    # Save the HTML to a file
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(page_html)
    
    print(f"HTML data saved to {filename}")
    driver.quit()

# Example usage for collecting HTML
urls = [
    'https://www.amazon.com/iphone/s?k=iphone',
    'https://www.ebay.com/sch/i.html?_nkw=iphone',
    'https://www.aliexpress.com/wholesale?SearchText=iphone'
]

for idx, url in enumerate(urls):
    collect_html(url, f'./sample_html_{idx}.html')


# Load a pre-trained NLP model (spaCy)
nlp = spacy.load('en_core_web_sm')

# Function to extract text elements from HTML
def extract_text_from_html(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        
        # Extract all text from the HTML
        raw_text = soup.get_text(separator=' ')
        return raw_text

# Apply NLP on the extracted text
def extract_entities(text):
    doc = nlp(text)
    for ent in doc.ents:
        print(ent.text, ent.label_)

# Example usage
html_text = extract_text_from_html('sample_html_0.html')
extract_entities(html_text)
