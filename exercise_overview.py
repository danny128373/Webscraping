import requests
from bs4 import BeautifulSoup

res = requests.get("http://quotes.toscrape.com/")
soup = BeautifulSoup(res.text, "lxml")


# 1. Get authors from first page (no repeats)
authors = soup.select(".author")
# list that will contain author names
authors_list = []
for author in authors:
    authors_list.append(author.text)
# Cast as a set in order to remove repeats
authors = set(authors_list)
print(authors)


# 2. Gets all quotes from first page
quotes = soup.select(".text")
quote_list = []
for quote in quotes:
    quote_list.append(quote.text)
print(quote_list)


# 3. Get the top 10 tags
tags = soup.select(".tag-item")
tag_list = []
for tag in tags:
    tag_list.append(tag.text)
filtered_tag_list = []

for tag in tag_list:
    filtered_tag = tag.split("\n")
    filtered_tag_list.append(filtered_tag[1])

print(filtered_tag_list)
