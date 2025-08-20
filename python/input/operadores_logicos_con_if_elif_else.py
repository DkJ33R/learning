user_name = input("¿Cómo te llamas?: ")
nota1 = int(input("Escribe el resultado final de tu examen (1-100): "))
nota2 = int(input("Escribe la nota que tienes por realizar tus tareas (1-100): "))

# Definimos la nota mínima para aprobar y la de excelencia
nota_minima_para_aprobar = 70
nota_excelente = 90

# Calculamos el promedio
promedio = (nota1 + nota2) / 2

# Determinamos el estado del estudiante usando condicionales
if promedio >= nota_excelente:
    estado = "¡Tienes una calificación excelente y aprobaste!"
elif promedio >= nota_minima_para_aprobar:
    estado = "Aprobaste el curso. ¡Felicidades!"
else:
    estado = "No aprobaste. ¡Ánimo y a seguir intentando!"

print("---")
print(f"Hola, {user_name}.")
print(f"Tu promedio final es: {promedio}")
print(f"Por lo tanto, {estado}")
print("---")