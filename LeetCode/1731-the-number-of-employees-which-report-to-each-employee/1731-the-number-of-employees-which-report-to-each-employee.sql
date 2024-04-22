# Write your MySQL query statement below
SELECT e.reports_to AS employee_id, m.name AS name, COUNT(e.employee_id) AS reports_count, ROUND(AVG(e.age)) AS average_age
FROM Employees e INNER JOIN Employees m ON e.reports_to = m.employee_id
WHERE e.reports_to IS NOT NULL
GROUP BY e.reports_to
ORDER BY e.reports_to;