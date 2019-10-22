n=int(input("Ingrese un numero:"))
pro=0
prot=0
c=0
i=0
while(i<n):
    i+=1
    num=int(input("Ingrese un numero:"))
    if(num>0):
        pro+=num
        c+=1
    prot+=num
print(f"Promedio de los numero positivos es de {pro/c} \nPromedio de todos los numeros es de {prot/n}")
