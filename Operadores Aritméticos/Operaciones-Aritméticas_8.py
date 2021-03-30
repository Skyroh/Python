## PROGRAMA REALIZADO POR SKYROH

print("Este programa convierte los segundos a minutos.")

segundos = input("Introduzca la cantidad de segundos: ")

try:
    segundos = int(segundos)
    minCalc = segundos / 60
    segCalc = segundos % 60

    segundos = str(int(segundos))
    minCalc = str(int(minCalc))
    segCalc = str(int(segCalc))

    print(segundos + " son " + minCalc + " minutos y " + segCalc + " segundos.")

except ValueError:
    print("Error: Introduzca valores numéricos para su cálculo.")
