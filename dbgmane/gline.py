import sqlite3
import time
import urllib
import zlib
import re

conn = sqlite3.connect('index.sqlite')
conn.text_factory = str
cur = conn.cursor()

# Determine the top ten organizations
cur.execute('''SELECT Messages.id, sender FROM Messages
    JOIN Senders ON Messages.sender_id = Senders.id''')

sendorgs = dict()
for message_row in cur :
    sender = message_row[1]
    pieces = sender.split("@")
    if len(pieces) != 2 : continue
    dns = pieces[1]
    sendorgs[dns] = sendorgs.get(dns,0) + 1

# pick the top schools
orgs = sorted(sendorgs, key=sendorgs.get, reverse=True)
orgs = orgs[:10]
print "Top 10 Organizations"
print orgs
orgs = ['total'] + orgs

# Read through the messages
mcounts = dict()
dcounts = dict()
months = list()
days = list()

cur.execute('''SELECT Messages.id, sender, sent_at FROM Messages
    JOIN Senders ON Messages.sender_id = Senders.id''')

for message_row in cur :
    sender = message_row[1]
    pieces = sender.split("@")
    if len(pieces) != 2 : continue
    dns = pieces[1]
    if dns not in orgs : continue
    month = message_row[2][:7]
    if month not in months : months.append(month)
    key = (month, dns)
    mcounts[key] = mcounts.get(key,0) + 1
    tkey = (month, 'total')
    mcounts[tkey] = mcounts.get(tkey,0) + 1
    # print mcounts

print

cur.execute('''SELECT Messages.id, sender, sent_at FROM Messages
    JOIN Senders ON Messages.sender_id = Senders.id''')

for message_row in cur:
    sender = message_row[1]
    pieces = sender.split("@")
    if len(pieces) != 2 : continue
    dns = pieces[1]
    if dns not in orgs : continue
    fulldate = message_row[2]
    pieces = fulldate.split(' ')
    if len(pieces) != 2 : continue
    date = re.findall('-*(\d*)', pieces[0])
    day = date[2]
    if day not in days : days.append(day)
    key = (day, dns)
    dcounts[key] = dcounts.get(key,0) + 1
    tkey = (day, 'total')
    dcounts[tkey] = dcounts.get(tkey,0) + 1
    # print dcounts

months.sort()
print mcounts
print months
print
days.sort()
print dcounts
print days
print

fhand = open('gline.js','w')
fhand.write("gline = [ ['Day'")
for org in orgs:
    fhand.write(",'"+org+"'")
fhand.write("]")

# # for month in months[1:-1]:
# for month in months:
#     fhand.write(",\n['"+month+"'")
#     for org in orgs:
#         key = (month, org)
#         val = mcounts.get(key,0)
#         print val
#         fhand.write(","+str(val))
#     fhand.write("]");

# for day in days
for day in days:
    fhand.write(",\n['"+day+"'")
    for org in orgs:
        key = (day, org)
        val = dcounts.get(key,0)
        fhand.write(","+str(val))
    fhand.write("]");

fhand.write("\n];\n")
#
# print "Output written to gline.js"
