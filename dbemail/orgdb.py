import sqlite3
import re

conn = sqlite3.connect('orgdb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE If EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts(org TEXT, count INTEGER)''')

fileName = raw_input('Nome do arquivo: ')
if ( len(fileName) < 1 ) : fileName = 'mbox.txt'
filHandle = open(fileName)
for line in filHandle:
    if not line.startswith('From: ') : continue
    linePieces = line.split()
    emails = linePieces[1]
    emailPieces = emails.split('@')
    org = emailPieces[1]
    # print org
    cur.execute('SELECT count FROM Counts WHERE org = ?', (org, ))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES ( ?, 1 )''', ( org, ) )
    else:
        cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?', (org, ))
conn.commit()
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

print
print 'Counts:'
for row in cur.execute(sqlstr) :
    print str(row[0]), row[1]

cur.close()
