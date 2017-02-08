import urllib


counts = dict()

fhand = urllib.urlopen('http://getip.net.br/blog')

for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

print counts
