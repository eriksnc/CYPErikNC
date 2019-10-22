n=int(input("Cantiad de numeros a ingresar:"))
i=0
mayor=-100000
menor=100000
while(i<n):
    i+=1
    num=int(input("Ingrese un numero:"))
    if(num>mayor):
        mayor=num
        print(f"El numero mayor es {num}")
    elif(num<menor):
        menor=num
        print(f"El numero menor es {num}")
print(f"El numero mayor es {mayor} y el menor es {menor}")
