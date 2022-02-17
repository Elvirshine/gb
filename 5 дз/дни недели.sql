SELECT 
dayname(ADDDATE(birthday_at, INTERVAL (timestampdiff(year, birthday_at, now())) year)) day_name,
count(*)
FROM shop.users
group by day_name;