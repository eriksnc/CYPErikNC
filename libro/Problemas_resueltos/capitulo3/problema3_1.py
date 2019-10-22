sumapar=0
sumimp=0
cuepar=0
i=1
while(i<=270):
    num=int(input("Dame un numero:"))
    if(num!=0):
        if (-1)**num > 0:
            sumapar+=num
            cuepar+=1
        else:
            sumimp+=num
    i=i+1
propar=sumapar/cuepar
print(f"El promedio de los numeros pares es de {propar}  \nLa suma de todos los impares es de {sumimp}")
