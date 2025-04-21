import json
import bs4

with open("two-sum.json", "r") as f:
    data = json.load(f)

soup = bs4.BeautifulSoup(data["question"]["content"])

snips = soup.find_all("pre")
# print(snips[0])

for test in snips:

