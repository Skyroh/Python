## PROGRAMA REALIZADO POR SKYROH

import random 

def NumeroRandom():
    global x
    x = (random.randint(1, 10))
    return x
    
UsrNum = input("Introduce un número aletrorio entre 1 y 10: ")

try:
    UsrNum = int(UsrNum)
    if UsrNum >= 1 and UsrNum <= 10:
        numeroRandom = NumeroRandom()
        if numeroRandom == UsrNum:
            print("¡Enhorabuena! Has acertado el número")

        else:
            UsrNum = str(UsrNum)
            numeroRandom = str(int(numeroRandom))
            print("Mala suerte, has escogido el número " + UsrNum + " y el número aleatorio ha sido el " + numeroRandom + ".")   
    else:
        print("Error, introduzca valores entre 1 y 10.")

except ValueError:
    print("Error, introduzca valores numéricos.")







