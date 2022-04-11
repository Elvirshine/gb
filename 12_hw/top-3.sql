-- 3 самых молодых заказчика
SELECT -- *,
	o.id `order#`
    , concat(firstname, ' ', lastname) as name
    , (timestampdiff(year, p.birthday_at, now())) as age
FROM cinema.orders as o
	join cinema.profiles as p on o.profiles_users_id = p.id
group by p.id
order by age
limit 3
;