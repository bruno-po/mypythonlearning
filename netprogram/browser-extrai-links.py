import urllib
from bs4 import BeautifulSoup 

url = raw_input('Digite a URL > ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)
# Retrieve all of the anchor tags
tags = soup('img')
for tag in tags:
    print tag.get('src', None)
