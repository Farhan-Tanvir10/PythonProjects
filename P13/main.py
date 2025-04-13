import os, requests, json, datetime
from openai import OpenAI
import creds

client = OpenAI(
    api_key=creds.openai,
    organization=creds.orgid
)

topic = "Apple"  

today = datetime.datetime.now()
week_ago = today - datetime.timedelta(days=1)
from_date = week_ago.strftime("%Y-%m-%d")

url = f"https://newsapi.org/v2/everything?q={topic}&from={from_date}&sortBy=popularity&apiKey={creds.api_key}"

result = requests.get(url)
data = result.json()

counter = 0
for article in data["articles"]:
    counter += 1
    if counter > 5:
        break
    
    print(f"\nArticle {counter}: {article['title']}")
    print(f"URL: {article['url']}")
    
    prompt = (f"""Summarize the following news article in one sentence:
Title: {article['title']}
Description: {article.get('description', 'No description available')}""")
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o",  
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0,
            max_tokens=20  
        )
        
        print("Summary:")
        print(response.choices[0].message.content)
    except Exception as e:
        print(f"Error with OpenAI: {e}")

    print()