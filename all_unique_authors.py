import requests
from bs4 import BeautifulSoup

# Get all distinct authors from all pages
base_url = "http://quotes.toscrape.com/page/"
author_list = []

for page_num in range(11):
    res = requests.get(base_url + str(page_num))
    soup = BeautifulSoup(res.text, "lxml")
    authors = soup.select(".author")
    for author in authors:
        author_list.append(author.text)

author_list = set(author_list)
print(author_list)
