# A program for scraping webpages for images and saving them to the file system
# Import packages
from bs4 import BeautifulSoup
import requests
import shutil
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Make a get request to retrieve webpage and pass through BeautifulSoup for parsing
html_page = requests.get('http://books.toscrape.com')
soup = BeautifulSoup(html_page.content, 'html.parser')
warning = soup.find('div', class_="alert alert-warning")
book_container = warning.nextSibling.nextSibling

images = book_container.findAll('img')
example = images[0]

# print(example.attrs['src']) - ## Commented out for testing

url_base = "http://books.toscrape.com/" # Original Website
url_ext = example.attrs['src'] # The extension you pulled earlier
full_url = url_base + url_ext # Combining to get the full URL

r = requests.get(full_url, stream=True) # Get request on full_url

if r.status_code == 200:
    with open("Pictures", 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)

img = mpimg.imread('Pictures')
imgplot = plt.imshow(img)
plt.show()

# TODO: Images are being saved as Portable Networks Graphic files as Pictures in Project folder.
####### Find a way to save images in WEBP format in a specific folder in filesystem.
