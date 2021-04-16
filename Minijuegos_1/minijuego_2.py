## PROGRAMA REALIZADO POR SKYROH

print("JUEGO DE DADOS (2)")

carmen1 = input("CARMEN: Introduzca tu primera tirada: ")
carmen2 = input("CARMEN: Introduzca tu segunda tirada: ")

david1 = input("DAVID: Introduzca tu primera tirada: ")
david2 = input("DAVID: Introduzca tu segunda tirada: ")

try:
    carmen1 = int(carmen1)
    carmen2 = int(carmen2)
    david1 = int(david1)
    david2 = int(david2)

    listaCarmen = [carmen1, carmen2]
    listaDavid = [david1, david2]

    maxCarmen = max(listaCarmen, key = int)
    maxDavid = max(listaDavid, key = int)

    if maxCarmen == maxDavid :
        print("¡Han empatado!")
    

    elif maxCarmen > maxDavid:
        print("¡Ha ganado Carmen!")
    
    else:
        print("¡Ha ganado David!")
   
except ValueError:
    print("Error.")