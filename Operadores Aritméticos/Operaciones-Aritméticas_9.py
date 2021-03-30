## PROGRAMA REALIZADO POR SKYROH

print("Este programa convierte los segundos a Horas, minutos y segundos.")

segundos = input("Introduzca la cantidad de segundos :")

try:
    segundos = float(segundos)

# SE DIVIDE ENTRE 3600 YA QUE SON LOS SEGUNDOS DE 1 HORA.
    horCalc =  segundos / 3600
    restoSeg = segundos % 3600
    minCalc = restoSeg / 60
    segCalc = restoSeg % 60

    segundos = str(int(segundos))
    horCalc = str(int(horCalc))
    minCalc = str(int(minCalc))
    segCalc = str(int(segCalc))

    print(segundos + " segundos son " + horCalc + " horas, " + minCalc + " minutos  y " + segCalc + " segundos")

except ValueError:
    print("Error: Introduce un valor numérico para poder realizar el cálculo.")
