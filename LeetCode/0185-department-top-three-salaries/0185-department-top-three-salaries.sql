# Write your MySQL query statement below
WITH salary_rank AS
(
    SELECT d.name AS Department
         , e.name AS Employee
         , e.salary
         , DENSE_RANK() OVER(PARTITION BY d.id ORDER BY e.salary DESC) AS rank_sal
         FROM Employee e
         INNER JOIN Department d ON e.departmentId = d.id
)
SELECT Department, Employee, salary
FROM salary_rank
WHERE rank_sal <= 3;