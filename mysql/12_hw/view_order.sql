CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `order3` AS
    SELECT 
        `o`.`id` AS `orders`,
        CONCAT(`p`.`firstname`, ' ', `p`.`lastname`) AS `name`,
        `f`.`name` AS `film`,
        GROUP_CONCAT(`s`.`price`
            SEPARATOR ',') AS `price`,
        GROUP_CONCAT(`t`.`type`
            SEPARATOR ',') AS `ticket_type`,
        GROUP_CONCAT(CONCAT(`s`.`seat_number`,
                    ' ',
                    'место',
                    ' ',
                    s.rows_number,
                    ' ',
                    'ряд')
            SEPARATOR ',') AS seats,
        SUM(o.seats_price) AS sum
    FROM
        ((((orders o
        JOIN seats `s` ON ((o.seats_id = s.id)))
        JOIN profiles `p` ON ((o.profiles_users_id = p.users_id)))
        JOIN ticket_type `t` ON ((o.ticket_type_id = t.id)))
        JOIN filmes `f` ON ((o.filmes_id = f.id)))
    GROUP BY o.profiles_users_id
    ORDER BY orders