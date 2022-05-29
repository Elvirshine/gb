CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `product_catalog` AS
    SELECT 
        `p`.`name` AS `products_name`, `c`.`name` AS `catalogs_name`
    FROM
        (`products` `p`
        LEFT JOIN `catalogs` `c` ON ((`p`.`catalog_id` = `c`.`id`)))