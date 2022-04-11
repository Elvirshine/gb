CREATE DEFINER = CURRENT_USER TRIGGER `cinema`.`users_AFTER_INSERT` 
AFTER INSERT ON `users` FOR EACH ROW
BEGIN
	insert into cinema.profiles (users_id)
	values (new.id);
END
