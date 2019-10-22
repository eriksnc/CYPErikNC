n=int(input("Ingrese un numero entero positivo:"))
i=1
suma=0
while(i<=n):
    suma+=(i)**(i)
    print(f"Suma {i}: {suma}")
    i+=1
print(f"Suma total={suma}")
