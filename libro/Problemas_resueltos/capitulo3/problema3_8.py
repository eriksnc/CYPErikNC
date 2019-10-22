num=int(input("Ingrese un valor entero positivo:"))
while(num!=1):
    if num%2==0:
        num/=2
    else:
        num=(num*3)+1
    print(num)
