# Write your MySQL query statement below
-- WITH DeliveryFirstOrders AS (
--     SELECT *, ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date DESC) AS rn
--     FROM Delivery d
-- )
-- WITH DeliveryFirstOrders AS (
--     SELECT customer_id, min(order_date) AS first_order_date
--     FROM Delivery d
--     GROUP BY customer_id
-- )
-- SELECT ROUND(AVG(IF(dfo.first_order_date = d.customer_pref_delivery_date, 100, 0)), 2) AS immediate_percentage
-- FROM DeliveryFirstOrders dfo INNER JOIN Delivery d
-- WHERE d.customer_id = dfo.customer_id AND d.order_date = dfo.first_order_date
-- ;
-- SELECT d.customer_id, first_order_date, customer_pref_delivery_date FROM DeliveryFirstOrders dfo INNER JOIN Delivery d
-- WHERE d.customer_id = dfo.customer_id
-- AND d.order_date = dfo.first_order_date

WITH DeliveryFirstOrders AS (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date ASC) AS rn
    FROM Delivery d
)
SELECT ROUND(AVG(IF(dfo.order_date = dfo.customer_pref_delivery_date, 100, 0)), 2) AS immediate_percentage
FROM DeliveryFirstOrders dfo
WHERE rn = 1;