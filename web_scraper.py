from bs4 import BeautifulSoup
import requests


url = "https://www.newegg.ca/p/N82E16883360565?Item=N82E16883360565&cm_sp=Homepage_SS-_-P2_83-360-565-_-02122025"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

prices = doc.find_all(string="$")
parent = prices[0].parent
strong = parent.find("strong")
print(strong.string)




