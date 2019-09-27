print("Ingrese los siguientes datos:")
mat=int(input("Matricula:"))
mat1=float(input("Primer calificación:"))
mat2=float(input("Segunda calificación:"))
mat3=float(input("Tercera calificación:"))
mat4=float(input("Cuarta calificación:"))
mat5=float(input("Quinta calificación:"))
pro=(mat1+mat2+mat3+mat4+mat5)/(5)
if(pro>=6):
    print(f"Matricula:{mat}, el alumno aprobo con {pro}")
else:
    print(f"Matricula:{mat}, el alumno reprobo con {pro}")
