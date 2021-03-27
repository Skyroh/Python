## PROGRAMA REALIZADO POR SKYROH

print("Programa que te calcula el índice de masa corporal (IMC).")
peso = input("¿Cuánto pesa?(Kg)")
altura = input("¿Cuánto mide en metros?(m)")
try:
    peso = int(peso)
    altura = float(altura)
    imc = (peso/altura)**2
    if imc >= 25:
        print("Su índice de masa corporal es alto "+ imc + ", los valores normales deben estar entre 20 y 25.")
    else:
        print(imc)
        print("Enhorabuena, su índice de masa corporal es adecuado.")

# CONTROLAMOS EL ERROR DE CÁLCULO POR SI EL USUARIO INTRODUCE OTROS CARÁCTERES.
except ValueError:
  print("Error, introduzca únicamente valores numéricos.")
