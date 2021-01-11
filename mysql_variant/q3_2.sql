SELECT member
FROM membership
WHERE DATE(begin_date) >= DATE('2018-12-31') OR DATE(end_date) = DATE('2018-12-31')
GROUP BY member;
-- assumes that end_date DOES count as enrollment