# A program for scraping webpages for images and saving them to the file system
# Import packages
from bs4 import BeautifulSoup
import requests


# Make a get request to retrieve webpage and pass through BeautifulSoup for parsing
html_page = requests.get('http://books.toscrape.com')
soup = BeautifulSoup(html_page.content, 'html.parser')
warning = soup.find('div', class_="alert alert-warning")
book_container = warning.nextSibling.nextSibling

images = book_container.findAll('img')
example = images[0]

print(example)
