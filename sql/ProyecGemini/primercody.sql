
-- Elimina la tabla 'Empleados' si ya existe
-- Esto te permite ejecutar el script completo una y otra vez sin errores.
-- DROP TABLE IF EXISTS Empleados;

-- Aquí ya no incluyes el comando CREATE TABLE.
-- Solo los comandos para manipular los datos.
-- Puedes ejecutar estas líneas tantas veces como quieras sin errores.


INSERT INTO Empleados (nombre, salario, fecha_contratacion)
VALUES ('Juan Pérez', 60000.00, '2022-01-15');

SELECT * FROM Empleados;








