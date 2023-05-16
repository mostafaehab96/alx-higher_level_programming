-- Lists number of records with the same score from second_table

SELECT score, COUNT(*) AS number FROM second_table GROUP BY score;
