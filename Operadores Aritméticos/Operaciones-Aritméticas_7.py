## PROGRAMA REALIZADO POR SKYROH

print("Este programa convierte los grados Fahrenheit a Celsius)")

fahrenheit = input("Escriba una temperatura en grados Fahrenheut: ")

try: 
    fahrenheit = float(fahrenheit)
    celsius = (fahrenheit - 32 ) / 1.8

    fahrenheit = str(int(fahrenheit))
    celsius = str(int(celsius))
    print(fahrenheit + "ºF son " + celsius + "ºC")

except ValueError:
    print("Error: Introduzca únicamente valores numéricos para su cálculo.")
