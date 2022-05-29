CREATE TABLE `logs` (
  id SERIAL,
  tables_id int,
  tables_name VARCHAR(255),
  `names` VARCHAR(255),
  created_at DATETIME DEFAULT current_timestamp
) ENGINE=ARCHIVE;