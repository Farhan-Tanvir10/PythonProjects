import os, requests, json, datetime
import creds

topic = "Apple"  


today = datetime.datetime.now()
week_ago = today - datetime.timedelta(days=1)
from_date = week_ago.strftime("%Y-%m-%d")


url = f"https://newsapi.org/v2/everything?q={topic}&from={from_date}&sortBy=popularity&apiKey={creds.api_key}"

result = requests.get(url)
data = result.json()

print(f"Request URL: {url}")
print(f"Response Status: {data.get('status')}")

if "articles" not in data or not data["articles"]:
    print("No articles found. Try a different topic or date range.")
    exit()

print(f"\n=== TOP NEWS ABOUT '{topic.upper()}' ===\n")

counter = 0
for article in data["articles"]:
    counter += 1
    if counter > 10:  
        break
    
    print(f"ARTICLE {counter}: {article['title']}")
    print(f"SOURCE: {article['source']['name']}")
    print(f"PUBLISHED: {article['publishedAt']}")
    print(f"URL: {article['url']}")
    
    description = article.get('description', 'No description available')
    print(f"DESCRIPTION: {description}")
    
    print()