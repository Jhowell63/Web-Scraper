from bs4 import BeautifulSoup
import requests

url = "https://coinmarketcap.com"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

# tbody = doc.tbody
# print(tbody)

# tbody = doc.tbody
# trs = tbody.contents
# print(trs)

# tbody = doc.tbody
# trs = tbody.contents

#  print(trs[0].next_sibling)

tbody = doc.tbody
trs = tbody.contents

prices = {}

for tr in trs[:10]:
    name, price =  tr.contents[2:4]
    fixed_name = name.p.string
    fixed_price = price.span.string

    prices[fixed_name] = fixed_price

for name, price in prices.items():
    print(f"{name} : {price}\n")
