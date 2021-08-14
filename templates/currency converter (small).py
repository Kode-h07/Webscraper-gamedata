import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

os.system("clear")
"""
Use the 'format_currency' function to format the output of the conversion
format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR" (no need to change this one))
"""
url = "https://www.iban.com/currency-codes"
result = requests.get(url)
soup = BeautifulSoup(result.text, 'html.parser')
countries = []
info = soup.find_all('tr')[1:]

for i in info:
    countries.append(i)
country_list = []

for i in countries:
    country = i.find_all('td')[0].text
    country_list.append(country)
res = [idx for idx, val in enumerate(country_list) if val in country_list[:idx]]

for i in res:
    if i + 1 in res:
        country_list[i - 1] = country_list[i - 1] + '(1)'
        country_list[i] = country_list[i] + '(2)'
        country_list[i + 1] = country_list[i + 1] + '(3)'
        res.remove(i + 1)
    else:
        country_list[i - 1] = country_list[i - 1] + '(1)'
        country_list[i] = country_list[i] + '(2)'
currency = []
for i in info:
    currency.append(i)
currency_list = []

for i in currency:
    currency = i.find_all('td')[2].text
    currency_list.append(currency)
zip_iterator = zip(country_list, currency_list)
dict = dict(zip_iterator)

for i in list(dict):
    if (dict[i]) == '':
        del dict[i]
print('Hello! Please choose select a country by number:')
for i in list(dict):
    print(f'#{list(dict).index(i)} {i}')
print('')
print('Where are you from? Choose a country by a number. ')
print('')
while True:
    global search

    try:
        search = int(input('#: '))
        if search > len(dict):
            print('Choose a number from the list')
            continue
        elif search <= len(dict) - 1:
            home_country = list(dict.keys())[search]
            print(home_country)
        break
    except:
        print("That wasn't a number")
print('')
print('Now Choose another country')
print('')
while True:
    global search2

    try:
        search2 = int(input('#: '))
        if search2 > len(dict):
            print('Choose a number from the list')
            continue
        elif search2 <= len(dict):
            conv_country = list(dict.keys())[search2]
            print(conv_country)
        break
    except:
        print("That wasn't a number")

home_code = list(dict.values())[search]
conv_code = list(dict.values())[search2]

while True:
    global amount
    try:
        amount = float(input(f"How many {home_code} do you want to convert to {conv_code}?\n"))
        break
    except:
        print("That wasn't a number")

url_conv = f"https://wise.com/gb/currency-converter/{home_code.lower()}-to-{conv_code.lower()}-rate?amount={amount}"

result2 = requests.get(url_conv)
soup2 = BeautifulSoup(result2.text, "html.parser")
rate = soup2.find('input', {'class': 'js-Rate'}).get('value')
converted = float(rate) * float(amount)
home = format_currency(amount, home_code, locale='ko_KR')
conv = format_currency(converted, conv_code, locale="ko_KR")
print(f"{home} is {conv}")