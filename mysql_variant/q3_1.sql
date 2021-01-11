SELECT member
FROM membership
WHERE DATE(begin_date) >= DATE('2018-12-31')
GROUP BY member;
-- assumes members is starting on that date or after