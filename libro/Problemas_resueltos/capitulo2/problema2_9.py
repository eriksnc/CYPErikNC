arti=float(input("Valor del producto:"))
if(arti<20):
    print(f"El producto no tiene impuesto su valor es de ${arti}")
elif(arti>20 and arti<40):
    imp=(arti-20)*0.30
    pagot=arti+imp
    print(f"El producto tiene un impuesto del ${imp} su costo es de ${pagot}")
elif(arti>40 and arti<500):
    imp=(20*0.30)+(arti-40)*0.40
    pagot=arti+imp
    print(f"El producto tiene un impuesto del ${imp} su costo es de ${pagot}")
else:
    imp=20*0.30+(arti-40)*0.50
    pagot=arti+imp
    print(f"El producto tiene un impuesto del ${imp} su costo es de ${pagot}")
