import requests
from bs4 import BeautifulSoup

# Get all distinct authors from all pages (assuming you don't know how many pages)
url = "http://quotes.toscrape.com/page/"
page_still_valid = True
authors = set()
page = 1
while page_still_valid:
    page_url = url + str(page)
    res = requests.get(page_url)

    if "No quotes found!" in res.text:
        break

    soup = BeautifulSoup(res.text, "lxml")

    for name in soup.select(".author"):
        authors.add(name.text)

    page = page + 1

print(authors)
