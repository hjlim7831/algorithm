# Write your MySQL query statement below
SELECT id, movie, description, rating 
FROM Cinema c
WHERE MOD(id, 2) = 1
AND description != "boring"
ORDER BY rating DESC;