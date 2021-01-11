SELECT member, 
SUM(DATEDIFF(
    CASE
		WHEN YEAR(end_date) > 2018
        THEN '2019-01-01'
        ELSE end_date
    END,
    CASE
	    WHEN YEAR(begin_date) < 2018
        THEN '2018-01-01'
        ELSE begin_date
    END)) AS enrolldays
FROM membership
WHERE(YEAR(begin_date) <= '2018' AND YEAR(end_date) >= '2018')
GROUP BY member;
-- assumes that end_date does not count as an enrollment date