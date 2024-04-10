# Write your MySQL query statement below
SELECT
q.query_name,
ROUND(AVG(q.rating / q.position), 2) AS quality,
ROUND(AVG(IF(q.rating < 3, 100, 0)), 2) AS poor_query_percentage
FROM Queries q
WHERE q.query_name IS NOT NULL
GROUP BY q.query_name;