-- Comentario: Las subconsultas funcionan igual en SQL Server.
-- Primero, calculamos el salario promedio en la subconsulta.
SELECT
    nombre,
    salario
FROM
    Empleados
WHERE
    salario > (SELECT AVG(salario) FROM Empleados);