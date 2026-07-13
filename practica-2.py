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
