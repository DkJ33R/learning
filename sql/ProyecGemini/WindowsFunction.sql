-- Comentario: SQL Server también soporta funciones de ventana con una sintaxis similar.
-- RANK() es una función de ventana que clasifica las filas.
-- OVER() define la "ventana" o el conjunto de filas sobre el que se aplica la función.
SELECT
    nombre,
    salario,
    -- Asigna un rango a cada empleado basado en su salario.
    RANK() OVER (ORDER BY salario DESC) AS ranking_salario
FROM
    Empleados;