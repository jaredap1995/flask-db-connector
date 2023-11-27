CREATE DATABASE strongapp;

CREATE TABLE users(
    id serial primary key,
    username varchar(256),
    email varchar(256),
    password varchar(256)
);

INSERT INTO users values ('name', 'email', 'password')