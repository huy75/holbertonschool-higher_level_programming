--  lists the number of records with the same score in the table second_table
-- Results should display:
-- 	   score
--	   number of records for this score with the label number
-- Sorted in descending order of number of records
SELECT score, COUNT(score) as number
FROM second_table
GROUP BY score
ORDER BY  COUNT(score) DESC;
