import requests
from bs4 import BeautifulSoup

url = 'http://hochicken.alba.co.kr/job/brand/'
result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")
jobs = soup.find("tbody").find_all("tr")
# for job in jobs:
job = jobs[0]
print(job['id'])
