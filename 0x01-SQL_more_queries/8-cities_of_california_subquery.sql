-- script that lists all the cities of California in a database
SELECT cities.id, name FROM cities WHERE state_id =
(SELECT id FROM states WHERE name = 'California') ORDER BY cities.id ASC;