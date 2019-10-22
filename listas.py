#Listas

lluvias_norte=[80,60,120,100,70,150,100,47,95,70,100,130]
mes=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]


for indice in range(0,12,1):
    print(f"Mes {mes[indice]}: \nRegion norte={lluvias_norte[indice]}")

print(lluvias_norte[4])
print(lluvias_norte[:5:])
