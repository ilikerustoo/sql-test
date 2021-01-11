SELECT member
FROM membership
WHERE DATE(begin_date) = DATE('2018-12-31')
GROUP BY member;
-- assumes that member started on enrollment only on that day