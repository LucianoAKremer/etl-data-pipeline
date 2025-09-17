-- 1 Crear la base de datos
CREATE DATABASE etl_db;

-- 2 Crear el usuario del proyecto
CREATE USER etl_user WITH ENCRYPTED PASSWORD 'etl_password';

-- 3 Dar permisos al usuario sobre la base
GRANT ALL PRIVILEGES ON DATABASE etl_db TO etl_user;

-- 4 Crear un esquema exclusivo para el proyecto
CREATE SCHEMA etl_schema AUTHORIZATION etl_user;

-- 5 Dar permisos de uso y creación en el esquema
GRANT USAGE, CREATE ON SCHEMA etl_schema TO etl_user;

-- 6 Dar permisos por defecto para futuras tablas dentro del esquema
ALTER DEFAULT PRIVILEGES IN SCHEMA etl_schema
GRANT ALL ON TABLES TO etl_user;

-- 7 Crear la tabla posts dentro del esquema
CREATE TABLE IF NOT EXISTS etl_schema.posts (
    userId INT,
    id INT PRIMARY KEY,
    title TEXT,
    body TEXT
);
