print ("Asignele un valor a las siguientes variables:")
a=int(input("A="))
b=int(input("B="))
c=int(input("C="))
if(a!=b and a!=c and b!=c):
    if(a<b):
        if(b<c):
            print ("Los valores estan en orden creciente")
        else:
            print("Los valores no estan en orden creciente, porque b>c")
    else:
        print("No estan en orden creciente, porque a>b")
else:
    print("Dos o tres valores son iguales")
