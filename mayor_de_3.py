print("Asigne un numero a la siguientes variables")
a=int(input("A="))
b=int(input("B="))
c=int(input("C="))
if(a>b and b>c):
    print("El mayor es A")
if(b>a and b>c):
    print("El mayor es B")
if(c>a and c>b):
    print ("El mayor es C")
if(a==b and a==c and b==c):
    print ("Todos son iguales")
