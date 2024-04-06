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

## 다른 풀이
select s.user_id, round(avg(if(c.action="confirmed",1,0)),2) as confirmation_rate
from Signups as s left join Confirmations as c on s.user_id= c.user_id group by user_id;
