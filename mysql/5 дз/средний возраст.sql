SELECT 
avg(timestampdiff(year, birthday_at, now())) as average_age
FROM shop.users;