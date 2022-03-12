CREATE DEFINER=`root`@`localhost` TRIGGER `catalogs_AFTER_INSERT` AFTER INSERT ON `catalogs` FOR EACH ROW BEGIN
	insert into shop.logs (tables_id, tables_name, names, created_at)
	values (new.id, new.name, 'catalogs', now());
END