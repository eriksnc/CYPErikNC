def sumar(x,y):
    z=x+y
    return z
def restar (x,y):
    return x-y
def mi_print(texto):
    print(f"Este es mi print: {texto}")
def main():
    a=10
    b=5
    c=sumar(a,b)
    print(f"La suma de {a} y {b} es {c}")
    c=restar(a,b)
    print(f"La resta de {a} y {b} es {c}")

def multiplica(valor , veces):
    if (veces==None):
        print("Debes enviar el segundo argumento de la función")
    else:
        print(valor*veces)
def comanda (mesa, comensal, entrada, medio ,fuerte , postre="helado de limón"): #Argumentos de la funcion
    print(f"Mesa:{mesa} comensal:{comensal}")
    print(f"\t Entrada: {entrada}")
    print(f"\t Segundo tiempo: {medio}")
    print(f"\t plato fuerte: {fuerte}")
    print(f"\t Postre: {postre}")

comanda(2,1,"Ensalada","Sopa de rana","Filete de Oso") #Ejecucion Del argumento
comanda(entrada="Ensalada",medio="Sopa de rana",fuerte="Filete de Oso",postre="Flan",mesa=1, comensal=2) 
""""
mesa=int(input("Mesa:"))
comensal=int(input("Comensal:"))
entrada=str(input("Entrada:"))
medio=str(input("Medio:"))
fuerte=str(input("Fuerte:"))
postre=str(input("Postre:"))
comanda(mesa, comensal, entrada, medio ,fuerte , postre)
"""
def imprime_argumentos(*argumentos):
    for ele in argumentos:
        print(ele)
    """
    for index in range(len(argumentos)):
        print(argumentos[index])
    """
def comanda2(**comida):
    print(comida)
    llaves=comida.keys()
    for elem in llaves:
        print(elem,"->",comida[elem])



multiplica(10,3)
multiplica(10,None)
multiplica('hola ',3)

mi_print("Hola!!!!!!!"), 
imprime_argumentos('Hola',True,3.1416,1000,{'id':'sc01','nombre':'Juan'})
comanda2(entrada="Ensalada",medio="Sopa de rana",fuerte="Filete de Oso",postre="Flan",mesa=1, comensal=2,bebida="Coca Ligth") 
if __name__=='__main__': #¿Se mandó a ejecutar (interpretar este archivo)?
    main()
