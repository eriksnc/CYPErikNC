print("Asignele un valor entero a las siguientes variables:")
a=int(input("A="))
b=int(input("B="))
c=int(input("C="))
if a>b:
    if a>c:
        if b>c:
            print(f"{a} > {b} > {c}")
        else:
            print(f"{a} > {c} > {b}")
    else:
        print(f"{c} > {a} > {b}")
else:
    if b>c:
        if a>c:
            print(f"{b} > {a} > {c}")
        else:
            print(f"{b} > {c} > {a}")
    else:
        print(f"{c} > {b} > {a}")
print("Fin del programa")
