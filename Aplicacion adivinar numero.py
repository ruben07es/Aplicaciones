from ast import Break
from random import random


from random import *

nombre = input ('Hola, ¿como te llamas? ')

print (f'Encantado {nombre.capitalize()} he pensado un número del 1 al 100 \n y tienes 8 intentos para adivinarlo\n ¿QUIERES JUGAR?\n')

intentos = 0
numero = randint(0,101)


while intentos < 8:
    respuesta = int(input ('¿Cuál es tu apuesta? '))
    if respuesta in range (0,101):
        if respuesta == numero:
            intentos += 1
            print (f'Enhorabuena {nombre.capitalize()}, vaya fenómeno has acertado a la {intentos} oportunidad')
            break
        elif respuesta != numero:
            intentos += 1
            if respuesta < numero:
                print (f'Lo siento mucho {nombre.capitalize()} pero has fallado, el numero secreto es mayor que {respuesta}, te quedan {8 - intentos} intentos')
            elif respuesta > numero:
                print (f'Lo siento mucho {nombre.capitalize()} pero has fallado, el numero secreto es menor que {respuesta}, te quedan {8 - intentos} intentos')
    elif respuesta not in range (0,101):
        print ('Debes ingresar un número entre 0 y 100')