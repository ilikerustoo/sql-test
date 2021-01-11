SELECT member, COUNT(DISTINCT member) 
FROM membership 
WHERE YEAR(begin_date) <= '2018' AND YEAR(end_date) >= '2018' GROUP BY member;