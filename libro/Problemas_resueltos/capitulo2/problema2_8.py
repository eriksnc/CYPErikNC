com=float(input("Cuanto fue la compra:"))
if(com<500):
    print(f"No hay descuento su pago es de {com}")
elif(com>500 and com<1000):
    pago=com-(com*0.05)
    print(f"Tiene un 5% de descuento su pago es de {pago}")
elif(com>1000 and com<7000):
    pago=com-(com*0.11)
    print(f"Tiene un 11% de descuento su pago es de {pago}")
elif(com>7000 and com<15000):
    pago=com-(com*0.18)
    print(f"Tiene un 18% de descuento su pago es de {pago}")
else:
    pago=com -(com*0.25)
    print(f"Tiene un 25% de descuento su pago es de {pago}")
