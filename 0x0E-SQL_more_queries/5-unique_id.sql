-- Creates a table in the current database if doesn't exists with some constraints
CREATE TABLE IF NOT EXISTS unique_id (
	id INT UNIQUE NOT NULL DEFAULT 1,
	name VARCHAR(256)
);
