import urllib
fhand = urllib.urlopen('http://getip.net.br/blog')
for line in fhand:
    print line.strip()
