print ("Ingrese los datos del dinosaurio:")
nombre=str(input("Nombre:"))
peso=float(input("Peso en toneladas:"))
longitud=float(input("longitud en pies:"))
pesokg=peso*1000
lm=longitud*0.3047
print("Los datos del dinosaurio son los siguientes:")
print(f"Nombre:{nombre}\nPeso en kg:{pesokg}kg \nLongitud en m:{lm}m")
