import requests
from bs4 import BeautifulSoup

url = "https://www.wexphotovideo.com/digital-cameras/?p=categoryPath%3A%22cameras%22&rows=12&start=0"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")

myLinks = soup.find_all("a", {"class": "wex-text"})
print(len(myLinks))

counter = 0
for link in myLinks:
    counter += 1
    if counter > 5:
        break
    print(link.text.strip())
    href = link["href"]
    full_url = f"https://www.wexphotovideo.com{href}?p=categoryPath%3A%22cameras%22&rows=12&start=0"
    print(full_url)