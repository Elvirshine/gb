SELECT 
    p.name, c.name
FROM
    shop.products as p
    left join 
    shop.catalogs as c
    on catalog_id = c.id
    ;