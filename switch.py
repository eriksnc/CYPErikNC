dia=int(input("Introduce un dia (1-7):"))
if(dia>0 and dia<=7):
    if (dia==1):
        print("lunes")
    if (dia==2):
        print("Martes")
    if (dia==3):
        print("Miercoles")
    if (dia==4):
        print("Jueves")
    if (dia==5):
        print("Viernes")
    if (dia==6):
        print("Sabado")
    if (dia==7):
        print("Domingo")
else:
    print("Dato erroneo")
