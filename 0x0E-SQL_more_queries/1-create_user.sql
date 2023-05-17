-- Creates a user with a password and set all privileges to him
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED WITH mysql_native_password
BY 'user_0d_1_pwd';

GRANT ALL
ON *.*
TO user_0d_1@localhost;
