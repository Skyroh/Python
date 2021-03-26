## PROGRAMA REALIZADO POR SKYROH
import colorama
from colorama import Fore, Style
numeroDNI = 00000000

## MENSAJE DEL PROGRAMA
print ("Programa para identificar la letra del DNI \n(Documento nacional de Identidad)")
print()

## RECOGIDA DE DATOS
numeroDNI = input("Introduzca los números del documento:")

## CÁLCULO DE LA LETRA Y CONTROL DE EXCEPCIONES
if numeroDNI.isdigit() and len(numeroDNI) == 8:
    numeroDNI = int(numeroDNI)
    letraDNI = numeroDNI % 23
    letras = ("T","R","W","A","G","M","Y","F","P","D","X","B")
    
    for x in range (1, len(letras)):
        if letraDNI == x:
            numeroDNI = str(numeroDNI)
            print(Fore.YELLOW + "Tu DNI con letra es " + numeroDNI + letras[x])

else:
    print(Fore.RED+"Error: Introduzca los 8 digitos del documento.")








