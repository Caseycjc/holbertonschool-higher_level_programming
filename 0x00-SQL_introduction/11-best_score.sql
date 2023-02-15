-- script that lists all records with a score of 10 or more
SELECT `score`, `name` FROM second_table WHERE `score` >= 10
ORDER BY `score` DESC;