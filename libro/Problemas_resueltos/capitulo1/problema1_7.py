L1=float(input("ingrese el valor de lado 1:"))
L2=float(input("ingrese el valor de lado 2:"))
L3=float(input("ingrese el valor de lado 3:"))

s=(L1+L2+L3)/2

area=(s*(s-L1)*(s-L2)*(s-L3))**(1/2)
print(f"El area de tu triangulo es de:{area}")
