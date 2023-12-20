--Lis all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).
CREATE USER 'user_0d_1'@'localhost';

-- Otorgar privilegios a 'user_0d_1'
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Crear el usuario 'user_0d_2'
CREATE USER 'user_0d_2'@'localhost';

-- Otorgar privilegios a 'user_0d_2'
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_2'@'localhost';

-- Mostrar privilegios de 'user_0d_1' y 'user_0d_2'
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';

