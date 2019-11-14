archivo=open("numeros.txt","rt")
print(dir(archivo))

n1=archivo.read()
print(n1)
print(n1.split('\n'))
lista_num=[]
for linea in n1.split('\n'):
    for numero in linea.split(','):
        lista_num.append(int(numero))

print(lista_num)
lista_num.sort()
print(f"\nLista ordenada:{lista_num}\n ")
print(f"El mayor es :{lista_num[-1]} y el menor es :{lista_num[0]}")
archivo.close()

print("---------------------------------------->Ejemplo de readlines<-------------------------------------")

archivo=open("numeros.txt","rt")
n2=archivo.readlines()
print(n2)

lista=[]

for x in n2:
    for num in x.split(','):
        lista.append(int(num))

print("\n",lista)
lista.sort()
print(f"\nLista ordenada:{lista_num}\n ")
print(f"El mayor es :{lista[-1]} y el menor es :{lista[0]}")

archivo.close()
print("------------------------------------------------------------------------------------------------------------------")
archivo=open("numeros.txt","rt")
n3=archivo.readline()
print(n3)               
archivo.close()
