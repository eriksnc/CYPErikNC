nom=0
print("Si quiere finalizar con el ciclo ingrese un -1")
sueldo=float(input("Ingrese Sueldo:$"))
while(sueldo!=-1):
    if(sueldo<1000):
        nsueldo=sueldo*1.15
    else:
        nsueldo=sueldo*1.12
    nom+=nsueldo
    sueldo = float(input(f"Ingrese Sueldo:$"))
    print(f"nuevo sueldo {nsueldo}")
print(f"La nomina es de ${nom}")
