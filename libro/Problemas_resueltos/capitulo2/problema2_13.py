cuenta=int(input("Ingrese su numero de cuenta:"))
sem=int(input("Semestre cursando:"))
pro=float(input("Que promedio tiene:"))
print("Iniciando con mayusculas y con sus debidos acentos \nMaterias:\nEconomía \nComputación \nAdministración \nContabilidad")
mat=str(input("Nombre de la materia:"))

if(mat=="Economía" or mat=="Computación" or mat=="Administración" or mat=="Contabilidad"):
    if (mat=="Economía"):
        if (sem>=6):
            if(pro>=8.8):
                print(f"Matricula:{cuenta} \nCarrera:{mat} \nUsted fue Aceptado")
            else:
                print(f"Matricula:{cuenta} \nCarrera:{mat} \nUsted no fue Aceptado")
        else:
            print(f"Matricula:{cuenta} \nCarrera:{mat} \nUsted no fue Aceptado")
    elif(mat=="Computación"):
        if(sem>6):
            if(pro>8.5):
                print(f"Matricula:{cuenta} \nCarrera:{mat} \nUsted fue Aceptado")
            else:
                print(f"Matricula:{cuenta} \nCarrera:{mat} \nUsted no fue Aceptado")
        else:
            print(f"Matricula:{cuenta} \nCarrera:{mat} \nUsted no fue Aceptado")
    elif(mat=="Administración" or mat=="Contabilidad"):
        if(sem>5):
            if(pro>8.5):
                print(f"Matricula:{cuenta} \nCarrera:{mat} \nUsted fue Aceptado")
            else:
                print(f"Matricula:{cuenta} \nCarrera:{mat} \nUsted no fue Aceptado")
        else:
            print(f"Matricula:{cuenta} \nCarrera:{mat} \nUsted no fue Aceptado")
else:
    print("La materia ingresada no esta disponible")
