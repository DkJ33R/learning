Para iterar sobre: 
    Cadenas de caracteres
    Listas
    Tuplas
    Diccionarios
    Otros...

Elemtno ---> Variable de control

for <var> in <iterable>: # Lista, Tupla, Cadena de Caracteres, diccionario
    # Código

Ejemplo:

for char in "Loops":
    iteration   char
         1       'L'
         2       'o'
         3       'o'
         4       'p'
         5       's'
    
Ej:

for char in "Loops":
    print(char)

L
o
o
p
s


for num in [1, 2, 3]:
    print(num)

1
2
3

Diccionarios

letras = {"a",: 1, "b": 2}

for clave in letras:
    print(clave)

a
b

for valor in letras.values():
    print(valor)

1
2

for clabe, valor in letras.items():
    print(clave, valor)

a 1
b 2

