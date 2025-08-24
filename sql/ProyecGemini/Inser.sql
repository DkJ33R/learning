-- Inserta datos de ejemplo
INSERT INTO Departamentos (nombre_departamento) VALUES ('Ventas');
INSERT INTO Departamentos (nombre_departamento) VALUES ('Marketing');


-- Comentario: Este tipo de subconsulta es idéntica en SQL Server.
-- Para cada fila de la tabla externa (E1), la subconsulta se ejecuta de nuevo.
SELECT
    nombre,
    salario,
    id_departamento
FROM
    Empleados AS E1
WHERE
    salario > (SELECT AVG(salario) FROM Empleados AS E2 WHERE E2.id_departamento = E1.id_departamento);