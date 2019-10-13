tipenfer=int(input("Tipo de enfermedad(1-4):"))
edad=int(input("Que edad tiene?"))
dias=int(input("Dias:"))
if(tipenfer==1 or tipenfer==2 or tipenfer==3 or tipenfer==4):
    if tipenfer==1:
        costo=25*dias
    elif tipenfer==2:
        costo=16*dias
    elif tipenfer==3:
        costo=20*dias
    else:
        costo=32*dias
    if(edad>=14 and edad<=22):
        costot=costo*1.10
        print("Tiene entre 14 y 22 años de edad por lo cual tiene un costo adicional del 10%")
        print(f"El costo total sera de ${costot}")
    else:
        print(f"El costo es de ${costo}")
else:
    print("El tipo de enfermedad no se a encontrado")
