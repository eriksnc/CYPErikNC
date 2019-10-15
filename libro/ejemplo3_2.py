tra=int(input("Cantidad de trabajadores:"))
nomina=0
for x in range(tra):
    sue=float(input(f"Sueldo del trabajador {x+1}:$"))
    nomina+=sue
print(f"La nomina de la empresa es ${nomina}")
