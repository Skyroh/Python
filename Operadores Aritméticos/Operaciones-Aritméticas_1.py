## PROGRAMA REALIZADO POR SKYROH

import colorama
from colorama import Fore, Style

numeroUno = 0
numeroDos = 0

print("Programa para calcular la media aritmética de dos numeros.")
numeroUno = input("Introduce le valor del primer número:")
numeroDos = input("Introduce le valor del segundo número:")

if numeroUno.isdigit() and numeroDos.isdigit():
    numeroUno = int(numeroUno)
    numeroDos = int(numeroDos)
    calculo = ( numeroUno + numeroDos) / 2
    calculo = str(calculo)
    print ("El resultado de la media aritmética es :" + calculo )
else:
    print("Error: El programa solo admite valores numericos.")
