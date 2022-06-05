start transaction;

insert into sample.users (id, name)
select users.id, users.name
from shop.users where users.id = 1;

DELETE FROM shop.users WHERE id = 1 LIMIT 1;

SELECT * FROM sample.users;

commit;