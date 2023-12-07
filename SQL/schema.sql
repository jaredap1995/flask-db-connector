CREATE DATABASE strongapp;

DROP TABLE IF EXISTS users; 
CREATE TABLE raw_data(
    id serial primary key,
    first_name varchar(256) NOT NULL,
    last_name varchar(256) NOT NULL,
    username varchar(256) NOT NULL,
    email varchar(256) NOT NULL,
    password varchar(256) NOT NULL,
    phone varchar(20)
);
