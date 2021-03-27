## PROGRAMA REALIZADO POR SKYROH

print("Convertidor de pies y pulgadas a centímetros.")

pies = input("Introduce la cantidad de pies: ")
pulgadas = input("Introduce la cantidad de pulgadas: ")


# CONVERSIÓN DE LAS UNIDADES A CENTÍMETROS
try:
    pies = int(pies)
    pulgadas = int(pulgadas)
    centimetros = ((pies * 12)+pulgadas)* 2.54
    pies = str(pies)
    pulgadas = str(pulgadas)
    centimetros = str(centimetros)

    print(pies + " pies y " + pulgadas + " pulgadas son " + centimetros + "cm.")
except ValueError:
    print("Error: Introduce solamente numeros para poder realizar el cálculo.")