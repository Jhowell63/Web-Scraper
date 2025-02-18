from bs4 import BeautifulSoup
import requests
import re

product = input("What product do you want to search for? ")

url = f"https://www.newegg.com/p/pl?d={product}&N=4131"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

page_text = doc.find(class_="list-tool-pagination-text").strong
pages = int(str(page_text).split("/")[-2].split(">")[-1][:-1])

items_found = {}

for page in range(1, pages + 1):
    url = f"https://www.newegg.com/p/pl?d={product}&N=4131&page={page}" 
    page = requests.get(url).text 
    doc = BeautifulSoup(page, "html.parser")
    
    div = doc.find(class_="item-cells-wrap border-cells short-video-box items-list-view is-list")
    
    if div is None:
        print(f"Warning: Could not find items on page {page}")
        continue

    # Initialize items list for the current page
    items = []
    for tag in div.find_all(string=True):  # Iterate over all text nodes
        if product.lower() in tag.lower():  # Check if product name is in the text (case-insensitive)
            items.append(tag)

    # Process each item found
    for item in items:
        parent = item.parent
        link = None
        if parent.name != "a":
            continue
        
        link = parent['href']
        next_parent = item.find_parent(class_="item-container")
        try:
            price = next_parent.find(class_="price-current").find("strong").string
            items_found[item] = {"price": int(price.replace(",", "")), "link": link}
        except:
            pass

# Sort items by price
sorted_items = sorted(items_found.items(), key=lambda x: x[1]['price'])

# Display the results
for item in sorted_items:
    print(item[0])
    print(f"${item[1]['price']}")
    print(item[1]['link'])
    print("----------------------------")
