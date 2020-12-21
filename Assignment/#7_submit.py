import requests
from bs4 import BeautifulSoup
import numpy as np

url = "http://www.alba.co.kr/"
i = 0
test_url = "http://handmadepizza.alba.co.kr/"


def extract_brand():
    brand_link_list = []
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    super_brands = soup.find("div", {"id": "MainSuperBrand"}).find(
        "ul", {"class": "goodsBox"}).find_all("li")
    super_brands = super_brands[:-1]

    for brands in super_brands:
        brand_link = brands.find("a")["href"]
        brand_link_list.append(brand_link)
    return brand_link_list


def extract_pages(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("span")
    print(pagination)


extract_pages(test_url)
