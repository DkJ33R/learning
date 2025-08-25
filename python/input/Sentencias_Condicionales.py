# Sentencias condicionales // Es una instrucción o un grupo de instrucciones cuya ejecución depende del valor de una condición booleana.


Lógica básica de un condicional

                       v  !
 Verdadera         Condición           Falsa  
v

 Instrucciones
v

                       v


#SIntaxis

if <condición>: # Si esta condición es verdadera
    #Código     # Ejecuta este código. // El Código tiene que estar indentado


temp = 15
if temp < 25:
    print("Frío")   # Se imprime en pantalla Frío


Cláusula 'else' # Si la condición es falsa // Sino 


Lógica Básica de un condicional con una clausula else

                           v
                           if
                           v
 Verdadera             Condición             Falsa
v                                                v

Instrucciones #Ejecuta el código               else

                           v
                           Se sale


if <condición>:
    # Código
else:
    # Código

Ej: 

temp = 15

if temp < 25:
    print('Frío') # Como menor de 25 se imprime esta
else:
    print('Calor') # si temp es 35 entonces es mayor que 25 y se imprime Calor


if <condición1>: # Si es Falsa
    # Código
elif <condicion2>: # Si es Verdadera // Entonces (Nos permite especificar más condiciones)
    # Código
else:                                      #// Si no
    # Código


Ej temp = 0

if temp <= 0:
    print("Muy Frío")
elif temp < 25:
    print("Frío")
else:
    print("Calor")

Puede haber más de una cláusula 'elif', pero solo una cláusula 'else'.

if <condición1>: # Si es Falsa
    # Código
elif <condicion2>: # Si es Verdadera // Entonces (Nos permite especificar más condiciones)
    # Código
elif <condicion3>:# Si es Verdadera // Entonces (Nos permite especificar más condiciones)
    # Código
elif <condicion4>:# Si es Verdadera // Entonces (Nos permite especificar más condiciones)
    # Código
else:                                      #// Si no
    # Código



