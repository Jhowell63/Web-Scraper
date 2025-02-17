from bs4 import BeautifulSoup
import requests
import re

product = input("What product do you want to search for? ")

url = f"https://www.newegg.ca/p/pl?d={product}&N=4131"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")
