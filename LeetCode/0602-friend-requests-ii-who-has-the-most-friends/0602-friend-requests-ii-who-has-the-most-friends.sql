# Write your MySQL query statement below
WITH cte AS (
    SELECT requester_id id, accepter_id s
    FROM RequestAccepted
    UNION ALL
    SELECT accepter_id id, requester_id s
    FROM RequestAccepted
)
SELECT id, COUNT(s) AS num
FROM cte
GROUP BY id
ORDER BY COUNT(s) DESC
LIMIT 1;