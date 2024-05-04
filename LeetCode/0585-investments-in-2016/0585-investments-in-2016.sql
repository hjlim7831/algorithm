# Write your MySQL query statement below
WITH valid_tiv_2015 AS (
    SELECT tiv_2015
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(tiv_2015) >= 2
),

unique_lat_lon AS (
    SELECT lat, lon
    FROM Insurance
    GROUP BY lat, lon
    HAVING COUNT(*) = 1
)
SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM Insurance
WHERE (lat, lon) IN (SELECT lat, lon FROM unique_lat_lon)
AND tiv_2015 IN (SELECT tiv_2015 FROM valid_tiv_2015);