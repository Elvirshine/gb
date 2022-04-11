-- MySQL Workbench Synchronization
-- Generated: 2022-04-05 21:33
-- Model: New Model
-- Version: 1.0
-- Project: Name of the project
-- Author: evyus

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

ALTER TABLE `cinema`.`filiales` 
DROP FOREIGN KEY `fk_filiales_hall_types1`;

ALTER TABLE `cinema`.`filmes` 
DROP FOREIGN KEY `fk_filmes_age_limites1`;

ALTER TABLE `cinema`.`orders` 
DROP FOREIGN KEY `fk_orders_filmes1`,
DROP FOREIGN KEY `fk_orders_seats1`;

ALTER TABLE `cinema`.`profiles` 
DROP FOREIGN KEY `fk_profiles_users`;

ALTER TABLE `cinema`.`filmes_has_formats` 
DROP FOREIGN KEY `fk_filmes_has_film_formats_film_formats1`;

ALTER TABLE `cinema`.`filmes_has_media_types` 
DROP FOREIGN KEY `fk_filmes_has_media_types_filmes1`,
DROP FOREIGN KEY `fk_filmes_has_media_types_media_types1`;

ALTER TABLE `cinema`.`filmes_has_media_persons` 
DROP FOREIGN KEY `fk_filmes_has_media_persons_filmes1`,
DROP FOREIGN KEY `fk_filmes_has_media_persons_media_persons1`;

ALTER TABLE `cinema`.`hall_types_has_seats` 
DROP FOREIGN KEY `fk_hall_types_has_seats_hall_types1`,
DROP FOREIGN KEY `fk_hall_types_has_seats_seats1`;

ALTER TABLE `cinema`.`seats` 
DROP COLUMN `rows_number`,
ADD COLUMN `rows_number` INT(10) UNSIGNED NOT NULL AFTER `seat_number`,
CHANGE COLUMN `price` `price` DECIMAL UNSIGNED NOT NULL ;

ALTER TABLE `cinema`.`filmes` 
CHANGE COLUMN `film_duration` `film_duration` INT(11) NOT NULL ,
CHANGE COLUMN `beginning` `beginning` DATETIME NOT NULL ;

ALTER TABLE `cinema`.`users` 
CHANGE COLUMN `phone` `phone` BIGINT(14) NULL DEFAULT NULL ,
CHANGE COLUMN `created_at` `created_at` DATETIME NOT NULL DEFAULT now() ,
CHANGE COLUMN `updated_at` `updated_at` DATETIME NULL DEFAULT now() ;

ALTER TABLE `cinema`.`orders` 
CHANGE COLUMN `cancel_date` `cancel_date` DATETIME NULL DEFAULT NULL ;

ALTER TABLE `cinema`.`profiles` 
CHANGE COLUMN `birthday_at` `birthday_at` DATE NULL DEFAULT NULL ;

ALTER TABLE `cinema`.`filmes_has_media_persons` 
CHANGE COLUMN `filmes_id` `filmes_id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT ;

ALTER TABLE `cinema`.`filiales` 
ADD CONSTRAINT `fk_filiales_hall_types1`
  FOREIGN KEY (`hall_types_id`)
  REFERENCES `cinema`.`hall_types` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

ALTER TABLE `cinema`.`filmes` 
ADD CONSTRAINT `fk_filmes_age_limites1`
  FOREIGN KEY (`id`)
  REFERENCES `cinema`.`age_limites` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

ALTER TABLE `cinema`.`orders` 
DROP FOREIGN KEY `fk_orders_ticket_type1`,
DROP FOREIGN KEY `fk_orders_profiles1`;

ALTER TABLE `cinema`.`orders` ADD CONSTRAINT `fk_orders_ticket_type1`
  FOREIGN KEY (`ticket_type_id`)
  REFERENCES `cinema`.`ticket_type` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_orders_profiles1`
  FOREIGN KEY (`profiles_users_id`)
  REFERENCES `cinema`.`profiles` (`users_id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_orders_filmes1`
  FOREIGN KEY (`filmes_id`)
  REFERENCES `cinema`.`filmes` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_orders_seats1`
  FOREIGN KEY (`seats_id`)
  REFERENCES `cinema`.`seats` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

ALTER TABLE `cinema`.`profiles` 
ADD CONSTRAINT `fk_profiles_users`
  FOREIGN KEY (`users_id`)
  REFERENCES `cinema`.`users` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

ALTER TABLE `cinema`.`filmes_has_formats` 
DROP FOREIGN KEY `fk_filmes_has_film_formats_filmes1`;

ALTER TABLE `cinema`.`filmes_has_formats` ADD CONSTRAINT `fk_filmes_has_film_formats_filmes1`
  FOREIGN KEY (`filmes_id`)
  REFERENCES `cinema`.`filmes` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_filmes_has_film_formats_film_formats1`
  FOREIGN KEY (`film_formats_id`)
  REFERENCES `cinema`.`film_formats` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

ALTER TABLE `cinema`.`filmes_has_media_types` 
ADD CONSTRAINT `fk_filmes_has_media_types_filmes1`
  FOREIGN KEY (`filmes_id`)
  REFERENCES `cinema`.`filmes` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_filmes_has_media_types_media_types1`
  FOREIGN KEY (`media_types_id`)
  REFERENCES `cinema`.`media_types` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

ALTER TABLE `cinema`.`filmes_has_media_persons` 
ADD CONSTRAINT `fk_filmes_has_media_persons_filmes1`
  FOREIGN KEY (`filmes_id`)
  REFERENCES `cinema`.`filmes` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_filmes_has_media_persons_media_persons1`
  FOREIGN KEY (`media_persons_id`)
  REFERENCES `cinema`.`media_persons` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

ALTER TABLE `cinema`.`hall_types_has_seats` 
ADD CONSTRAINT `fk_hall_types_has_seats_hall_types1`
  FOREIGN KEY (`hall_types_id`)
  REFERENCES `cinema`.`hall_types` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_hall_types_has_seats_seats1`
  FOREIGN KEY (`seats_id`)
  REFERENCES `cinema`.`seats` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;


DELIMITER $$

USE `cinema`$$
DROP TRIGGER IF EXISTS `cinema`.`users_AFTER_INSERT` $$

USE `cinema`$$
CREATE DEFINER = CURRENT_USER TRIGGER `cinema`.`users_AFTER_INSERT` 
AFTER INSERT ON `users` FOR EACH ROW
BEGIN
	insert into cinema.profiles (users_id)
	values (new.id);
END$$

USE `cinema`$$
DROP TRIGGER IF EXISTS `cinema`.`profiles_BEFORE_UPDATE` $$


DELIMITER ;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
