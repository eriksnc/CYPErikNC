cate=int(input("Ingrese la categoria (1-4):"))
sueldo=float(input("Sueldo del trabajador:$"))
nuesue=0
if(cate==1 or cate==2 or cate==3 or cate==4):
    if(cate==1):
        nuesue=sueldo*1.15
    elif(cate==2):
        nuesue=sueldo*1.10
    elif(cate==3):
        nuesue=sueldo*1.08
    else:
        nuesue=sueldo*1.07
    print(f"Categoria {cate}")
    print(f"El nuevo sueldo es de ${nuesue}")
else:
    print(f"La categoria {cate} no existe, por lo cual el sueldo es de {nuesue}")
