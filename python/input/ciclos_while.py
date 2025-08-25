# Cliclos while

Ciclo que continúa mientras una condición es verdadera y se detiene cuando es falsa

    Si tenenmos que detener manualmente o la computadora lo debe detener se dara un ciclo infinito

while <condición>:
    #Código  /// Indentación. representada por 4 espacios


#Iteraciones
UN Ciclo while no tiene un número fijo o predeterminado de iteraciones

Se ejecuta hasta que la condición es falsa


                                       I
                                       v
<--------- False ------------------Evaluar condición <---------
i                                                              i
i                                         v  True              i
i                                                              i
i                                        Instrucciones_________i_
i
i
i--------------------------------------> Ciclo se Detiene
                                               i
                                               v
                                              Fin


Las variables de COntrol

Los ciclos while no actualizan la(s) variables(s) de control automaticamente

Deben ser actualizadas en el cuerpo del Ciclo

Ej: 

x = 20

while x < 35:    # 35 false
        print(x) # 32
        x += 3   # 35


Si ciclo infinito KyboardInterrupt 
