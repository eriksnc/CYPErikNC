n= int(input("Ingrese el numero de elementos del arreglo:"))
vec=[]
if n>=1 and n<=500:
    #Logica
    for i in range(n):
        vec.append(int(input("Ingrese valor:")))
    vec.sort()
    print(vec)
    print("Lista de numeros sin repeticiones")
    i=0
    while i <= n-1:
        print(vec[i])
        repet=vec[i]
        while i<=n-1 and repet==vec[i]:
            i=i+1
else:
    print("El numero de elementos del arreglo es incorrecto")
