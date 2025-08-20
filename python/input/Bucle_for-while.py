# Un pequeño programa para empezar

# 1. Pide el nombre y la edad del usuario
nombre = input("¿Cuál es tu nombre? ")
# Haz que el usuario ingrese su edad y conviértela a un número
edad = int(input("Cuál es tu edad: "))

# 2. Bucle 'for' para mostrar un mensaje varias veces
print(f"¡Hola, {nombre}! Aquí tienes una cuenta regresiva:")
for i in range(5, 0, -1):
    print(i)

# 3. Bucle 'while' para pedir una contraseña
contraseña = ""
while contraseña != "123":
    contraseña = input("Introduce la contraseña para continuar: ")
print("Contraseña correcta. ¡Bienvenido!")

# 4. Condicionales para tomar una decisión
if edad >= 18:
    print(f"{nombre}, eres mayor de edad.")
else:
    print(f"{nombre}, eres menor de edad.")