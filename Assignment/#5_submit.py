import os
import requests
from bs4 import BeautifulSoup

url = "https://www.iban.com/currency-codes"

country_list = []


def ask_code():
    try:
        answer = int(input("#: "))
        if answer < 0 or answer > 264:
            print('Choose a number from the list.')
            ask_code()
        else:
            choose_country = country_list[answer]
            name = list(choose_country.keys())[0]
            code = list(choose_country.values())[0]
            print(f"You chose {name} \nThe currency code is {code}")
    except:
        print("That wasn't a number")
        ask_code()


result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")
table = soup.find("tbody")
table_list = table.select('tr')

for extract_table_list in table_list:
    if extract_table_list.select('td')[2].string == None:
        pass
    else:
        country_name = extract_table_list.select('td')[0].string
        code = extract_table_list.select('td')[2].string
        country_dick = {country_name: code}
        country_list.append(country_dick)


print("Hello! Please choose select a country by number:")
for idx, val in enumerate(country_list):

    val_key = list(val.keys())[0]
    print(f"# {idx} {val_key}")

ask_code()
