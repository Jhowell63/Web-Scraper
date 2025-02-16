from bs4 import BeautifulSoup
import re


with open("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

    # results = doc.find_all("option")
    # print(results)

    # tag = doc.find("option")
    # tag['value'] = 'new value'
    # print(tag)

    # tag = doc.find("option")
    # print(tag.attrs)

    # tag = doc.find_all(["p", "div", "l1"])
    # print(tag)

    # tag = doc.find_all(["option"], text="Undergraduate", value="undergraduate")
    # print(tag)

    # tag = doc.find_all(class_="btn-item")
    # print(tag)

    # tags = doc.find_all(text=re.compile("\$.*"))
    # for tag in tags:
        # print(tag.strip())

    # tags = doc.find_all(text=re.compile("\$.*"), limit=1)
    # for tag in tags:
        # print(tag.strip())

    tags = doc.find_all("input", type="text")
    for tag in tags:
        tag['placeholder'] = "I changed you!"

    with open("changed.html", "w") as file:
        file.write(str(doc))