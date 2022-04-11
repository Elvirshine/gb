-- Заполним таблицу возрастных цензов на фильмы. (+)
INSERT INTO cinema.age_limites (ages) VALUES
  ('0+'),
  ('6+'),
  ('12+'),
  ('16+'),
  ('18+');
 SELECT * FROM cinema.age_limites;
 
 -- Таблица жанров (+)
 INSERT INTO cinema.film_formats (name) VALUES
  ('фантастика'),
  ('боевик'),
  ('приключения'),
  ('ужасы'),
  ('триллер'),
  ('комедия'),
  ('драма'),
  ('мелодрама'),
  ('документальный'),
  ('криминальный');
 SELECT * FROM cinema.film_formats;
 
 -- Таблица пользователей (+)
 INSERT INTO cinema.users (phone, email, password_hash, updated_at, deleted_at) VALUES
  ('79170000000', 'a@mail.ru', sha1('a@mail.ru'), null, null),
  ('79170000001', 'b@mail.ru', sha1('b@mail.ru'), null, null),
  ('79170000002', 'c@mail.ru', sha1('c@mail.ru'), null, null),
  ('79170000003', 'd@mail.ru', sha1('d@mail.ru'), null, null),
  ('79170000004', 'e@mail.ru', sha1('e@mail.ru'), null, null);
SELECT * FROM cinema.users;

-- Таблица профили (+)
update cinema.profiles
	set firstname = 'Marina', lastname = 'Black', gender = 'female', birthday_at = '1992-10-06', city = 'Moscow'
	where users_id = (SELECT id FROM cinema.users where id = 1);
update cinema.profiles
	set firstname = 'Max', lastname = 'White', gender = 'male', birthday_at = '1983-11-26', city = 'Kazan'
	where users_id = (SELECT id FROM cinema.users where id = 2);
update cinema.profiles
	set firstname = 'Jane', lastname =  'Potter', gender = 'female', birthday_at = '1988-06-29', city = 'Kazan'
	where users_id = (SELECT id FROM cinema.users where id = 3);
update cinema.profiles
	set firstname = 'Maxin', lastname = 'Whiter', gender = 'female', birthday_at = '1973-12-17', city = 'Kazan'
	where users_id = (SELECT id FROM cinema.users where id = 4);
update cinema.profiles
	set firstname = 'Ivan', lastname = 'Ivanov', gender = 'male', birthday_at = '2002-08-01', city = 'Moscow'
	where users_id = (SELECT id FROM cinema.users where id = 5);    
SELECT * FROM cinema.profiles;

-- Таблица фильмы имеют форматы (+)
INSERT INTO cinema.filmes_has_formats (filmes_id, film_formats_id) VALUES
  (1, 3), (1, 4), (1, 6)
  , (2, 2), (2, 5), (2, 4), (2, 8)
  , (3, 1), (3, 7), (3, 8), (3, 2), (3, 10);
SELECT * FROM cinema.filmes_has_formats;

-- Таблица медиа личности (+)
INSERT INTO cinema.media_persons (firstname, lastname, profession) VALUES
  ('Катрина', 'Балф', 'актриса')
  , ('Сэм', 'Хьюэн', 'актер')
  , ('Софи', 'Скелтон', 'актриса')
  , ('Ричард', 'Ранкин', 'актер')
  , ('Данкан', 'Лакруа', 'актер')
  , ('Сезар', 'Домбой', 'актер')
  , ('Тобайас', 'Мензис', 'актер')
  , ('Джон', 'Белл', 'актер')
  , ('Лорен', 'Лайл', 'актриса')
  , ('Метин', 'Хусейн', 'режиссер')
  , ('Стивен', 'Вульфенден', 'режиссер')
  ;
SELECT * FROM cinema.media_persons;

-- Таблица типов залов (+)
INSERT INTO cinema.hall_types (name, seats_count, rows_count, seats_row) VALUES
  ('2D/3D', 100, 10, 10),
  ('VIP', 10, 5, 2),
  ('Комфорт', 20, 5, 4),
  ('Dolby Atmos', 100, 10, 10),
  ('Atmos Комфорт', 20, 5, 4),
  ('IMAX', 120, 10, 12 ),
  ('D-BOX', 10, 5, 2),
  ('Детский зал', 40, 5, 8);
SELECT * FROM cinema.hall_types;

-- Таблица медиа типов (+)
INSERT INTO cinema.media_types (name) VALUES
  ('Трейлер')
  , ('Постер')
  ;
SELECT * FROM cinema.media_types;

-- Таблица фильмов(+)
INSERT INTO cinema.filmes (name, media_type, age_limite_id, film_format, film_duration, beginning, country, directors, actors, description) VALUES
  ('Чужестранка', 1, 5, 1, 125, now(), 'Великобритания', 10, 1, 'аопрдлжжлаенгшщ')
  , ('Гарри Поттер', 3, 1, 2, 155, now(), 'Великобритания', 9, 5, 'аопрдлжжлаееаввчснгшщ')
  , ('Хоббит', 2, 2, 1, 130, now(), 'США', 10, 3, 'аопроиолддбпрдлжжлаенгшщ')
  ;
SELECT * FROM cinema.filmes;

-- Таблица тип билета (+)
INSERT INTO cinema.ticket_type (type) VALUES
  ('adults')
  , ('children')
  ;
SELECT * FROM cinema.ticket_type;

-- Таблица харектеристики и стоимости мест (+)
INSERT INTO cinema.seats (hall_type, place_types, price, seat_number, rows_number) VALUES
  (1,'Эконом', 170, 1, 1)
  , (1,'Эконом', 170, 2, 1)
  , (1,'Эконом', 170, 3, 1)
  , (1,'Комфрот', 170, 4, 1)
  , (1,'Комфорт', 170, 5, 1)
  , (1,'Комфорт', 170, 6, 1)
  , (1,'Комфорт', 170, 7, 1)
  , (1,'Эконом', 170, 8, 1)
  , (1,'Эконом', 170, 9, 1)
  , (1,'Эконом', 170, 10, 1)
  , (2,'VIP', 300, 1, 1)
  , (2,'VIP', 300, 2, 1)
  , (3,'Комфорт', 250, 1, 1)
  , (3,'Комфорт', 250, 2, 1)
  , (3,'Комфорт', 250, 3, 1)
  , (3,'Комфорт', 250, 4, 1)
  , (7,'DBOX', 300, 1, 2)
  ;
SELECT * FROM cinema.seats;

-- Таблица заказов (+)
INSERT INTO cinema.orders (profiles_users_id, filmes_id, seats_id, 
ticket_type_id, seats_price, created_at, cancel_date) VALUES
  (5, 3, 17, 1, 300, now(), null)
  , (3, 2, 4, 1, 170, now(), null)
  , (1, 1, 15, 1, 250, now(), null)
  , (3, 2, 5, 2, 170, now(), null)
  ;
SELECT * FROM cinema.orders;

-- Таблица мест в залах (+)
INSERT INTO cinema.hall_types_has_seats (hall_types_id, seats_id) VALUES
  (1, 1), (1, 2), (1, 3), (1, 4), (1, 5),(1, 6)
  , (1, 7), (1, 8), (1, 9), (1, 10),(2, 1), (2, 2)
  , (3, 1),(3, 2), (3, 3), (3, 4), (7, 1);
SELECT * FROM cinema.hall_types_has_seats;

-- Таблица у фильмов есть медиа типы (+)
INSERT INTO cinema.filmes_has_media_types (filmes_id, media_types_id) VALUES
  (1, 1), (1, 2)
  , (2, 1), (2, 2)
  , (3, 1),(3, 2)
  ;
SELECT * FROM cinema.filmes_has_media_types;

-- Таблица у фильмов есть медиа персоны (+)
INSERT INTO cinema.filmes_has_media_persons (filmes_id, media_persons_id) VALUES
  (1, 1), (1, 2), (1, 3), (1, 11)
  , (2, 3), (2, 4), (2, 5), (2, 10)
  , (3, 6),(3, 7), (3, 8), (3, 11)
  ;
SELECT * FROM cinema.filmes_has_media_persons;

-- Таблица филиалы (+)
INSERT INTO cinema.filiales (city, address, hall_types_id) VALUES
  ('Москва', 'Кукушкина 2', 1),
  ('Москва', 'Кукушкина 2', 2),
  ('Москва', 'Кукушкина 2', 3),
  ('Москва', 'Кукушкина 2', 4),
  ('Москва', 'Кукушкина 2', 5),
  ('Москва', 'Кукушкина 2', 6),
  ('Москва', 'Кукушкина 2', 7),
  ('Москва', 'Кукушкина 2', 8),
  ('Казань', 'Птичкина 3', 1),
  ('Казань', 'Птичкина 3', 2),
  ('Казань', 'Птичкина 3', 3),
  ('Казань', 'Птичкина 3', 4),
  ('Казань', 'Птичкина 3', 5),
  ('Казань', 'Птичкина 3', 6),
  ('Казань', 'Птичкина 3', 7),
  ('Казань', 'Птичкина 3', 8);
SELECT * FROM cinema.filiales;