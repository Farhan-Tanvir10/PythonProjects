from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

data_dir = "C:\\Users\\97450\\PythonProjects\\P10\\data"
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

driver = webdriver.Chrome()
query = "Lighting_Cases"  
file = 0


for i in range(0, 30, 10): 
    url = f"https://www.wexphotovideo.com/search/?q=Lighting+Cases&rows=10&start={i}&search_type=All"
    driver.get(url)
    time.sleep(5)  
    
    selectors = [
        ".product-tile",          
        ".unbxd-grid-product",     
        ".item",                  
        "[data-component-type='product']", 
        ".product-container"      
    ]
    
    elems = []
    for selector in selectors:
        elems = driver.find_elements(By.CSS_SELECTOR, selector)
        if len(elems) > 0:
            print(f"Found {len(elems)} items with selector: {selector}")
            break
    
    if len(elems) == 0:
        print("No product elements found with any of the known selectors.")
        elems = driver.find_elements(By.CSS_SELECTOR, "[class*='product']")
        print(f"Found {len(elems)} items with fallback selector containing 'product'")
    
    for elem in elems:
        d = elem.get_attribute("outerHTML")
        file_path = os.path.join(data_dir, f"{query}_{file}.html")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(d)
            print(f"Saved item {file} to {file_path}")
            file += 1
    
    print(f"Completed page {i//10 + 1}")
    time.sleep(3)  

driver.close()
print("Scraping completed successfully!")