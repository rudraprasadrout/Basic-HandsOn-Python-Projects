#  News app using API and python

import requests

query  = input("What type of news are you interested today ? : ")
api = " Use Your api"

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-07-26&sortBy=publishedAt&apiKey={api}"
print(url)

r = requests.get(url)
data = r.json()

articles = data["articles"]
for index,article in enumerate(articles):
    print(index+1, article["title"],article["url"])
    print("\n *************************************************************** \n")
