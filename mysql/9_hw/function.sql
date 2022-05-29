CREATE DEFINER=`root`@`localhost` FUNCTION `hello`(time_of_day varchar(12)) RETURNS varchar(12) CHARSET utf8mb4
    NO SQL
BEGIN
		declare tmd VARCHAR(12);
            case
				when ((curtime() > time('06:00:01')) 
				  and (curtime() < time('12:00:00'))) then set tmd = 'Доброе утро';
				when ((curtime() > time('12:00:01')) 
				  and (curtime() < time('18:00:00'))) then set tmd = 'Добрый день';
				when ((curtime() > time('18:00:01')) 
				  and (curtime() < time('23:59:59'))) then set tmd = 'Добрый вечер';
				else set tmd = 'Доброй ночи';
			end case;
	RETURN tmd;
END