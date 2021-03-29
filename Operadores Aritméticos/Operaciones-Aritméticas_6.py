## PROGRAMA REALIZADO POR SKYROH

print("Este programa convierte los grados Celsius a Fahrenheit.")

celsius = input("Introduce los grados Celsius: ")

try:
    celsius = float(celsius)
    fahrenheit = 1.8 * celsius + 32
    celsius = str(int(celsius))
    fahrenheit = str(int(fahrenheit))
    print(celsius + "ºC son " + fahrenheit + "ºF.")

except ValueError:
    print("Error: Introduzca únicamente valores numéricos para realizar la conversión.")