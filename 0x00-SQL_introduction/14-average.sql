-- script that computes the score average of all records in a table
SELECT SUM(`score`) / COUNT(*) AS "average" FROM second_table;