-- Comentario: Las funciones de agregación como COUNT, SUM, AVG, MIN, y MAX
-- tienen la misma sintaxis en SQL Server.
-- GROUP BY también funciona de manera idéntica.
SELECT
    D.nombre_departamento,
    COUNT(E.id_empleado) AS total_empleados,
    AVG(E.salario) AS salario_promedio
FROM
    Empleados AS E
INNER JOIN
    Departamentos AS D ON E.id_departamento = D.id_departamento
GROUP BY
    D.nombre_departamento;