#Arreglos
#lectura
#Escritura / Asignación
#Actualización : Inserción, eliminación, modificación
#Ordenamiento
#Busqueda

# ESCRITURA
frutas=["Zapote","Manzana", "Pera", "Aguacate", "Durazno", "Uva","Sandia"]

#LECTURA, el selector [indice]

print(frutas[2])
print("---------")

#Lectura Con for op 1

for indice in range(0,7,1):
    print(frutas[indice])

print("-------")

#Lectura con for op 2 por un interador for each

for fr in frutas:
    print(fr)
print("---------")

#Asignacón
frutas[2]="Melon"
print(frutas)
print("----Inserccion al final----")
#Inserción al final

frutas.append("Naranja")
print(len(frutas))

frutas.insert(2,"Limon")
print(len(frutas))

frutas.insert(0,"Mamey")
print(frutas)

print("----Eliminaciòn pop----")
#Eliminación con pop

print(frutas.pop(),"<----Elemento eliminado")
print(frutas)
print("--------")
print(frutas.pop(1),"<--Elemento eliminado")
print(frutas)
print("--------")
frutas.append("Limon")
frutas.append("Limon")
print(frutas)
print("--------")
frutas.remove("Limon")
print(frutas)

print("----Ordenamiento----")
#Ordenamiento
frutas.sort()
print(frutas)
frutas.reverse()
print(frutas)
#Busqueda
print("----Busqueda----")
print(f"La uva esta en la pos.{frutas.index('Uva')}")
print(f"El limon esta {frutas.count('Limon')} veces en la lista")

#Concatenar (Extend)
print("----Concatenar----")
print(frutas)
otras_frutas=["Rambutan","Nispero","Liche","Pitaya"]
frutas.extend(otras_frutas)
print(frutas)

#Copiar
print("----Copiar----")
otra_copia=frutas.copy()
otra_copia.append("Fresa")
otra_copia.append("Fresa")
print(otra_copia)


