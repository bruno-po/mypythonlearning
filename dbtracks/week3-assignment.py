import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('musicasdb.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Composer;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist(
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	name TEXT
)

CREATE TABLE Genre(
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	name TEXT
)

CREATE TABLE Album(
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	artist_id INTEGER,
	title TEXT
)

CREATE TABLE Track(
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	title TEXT,
	album_id INTEGER,
	genre_id INTEGER,
	len INTEGER, rating INTEGER, count INTEGER
);
''')
