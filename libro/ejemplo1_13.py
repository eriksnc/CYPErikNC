matricula=int(input ("Ingrese su matricula:"))
print(matricula)
Mat1=float(input("ingresa calificacion 1:"))
Mat2=float(input("ingresa calificacion 2:"))
Mat3=float(input("ingresa calificacion 3:"))
Mat4=float(input("ingresa calificacion 4:"))
Mat5=float(input("ingresa calificacion 5:"))
promedio=(Mat1+Mat2+Mat3+Mat4+Mat5)/(5)

if(promedio<=5):
    print("Matricula:",matricula," el alumno reprobo con",promedio)
else:
    print("Matricula:",matricula," El alumno aprobo con:",promedio)
