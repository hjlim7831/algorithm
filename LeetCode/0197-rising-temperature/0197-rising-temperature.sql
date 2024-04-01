# Write your MySQL query statement below
SELECT nw.id FROM Weather yw, Weather nw
WHERE DATEDIFF(nw.recordDate, yw.recordDate) = 1
AND yw.temperature < nw.temperature;