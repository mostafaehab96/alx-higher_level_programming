-- Lists all records of the table second_table which has a name sorted by score.

SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
