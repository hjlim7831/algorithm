# Write your MySQL query statement below
WITH cte AS
(
    SELECT person_id
    , person_name
    , turn
    , SUM(weight) OVER (ORDER BY turn) AS cum_weight
    FROM Queue
    ORDER BY turn
)
SELECT person_name FROM cte
WHERE cum_weight <= 1000
ORDER BY turn DESC
LIMIT 1;