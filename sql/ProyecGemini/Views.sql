-- Comentario: La sintaxis de CREATE VIEW es la misma en SQL Server.
CREATE VIEW VistaSalariosAltos AS
SELECT nombre, salario
FROM Empleados
WHERE salario > 70000;

-- Para usar la vista, solo la consultas como si fuera una tabla normal.
SELECT * FROM VistaSalariosAltos;