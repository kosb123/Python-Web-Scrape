import requests

r = requests.get("https://hn.algolia.com/api/v1/search")
r.json()
print(r)
