CREATE DEFINER=`root`@`localhost` TRIGGER `users_AFTER_INSERT` AFTER INSERT ON `users` FOR EACH ROW BEGIN
	insert into shop.logs (tables_id, tables_name, names, created_at)
	values (new.id, 'users', new.name, now());
END