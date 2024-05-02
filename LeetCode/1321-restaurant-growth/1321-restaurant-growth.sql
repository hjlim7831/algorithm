# Write your MySQL query statement below
WITH daily_customer AS (
    SELECT
        visited_on,
        SUM(amount) AS total_amount
    FROM Customer
    GROUP BY visited_on
),
daily_ma_customer AS (
    SELECT
        visited_on,
        SUM(total_amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount,
        MIN(visited_on) OVER() 1st_date
        FROM daily_customer
)
SELECT visited_on, amount, ROUND(amount/7, 2) AS average_amount
FROM daily_ma_customer
WHERE visited_on >= 1st_date+6;

-- -- SELECT visited_on, amount, ROUND(amount/7, 2) AS average_amount
-- -- FROM daily_customer
-- -- WHERE visited_on >= 1st_date+6;
-- SELECT * FROM daily_customer;