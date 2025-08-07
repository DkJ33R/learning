"""name = input("Ingresa tu nombre: ")
user_age = int(float(input("Ingresa tu edad: ")))
future = user_age + 10

print(f'''Hola {name}, 
tienes {user_age} actualmente,
y dentro de 10 años tendrás {future}''')
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
