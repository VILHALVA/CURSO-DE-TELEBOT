CREATE DATABASE IF NOT EXISTS database.db;

USE database.db;

CREATE TABLE IF NOT EXISTS entrevistas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age TEXT
);
