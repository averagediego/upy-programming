#12 factorial 

n = int(input("Ingresa un numero:"))
total = 1
i = 1

while (i<=n):
    total = total * 1
    i = i +1
print ("Factorial: ", total)




#13 suma de numeros pares
#suma numeros pares hasta la numero N 

n = int(input(("Ingresa un numero: "))) #31 - 30
res = 0
for i in range  (2,n,2):
    res = res + 1
    print(i)
print ("suma de pares", res)



#14 contar vocales de una palabra 

palabra = input("Ingresa una palabra: ")
contar = 0
for i in palabra.lower():
    if i in "aeiou"
         contar = contar + 1
print ("Contiene tantas vocales: ", contar)



#15 primer multiplo de 7 entre 1 rango / break y continues/
#Ingrese dos numeros, A y B. %7

a = int(input("ingresa un numero para empezar el rango: "))
b = int(input("ingresa un numero para empezar el rango: "))
for n in range (a,b+1):
    if n %7 == 0
         print ("Primer multiplo de 7: ", n)
         break
    


#16 Suma de numeros positivos

n = [5, 10, -50, 70, -6, -5, -8]
t = 0
for n in num: 
    if n <0:
        continue 
    t = t + n 
print ("total: ",t)


#17 triangulo de asteriscos
#necesitamos una variable n, todoos los asteriscos se van alinear a la izquierda, renglon 1=*, renglon 2=**

n=int(input("Ingresa un numero: "))
for renglon in range (1,n+1)
    print("*" * renglon)


# #17 triangulo de asteriscos invertido

n = int(input("Ingresa un numero: "))

# range(inicio, fin, paso)
# Iniciamos en 'n', nos detenemos antes del 0 (es decir, en 1) y bajamos de -1 en -1
for renglon in range(n, 0, -1):
    print("*" * renglon)


#18 cuadricula de multiplicacion
#Lee un #, se imprime una cuadricula #*#

n = int(input("Ingresa un numero:  "))
for r in range (1, n+1): 
    row = ""
    for c in range(1,n+1)
        linea = linea + str (r*c) + "\t"
    print(linea)