# Write your MySQL query statement below
SELECT st.machine_id, ROUND(AVG(ed.timestamp - st.timestamp), 3) AS processing_time FROM Activity ed INNER JOIN Activity st
ON ed.machine_id = st.machine_id AND ed.process_id = st.process_id
WHERE st.activity_type = 'start' AND ed.activity_type = 'end'
GROUP BY st.machine_id;