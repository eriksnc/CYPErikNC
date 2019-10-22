arsu=0
arno=0
mersu=50000
arce=0
i=1
while(i<=12):
    print(f"Mes{i}:")
    rno=float(input(f"Promedio de lluvias de la region norte:"))
    rce=float(input(f"Promedio de luvias de la region centro:"))
    rsu=float(input(f"Promedio de lluvias de la region sur:"))
    arno+=rno
    arce+=rce
    arsu+=rsu
    if(rsu<mersu):
        mersu=rsu
        mes=i
    i+=1
    
prorce=arce/12
print(f"Promedio en la region centro:{prorce} \nMes con menor lluvia region sur:{mes} \nRegistro del mes:{mersu}")

if(arno>arce):
    if(arno>arsu):
        print("La region con mayor lluvia es la region norte")
    else:
        print("La region con mayor lluvia es la region sur")
elif (arce>arsu):
    print("La region con mayor lluvia es la region centro")
else:
    print("La region con mayor lluvia es la region sur")
    

