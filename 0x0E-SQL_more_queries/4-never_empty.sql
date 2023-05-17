-- Creates a table in the current database if doesn't exists with some constraints
CREATE TABLE IF NOT EXISTS id_not_null (
	id INT NOT NULL DEFAULT 1,
	name VARCHAR(256)
);
