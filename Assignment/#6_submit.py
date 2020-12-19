import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

url = "https://www.iban.com/currency-codes"

country_list = []


def ask_code():
    try:
        answer = int(input("#: "))
        if answer < 0 or answer > 264:
            print('Choose a number from the list.')
        else:
            choose_country = country_list[answer]
            name = choose_country['name']
            print(f"{name}")
            return choose_country
    except:
        print("That wasn't a number")


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
        country_dick = {
            'name': country_name,
            "code": code
        }
        country_list.append(country_dick)


print("Hello! Please choose select a country by number:")
for idx, val in enumerate(country_list):
    print(f"# {idx} {val['name']}")
print("\nWhere are you from? Choose a country by number\n")

first_country = ask_code()
while first_country == None:
    first_country = ask_code()

print("\nNow choose another country.\n")

last_country = ask_code()
while last_country == None:
    last_country = ask_code()


def ask_convert_money():
    print(
        f"\nHow many {first_country['code']} do you want to convert to {last_country['code']}?")
    try:
        convert_money = float(input())
        return convert_money
    except:
        print("That wasn't a number.")


convert_money = ask_convert_money()
while type(convert_money) != float:
    convert_money = ask_convert_money()


url_transferwise = f"https://transferwise.com/gb/currency-converter/{first_country['code']}-to-{last_country['code']}-rate?amount={convert_money}"
result = requests.get(url_transferwise)
soup = BeautifulSoup(result.text, "html.parser")
table = float(soup.find("span", {"class": "text-success"}).string)
result_money = table * convert_money
print(
    format_currency(convert_money, first_country['code']),
    "is",
    format_currency(result_money, last_country['code'])
)
