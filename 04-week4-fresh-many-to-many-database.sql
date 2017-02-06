

CREATE TABLE User (
	id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	name TEXT,
	email TEXT
);

CREATE TABLE Couse (
	id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	title	TEXT
);

CREATE TABLE Member (
	user_id	INTEGER,
	course_id INTEGER,
		role INTEGER,
	PRIMARY KEY (user_id, course_id)
)

INSERT INTO User (name, email) VALUES ('Jane',
'jane@tsugi.org');
INSERT INTO User (name, email) VALUES ('Ed',
'ed@tsugi.org');
INSERT INTO User (name, email) VALUES ('Sue',
'sue@tsugi.org');

INSERT INTO Course (title) VALUES ('Python');
INSERT INTO Course (title) VALUES ('SQL');
INSERT INTO Course (title) VALUES ('PHP')
