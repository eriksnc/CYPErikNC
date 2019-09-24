sueldo=float(input("De cuanto es su sueldo:"))
if(sueldo<1000):
    newsueldo=sueldo*1.15
    print("Su nuevo salario es de:",newsueldo)
else:
    newsueldo=sueldo*1.12
    print("Su nuevo salario es de:",newsueldo)
