-- SQLite
/*
CREATE TABLE category (
    nombre VARCHAR not null
)
*/

CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);