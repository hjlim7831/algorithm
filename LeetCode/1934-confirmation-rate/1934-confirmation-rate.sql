# Write your MySQL query statement below
SELECT s.user_id,
ROUND(
IFNULL(
    (SELECT COUNT(*) FROM Confirmations c WHERE s.user_id = c.user_id AND c.action = "confirmed")
 / (SELECT COUNT(*) FROM Confirmations c WHERE s.user_id = c.user_id)
 , 0)
 , 2)
 AS confirmation_rate
FROM Signups s;