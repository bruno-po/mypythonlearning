SELECT title FROM Track

SELECT Track.title, Artist.name, Album.title, Track.num,
  Track.year, Genre.name, Composer.name, Track.rating
  FROM Track JOIN Artist JOIN Album JOIN Genre JOIN Composer
