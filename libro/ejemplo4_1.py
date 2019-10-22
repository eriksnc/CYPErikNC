ac=0
suma=0
sueldos= []
for i in range(7):
    sueldos.append(int(input(f"Sueldo {i+1}:$")))
print(sueldos)

for indice in range(7):
    suma+=sueldos[indice]
promedio=suma/7
print(f"El promedio de sueldos es de {promedio}")
cont=0
for x in range(7):
    if(sueldos[x]>promedio):
        cont+=1
        print(f"Sueldo:{sueldos[x]}")

     
