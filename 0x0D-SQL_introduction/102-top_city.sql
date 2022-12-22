-- Import in hbtn_0c_0 database this table dump: download (same as Temperatures #0)

SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month BETWEEN 7 and 8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
