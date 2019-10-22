n=int(input("Ingrese un numero entero positivo:"))
suma=0
i=1
while(i<=n):
    if(-1)**(i)>0:
        suma-=1/i
    else:
        suma+=1/i
    i+=1
print(f"La suma de la series es {suma}")
