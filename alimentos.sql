CREATE TABLE alimentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    precio REAL,
    marca TEXT
);

INSERT INTO alimentos (nombre, precio, marca) VALUES ('Manzana', 1.5, 'Marca A');
INSERT INTO alimentos (nombre, precio, marca) VALUES ('Banana', 2.0, 'Marca B');
INSERT INTO alimentos (nombre, precio, marca) VALUES ('Yogurt', 1.0, 'Marca C');