#operadores Son esenciales para escribir cualquier programa en Python
Qué es un operador? # Son S´+imbolos que denotan un operación.

# Operandos 
Son Valores con los cuales se ejecuta la operación

#Se Juantan para formar una expresión
Operador + Operandos = Expresión

#¿Qué es una expresión?
Una expresión es un combinación de valores, variables, y operadores que al ser evaluados resultan en un valor.

Se evalua una expresi+ón para obtener un valor final

#Excepto cuando ciertos operadores tienen mayor "importancia" para el orden de las operaciones.

#Cuatro tipos principales de Operadores:

#Aritméticos

Nos permite realizar operaciones aritméticas en el programa.

suma + suma ambos operandos para obtener un resltado final (expresión)

puede sumar cadena de caracteres concatenandolas (unir cadena de caracteres para formar una sola) "Hola" + "Mundo" == 'Hola mundo'

Resta -

Multiplicación *

División / # Aquí el resultado siempre es en ,flotante - siempre retorna un número en coma-flotante

División Entera // #Tenemos que usar este simbolo si queremos tener un resultado en ENTERO

Exponente ** # 5**3 elevando 5 a la 3 que su resultado sería 125

16 ** (1/2) raiz cuadrada 4.0 # Podemos obtener la raiz cuadrada de un número elevandolo a un medio
y todo número elevado a 0 da como resultado 1 5**0

Módulo % # Retorna el resto de la división # muy usado para retornar si un número es para o impar

Ej: 5//2 = 1 (Es impar) 

El acronimo que nos facilita utilizar las operaciones

PEMDAS

P ()
E **
M *
D /
A +
S -


#OPERADORES LÓGICOS

Nos permiten trabajar con valores booleanos (True y False).

and #Reglas /Evalua si el operando izquierdo y el derecho son verdaderos. Y dependiendo de eso retorna verdadero o falso

Ej: x and y (Va a evaluar a verdadero solamente si ambas son verdaderas)
___________________________
True Table
---------------------------
x       y      x and y
True   True    True
True   False   False
False  True    False
False  False   False

Ej: (5 < 6) and (6 > 8) # False
       T           F


or #Reglas /Nos permite conectar 2 expresiones más pequeñas // Cuando uno de los 2 es verdadero el resultado final es verdadero
x or y

______________________
True Table
----------------------
x      y    x or y
True  True   True
True  False  True
False True   True
False False  False

Ej:  (5 < 6) or (6> 8) # True
        T          F



not # Lo que hace es negar el valor de esta expresion / Si la expresión es verdadera el resultado es falso

___________________
True Table
---------------------
x     not x
True  False
Fasle True

not True # False

not False # True



En cuanto a prioridad:

not Mayor (primero van a ser evaluadas)

and

or  Menor


Operadores relacionales # Son utiliozados para comparar valores y ellos retornan un valor booleano.

> Mayor que

< Menor que

== Igual (Comparando valores) extrictamente igual

>= Mayor o igual que

<= Menor o igual que

!= No igual a 

Ej    5             >           6             # False
 operando_Izq    Operador    Operando_Der


#Operadores de asignación

Son utilizados para asignar valores a las variables del programa 

realiza la operacion correspondiente con la variable y luego le asigna el valor obtenido

=

-=

+=

*=

/=

**=

%=

Ej: 

edad = 56
edad = += 3
edad # 59







#Lógicos

#De asignación

#Relación







"""""
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

