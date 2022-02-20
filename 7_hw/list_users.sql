INSERT INTO shop1.orders (user_id, created_at, updated_at) VALUES
  ('1', now(), now()),
  ('3', now(), now()),
  ('6', now(), now()),
  ('2', now(), now()),
  ('3', now(), now()),
  ('6', now(), now()),
  ('3', now(), now()),
  ('4', now(), now());

SELECT 
    u.id
FROM
    shop.orders as o
    JOIN
    shop.users as u
	on
	o.user_id = u.id
    group by u.id;
