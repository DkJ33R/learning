# Ejercicio 10 - Adivina el número (máx. 7 intentos)
import random

secret_num = random.randint(1, 100)
intentos = 0;
mayor_intentos = 7


while intentos < mayor_intentos:
    try:
        user_num = int(input("Adivina el número secreto: "))
        intentos += 1

        if user_num < secret_num:
            print('Número bajito. Intenta de nuevo.')
        elif user_num > secret_num:
            print('Tu número está alto. Intenta de nuevo.')
        else:
            break
    except ValueError:
        print('No ingresaste un Número inválido. Por favor, introduce un número.')

if user_num == secret_num:
    print(f'¡Felicitaciones! Adivinaste en {intentos} intentos')
else:
    print(f'Perdiste. El número era {secret_num}.')
""""

"""""
# Ejercicio 9-- Factorial con for y while 


n = int(input("Ingresa un número entero para calcular su factorial: "))

factorial_while = 1
contador = 1

while contador <= n:
    factorial_while *= contador
    contador += 1

print(f"El factorial de {n} (con 'while') es: {factorial_while}")

lista_numeros = [245, 87, 103, 506]

    print(f"\nProcesando el número: {numero}")
    suma_digitos = 0
    temp_numero = numero

    while suma_digitos < 10:
        digito = temp_numero % 10
        suma_digitos += digito 
        temp_numero //= 10
        if temp_numero == 0 and suma_digitos < 10:
            print(f"  La suma de los dígitos es {suma_digitos}, y es menor que 10.")
            break

    print(f"  Proceso terminado para {numero}. Suma final de dígitos: {suma_digitos}")

#Ejercicio 8  Suma hasta fin
suma_total = 0
cantidad_numeros = 0

print("Ingresa números enteros. Escribe 'fin' cuando hayas terminado.")

while True:
    entrada = input("> ")

    if entrada.lower() == 'fin':
        break
    try:
        numero = int(entrada)
        suma_total += numero
        cantidad_numeros += 1

    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número entero o 'fin'.")

print(f"Suma total: {suma_total}")
print(f"Cantidad de números: {cantidad_numeros}")

#Ejercicio 7
for numero in range(1, 101):
    salida = ""

    # Usamos el operador % para verificar si es múltiplo
    if numero % 3 == 0:
        salida += "Fizz"

    if numero % 5 == 0:
        salida += "Buzz"

    # Si la cadena está vacía, no es múltiplo de 3 ni de 5
    if salida == "":
        print(numero)
    else:
        print(salida)

"""