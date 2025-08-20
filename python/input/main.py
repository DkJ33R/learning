"""name = input("Ingresa tu nombre: ")
user_age = int(float(input("Ingresa tu edad: ")))
future = user_age + 10

print(f'''Hola {name}, 
tienes {user_age} actualmente,
y dentro de 10 años tendrás {future}''')

"""
"""
operator = input("teclea el operador que quieres realizar. Ej: + para suma. ")
num1 = int(input("Ingresa un número: ")) #int antes del input con string es para converir el string a int.
num2 = int(input("Ingresa otro número: "))
resultado = 0
if (num2 == 0 and operator == "/"):
    print("No puedes dividir por Zero, Fofi")
else:
    if (operator == "+"):
        resultado = num1 + num2
    elif(operator == "-"):
        resultado = num1 - num2
    elif(operator == "*"):
        resultado = num1 * num2
    elif(operator == "/"):
        resultado = num1 / num2

    print(f'''
        {num1}
    {operator}   {num2}
    -------------------------------------------
    El resultado de la suma es = {resultado}
    ''')

"""

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