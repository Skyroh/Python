## PROGRAMA REALIZADO POR SKYROH

print("Programa que convierte las pulgadas a centímetros.")

pulgadas = input("Introduce la cantidad de pulgadas: ")

try:
    pulgadas = float(pulgadas)
    centimetros = pulgadas * 2.54

    pulgadas = str(pulgadas)
    centimetros = str(centimetros)
    print(pulgadas + " pulgadas son " + centimetros + " centimetros.")

except ValueError:
    print("Error: Introduce valores numeéricos para poder realizar la conversión.")

    