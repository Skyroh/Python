## PROGRAMA REALIZADO POR SKYROH

print("Convertidor de pies a centímetros.")

pies = input("Introduzca el número de pulgadas: ")

try:
    pies = float(pies)
    centimetros = (pies * 12)* 2.54
    pies = str(int(pies))
    centimetros = str(centimetros)
    print(pies + " pies son " + centimetros +" centimetros.")

except ValueError:
    print("Error: Introduzca valores numéricos para poder realizar la conversión.")