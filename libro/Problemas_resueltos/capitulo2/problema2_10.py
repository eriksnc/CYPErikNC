print("Asignele un valor tipo entero a las siguientes variables")
a=int(input("A="))
b=int(input("B="))
c=int(input("c="))
if a>b:
    if a>c:
        print(f"A es el mayor su valor es de {a}")
    elif(a==c):
        print(f"A y C son los mayores con un valor de {a}")
    else:
         print(f"C es el mayor con un valor de {c}")
else:
    if(a==b and b==c and a==c):
        print(f"A, B y C son iguales su valor es de {a}")
    elif(b==c):
        print(f"B y C son los mayores con un valor de {b}")
    elif(a==b):
        if(a>c):
            print(f"A y B son los mayores con un valor de {a}")
        else:
            print(f"C es el mayor con un valor de {c}")
    elif(b>c):
        print(f"B es el mayor con un valor de {b}")
    elif(c>b):
        print(f"C es el mayor con un valor de {c}")
