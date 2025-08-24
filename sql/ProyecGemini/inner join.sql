-- Comentario: La sintaxis de INNER JOIN es idéntica en SQL Server.
-- Une las tablas 'Empleados' y 'Departamentos'
SELECT
    E.nombre,
    D.nombre_departamento
FROM
    Empleados AS E -- El uso de alias es una buena práctica en ambos sistemas.
INNER JOIN
    Departamentos AS D ON E.id_departamento = D.id_departamento;