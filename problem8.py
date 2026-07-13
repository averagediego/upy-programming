# Problema 8: Estado físico del agua

# Solicitamos la temperatura al usuario y la convertimos a número flotante (decimal)
temp = float(input("Ingresa la temperatura en Celsius: "))

# Evaluamos las condiciones para determinar el estado físico
if temp <= 0:
    print("Solido (hielo)")
elif 0 < temp < 100:
    print("Liquido (agua)")
else:
    print("Gaseoso (vapor)")