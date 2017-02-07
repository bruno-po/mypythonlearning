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
)

INSERT INTO Artist (name) VALUES ('Led Zepelin');
INSERT INTO Artist (name) VALUES ('AC/DC');
INSERT INTO Genre (name) VALUES ('Rock');
INSERT INTO Genre (name) VALUES ('Metal');
INSERT INTO Album (title,artist_id) VALUES ('Who Made Who', 2);
INSERT INTO Album (title,artist_id) VALUES ('IV', 1);
INSERT INTO Track (title,album_id,genre_id,len,rating,count) VALUES ('', );
INSERT INTO Track (title,album_id,genre_id,len,rating,count) VALUES ('', );
