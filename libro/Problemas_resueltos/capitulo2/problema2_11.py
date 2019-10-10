print("El costo de la llamada dependera de la zona geografica:")

print("América del Norte  Clave:12  Costo:$2 \nAmérica Central  Clave:15  Costo:$2.2 \nAmérica del Sur  Clave:18  Costo:$4.5")
print("Europa  Clave:19  Costo:$3.5\nAsia  Clave:23  Costo:$6 \nÁfrica  Clave:25  Costo:$6\nOceanía  Clave:29  Costo:$5")

clave=int(input("\nIngrese la clave:"))
numin=int(input("\nTiempo de llamada:"))
if(clave==12 or clave==15 or clave==18 or clave==19 or clave==23 or clave==25 or clave==29):
    if(clave==12):
        costo=numin*2
        print(f"La llamada tuvo una duracion de {numin} min y el costo total sera de ${costo}")
    if(clave==15):
        costo=numin*2.2
        print(f"La llamada tuvo una duracion de {numin} min y el costo total sera de ${costo}")
    if(clave==18):
        costo=numin*4.5
        print(f"La llamada tuvo una duracion de {numin} min y el costo total sera de ${costo}")
    if(clave==19):
        costo=numin*3.5
        print(f"La llamada tuvo una duracion de {numin} min y el costo total sera de ${costo}")
    if(clave==23):
        costo=numin*6    
        print(f"La llamada tuvo una duracion de {numin} min y el costo total sera de ${costo}")
    if(clave==25):
        costo=numin*6
        print(f"La llamada tuvo una duracion de {numin} min y el costo total sera de ${costo}")
    if(clave==29):
        costo=numin*5
        print(f"La llamada tuvo una duracion de {numin} min y el costo total sera de ${costo}" )
else:
    print("La clave ingresada es erronea")

