CREATE DEFINER=`root`@`localhost` TRIGGER `n_null_for_insert` BEFORE INSERT ON `products` FOR EACH ROW BEGIN
	if isnull(new.name) + isnull(new.description) = 0 then 
		signal sqlstate '45000'
		set message_text = 'not allow null both of cell';
	end if;
END