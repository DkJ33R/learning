# Un programa de calculadora simple

# 1. Pedir los números al usuario
# Recuerda que input() devuelve un texto, por lo que debes convertirlo a un número
msm = print("Bienvenido a la Calculadora Mágica")

# Pedir el primer número de forma segura
while True:
    try:
        num1 = int(input("Introduce el primer número: "))
        break # Si la conversión es existosa, sal del bucle
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número entero.")

#Pedir el segundo número de forma segura 
while True:
    try:
        num2 = int(input("Introduce el segundo número: "))
        break # Si la conversión es exitosa, sal del bucle
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número entero")


# 2. Realizar y mostrar las operaciones
# a) Suma
suma = num1 + num2
print(f"La suma es: {suma}")

# b) Resta
resta = num1 - num2
print(f"La resta es: {resta}")

# c) Multiplicación
multiplicacion = num1 * num2
print(f"La multiplicación es: {multiplicacion}")

# d) División - ahora con un condicional para evitar el error
if num2 != 0:
    division = num1 / num2
    print(f"La división es: {division}")
else:
    print("No se puede dividir por cero.")
# e) Módulo (el resto de una división)
if num2 != 0:
    modulo = num1 % num2
    print(f"El módulo es: {modulo}")
else:
    print("El módulo no se puede calcular con cero")