import urllib
import re

url = raw_input('Digite a URL > ')
html = urllib.urlopen(url).read()
links = re.findall('href="(http://.*?)"', html)
for link in links:
    print link
