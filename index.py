from pip._vendor import requests
from bs4 import BeautifulSoup


result = requests.get("https://en.wikipedia.org/wiki/Jonas_Salk")

# result.text is the entire text of the website
# lxml makes the html look legible
# soup is an instance of BeautifulSoup
soup = BeautifulSoup(result.text, "lxml")
# soup inherited select, select retrieves all h1 tags in a list
# in this case we are only getting the text portion of the first element in the list
name_of_wiki = soup.select('h1')[0].getText()
print(name_of_wiki)
# retriving the 3rd paragraph in this site
paragraph = soup.select('p')[2].getText()
print(paragraph)

res = requests.get("https://en.wikipedia.org/wiki/Grace_Hopper")
soup = BeautifulSoup(res.text, "lxml")

# every title in table of contents has toctext class
table_of_contents_list = soup.select('.toctext')
for _ in table_of_contents_list:
    print(_.getText())

# scraping an image
res = requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')
soup = BeautifulSoup(res.text, 'lxml')
computer = soup.select('.thumbimage')[0]['src']
print(computer)

# image_link is assigned full path of computer image

image_link = requests.get(f'https:{computer}')

# creating a jpg file to put computer image content
f = open('computer_image.jpg', 'wb')
# image_link.content is the binary representation of the computer image
f.write(image_link.content)
f.close()
