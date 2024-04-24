# Write your MySQL query statement below
WITH cte AS (
    SELECT num, id,
    LEAD(num, 1) OVER(ORDER BY id) num1,
    LEAD(id, 1) OVER(ORDER BY id) id1,
    LEAD(num, 2) OVER(ORDER BY id) num2,
    LEAD(id, 2) OVER(ORDER BY id) id2
    FROM Logs
    ORDER BY id
)

SELECT DISTINCT num ConsecutiveNums
FROM cte
WHERE num = num1 AND num = num2
AND id = id1 - 1 AND id1 = id2 - 1
