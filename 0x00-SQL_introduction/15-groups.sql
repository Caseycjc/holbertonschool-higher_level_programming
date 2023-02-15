-- script that lists the number of records with the same score
SELECT `score`, COUNT(*) AS "number" FROM second_table
GROUP BY `score` HAVING COUNT(*) > 0 ORDER BY `number` DESC;