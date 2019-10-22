v=int(input("Cantidad de ventas:"))
i=0
camen=0
camed=0
camay=0
while(i<v):
    i+=1
    venta=float(input("Ventas:$"))
    if(venta<200):
        camen+=1
    elif(venta>200 and venta<400):
        camed+=1
    else:
        camay+=1
print(f"la cantidad de ventas menores es de {camen}  \nLa cantidad de ventas medias es de {camed} \nLa cantidad de ventas mayores es de {camay}")
