print("Asignele un valor a las siguientes variables")
p=int(input("P="))
q=int(input("Q="))
exp=p**3+q**4-2*p**2
if (exp<680):
    print(f"La expresion de p**3+q**4-2*p**2 es de {exp}")
    print(f"P={p} y Q={q}")
else:
    print(f"La expresion de p**3+q**4-2*p**2 es de {exp}")
