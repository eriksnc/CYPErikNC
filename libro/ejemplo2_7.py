num=int(input("Ingrese un valor entero:"))
v=int(input("Ingresa un valor entero:"))
val=0
if(num>0 and num<4):
    if num==1:
        val=100*v
    
    elif num==2:
        val=100**v
        
    elif num==3:
        val=100/v
        
else:
    val=0
print(f"El valor de la funcion es igual a {val}")
