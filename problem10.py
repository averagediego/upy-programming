# Problema 10: Clasificación de números positivos

# Leemos el número y lo convertimos a entero
numero = int(input("Ingresa un número: "))

# Primero verificamos si es positivo (mayor que 0)
if numero > 0:
    # Si es positivo, revisamos si el residuo de dividir entre 2 es cero (par)
    if numero % 2 == 0:
        print("Positivo par")
    else:
        print("Positivo impar")
else:
    # Si es 0 o un número negativo
    print("No es positivo")