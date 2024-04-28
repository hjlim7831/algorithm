# Write your MySQL query statement below
SELECT sc.category, COUNT(account_id) AS accounts_count
FROM (
    SELECT 'Low Salary' AS category
    UNION ALL
    SELECT 'Average Salary'
    UNION ALL
    SELECT 'High Salary') AS sc(category)
LEFT JOIN (
    SELECT
        account_id, 
        CASE
            WHEN income < 20000 THEN "Low Salary"
            WHEN income >= 20000 AND income <= 50000 THEN "Average Salary"
            ELSE "High Salary"
        END AS category
    FROM Accounts
) AS ac ON sc.category = ac.category
GROUP BY category;