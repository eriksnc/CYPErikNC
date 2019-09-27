print("Dele un valor a las siguientes variables:")
a=float(input("A="))
b=float(input("B="))
c=float(input("C="))
dis=b**2-4*a*c
if (dis>=0):
    x1=((-b)+(dis)**(1/2))/(2*a)
    x2=((-b)-(dis)**(1/2))/(2*a)
    print(f"Raices reales de x1={x1} y x2={x2}")
else:
    print("Los valores proporcionados generan una raiz negativa")
