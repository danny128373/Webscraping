# Goal: Get title of every book with a 2 star rating
import requests
from bs4 import BeautifulSoup


# Example url: http://books.toscrape.com/catalogue/page-2.html
page_num = 1
# Assigns base_url the url as an f-string
base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
# Requests the entire html of page
res = requests.get(base_url.format(1))
# Makes res legible
soup = BeautifulSoup(res.text, 'lxml')
# Selects anything in page with the class product_pod
products = soup.select('.product_pod')
# Grabs first book and assigns to example
example = products[0]
# Selects anything with the class star-rating Three
rating_container = example.select('.star-rating.Three')

# Code for goal
two_star_titles = []
for page in range(1, 51):
    scrape_url = base_url.format(page)
    res = requests.get(scrape_url)
    soup = BeautifulSoup(res.text, 'lxml')
    books = soup.select('.product_pod')
    for book in books:
        if book.select('.star-rating.Two') != []:
            two_star_titles.append(book.select('a')[1]['title'])

for title in two_star_titles:
    print(title)
