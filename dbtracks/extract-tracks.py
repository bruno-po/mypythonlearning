import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('musicasdb.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Composer;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
);

CREATE TABLE Album (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id INTEGER,
    title TEXT UNIQUE,
    rating INTEGER
);

CREATE TABLE Genre (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Composer (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Track (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id INTEGER,
    genre_id INTEGER,
    composer_id INTEGER,
    count INTEGER, len INTEGER, num INTEGER, year INTEGER, rating INTEGER
);
''')


fname = 'Library.xml'
trackList = []

def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None


stuff = ET.parse(fname)
lst = stuff.findall('dict/dict/dict')
print 'Tracks count:', len(lst)
for entry in lst:
    if ( lookup(entry, 'Track ID') is None ) : continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    composer = lookup(entry, 'Composer')
    album = lookup(entry, 'Album')
    genre = lookup(entry, 'Genre')
    plcount = lookup(entry, 'Play Count')
    length = lookup(entry, 'Total Time')
    tcknum = lookup(entry, 'Track Number')
    year = lookup(entry, 'Year')
    rating = lookup(entry, 'Rating')
    alrating = lookup(entry, 'Album Rating')

    if name is None or artist is None or album is None or genre is None or composer is None :
        continue

    # print name, artist, composer, album, genre, plcount, length, tcknum, year, rating, alrating

    cur.execute('''INSERT OR IGNORE INTO Artist (name)
        VALUES ( ? )''', (artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id, rating)
        VALUES ( ?, ? , ? )''', ( album,  artist_id, alrating ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Genre (name)
        VALUES ( ? )''', ( genre, ) )
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Composer (name)
        VALUES ( ? )''', ( composer, ) )
    cur.execute('SELECT id FROM Composer WHERE name = ? ', (composer, ))
    composer_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, composer_id, num, rating, len, count )
        VALUES ( ? , ? , ? , ? , ? , ? , ? , ? )''',
        ( name, album_id, genre_id, composer_id, tcknum, rating, length, plcount) )

conn.commit()
