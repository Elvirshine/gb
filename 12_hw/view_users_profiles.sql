CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `users+profiles` AS
    SELECT 
        `p`.`users_id` AS `user_id`,
        CONCAT(`p`.`firstname`, ' ', `p`.`lastname`) AS `name`,
        `u`.`phone` AS `phone`,
        `u`.`email` AS `email`
    FROM
        (`profiles` `p`
        LEFT JOIN `users` `u` ON ((`p`.`users_id` = `u`.`id`)))