import requests

r = requests.get("http://hn.algolia.com/api/v1/search_by_date?tags=story")
print(type(r.json()))
