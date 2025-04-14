import requests
from bs4 import BeautifulSoup
import creds
from openai import OpenAI

url = input("Paste wiki url> ")
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")
text = ""

article = soup.find_all("div", {"class": "mw-parser-output"})
for articles in article:
    content = articles.find_all("p")
    for p in content:
        text += p.text

client = OpenAI(
    api_key=creds.openai,
    organization=creds.orgid
)

prompt = f"Summarize the text below in no more than 3 paragraphs:\n\n{text}"

try:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0,
        max_tokens=30
    )
    summary = response.choices[0].message.content
    print("\n📄 Summary:\n", summary)

except Exception as e:
    print("\n❌ OpenAI API Error:", e)
    summary = None

print("\n🔗 References:")

refs = soup.find_all("ol", {"class": "references"})
count = 0
for ref in refs:
    count += 1
    print(ref.text.replace("^ ", ""))
    if count > 5:
        break