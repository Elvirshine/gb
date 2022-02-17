alter table shop.users change created_at created_at varchar(50);
alter table shop.users change updated_at updated_at varchar(50);

UPDATE shop.users
SET created_at = '20.10.2017 8:10', updated_at = '20.10.2017 8:10'
WHERE (id > 0);

SELECT *, STR_TO_DATE(created_at,'%d.%m.%Y %H:%i'), STR_TO_DATE(updated_at,'%d.%m.%Y %H:%i') 
FROM shop.users;