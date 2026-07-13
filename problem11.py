# Problema 11: Suma de 1 hasta N con ciclo while

# Leemos el entero positivo N
n = int(input("Ingresa un entero positivo N: "))

# 1. INICIALIZACIÓN
suma = 0      # Aquí vamos a acumular el resultado
i = 1         # Nuestro contador que empezará en 1

# 2. CONDICIÓN
# El ciclo se ejecutará mientras el contador 'i' sea menor o igual a 'N'
while i <= n:
    suma = suma + i  # Sumamos el valor actual de 'i' al acumulador
    
    # 3. ACTUALIZACIÓN
    i = i + 1        # Incrementamos el contador para no crear un ciclo infinito

# Imprimimos el resultado final
print(f"La suma de 1 hasta {n} es: {suma}")