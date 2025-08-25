# Las cadenas de caracteres son (stirng)
#Secuencia de caracteres encerrados entre comillas y usados para representar texto en el programa.

#sell: que se pronuncia shel se conoce como intérprete de comandos. Es un programa que actúa entre el ususario y el sistema operativo, permitiendo ejecutar comandos para administrar archivos, procesos y programas de forma interctiva o a través de scripts
#script es un conjunto de instrucciones en un lenguaje de programacion que se ejecuta por un interprete para automatizar tareas, controlas proceso o realizar funciones especificas, sin necesidad de ser compilado previamente.

nombre = "Nora"

EOL (End On Line) fin de lineas 

5 != "5"

type(5)

type('5')

#Tamaño (Length) número de caracteres que posee
len() #Esta función nos va a retornar la longitud de caracteres.

len(nombre) # al llamar la función vemos el valor 4

#la secuencia comineza desde cero Ejemplo Python / indices / o 1 2 3 4 5
# 
# indexación: nos permite acceder  

palabra = "Python"
palabra [0] # podemos acceder con corchetes # = 'p'
palabra [1] # 'y'
palabra [2] # 't'
palabra [3] # 'h'
palabra [4] # 'o'
palabra [5] # 'n'


#Rebanado (Slicing) vamos a tomar una rebanada de la cadena de caracteres.

#Ej yth

#sintaxis <cadena> [inicio:fin] especificamos de donde a donde el fin no va a estar incluido en la rebanada

palabra[1:4] # yth

<cadena>[inicio:] #
<cadena>[:fin] #
<cadena>[:] #


<cadena>[inicio:fin:paso] # paso especifica como se va a saltar de un caracter al siguiente
#y(1) - h(3) -n(5)

palabra[1:6:2] # yhn



