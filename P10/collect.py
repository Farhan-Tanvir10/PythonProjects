import os
from bs4 import BeautifulSoup
import pandas as pd

d = {"title": [], "price": [], "link": []}  
for file in os.listdir("data"):
    try:
        with open(f"data/{file}", encoding="utf-8") as f:  
            html_doc = f.read()
            soup = BeautifulSoup(html_doc, "html.parser")

        t = soup.find("h3", class_="-title") 
        title = t.get_text(strip=True)

        l = t.parent  
        link = l["href"] if l.name == "a" else "No link found"
        full_link = f"https://www.wexphotovideo.com{link}" if link != "No link found" else "No link found"  # added full URL

        price_tag = soup.find("span", class_="--price wex-red") 
        price = price_tag.get_text(strip=True) if price_tag else "No price found"
        d["title"].append(title)
        d["price"].append(price)
        d["link"].append(link)
    except Exception as e:
        print(e)

df = pd.DataFrame(data=d)
df.to_csv("data.csv")