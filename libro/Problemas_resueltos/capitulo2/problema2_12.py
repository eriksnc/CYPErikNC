sue=float(input("Ingrese el sueldo:$"))
cate=int(input("Categoria (1-4):"))
he=int(input("Cantidad de horas extra:"))
nsue=0
if cate>0 and cate<5:
    if(cate==1):
        phe=30
    elif(cate==2):
        phe=38
    elif cate==3:
        phe=50
    else:
        phe=70
    if(he>30):
        nsue=sue+30*phe
        print(f"Categoria:{cate} y el nuevo sueldo es de {nsue}")
    else:
        nsue=sue+he*phe
        print(f"Categoria:{cate} y el nuevo sueldo es de {nsue}")
else:
    phe=0
    nsue=sue+he*phe
    print(f"no existe la categoria {cate} por lo tanto el sueldo es de {nsue}")
