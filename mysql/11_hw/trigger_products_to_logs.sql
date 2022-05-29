CREATE DEFINER=`root`@`localhost` TRIGGER `products_AFTER_INSERT` AFTER INSERT ON `products` FOR EACH ROW BEGIN
	insert into shop.logs (tables_id, tables_name, names, created_at)
	values (new.id, 'products', new.name, now());
END