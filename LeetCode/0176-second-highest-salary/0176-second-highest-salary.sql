# Write your MySQL query statement below
WITH cte AS (
    SELECT id, salary, DENSE_RANK() OVER(ORDER BY salary DESC) AS salary_rank
    FROM Employee
)
SELECT IF(COUNT(*) = 0, null, cte.salary) AS SecondHighestSalary
FROM cte
WHERE salary_rank = 2;