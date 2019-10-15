cue=0
n=int(input("Dame un valor:"))
for i in range (0,n,1):
    num=int(input("Dame un valor:"))
    if num==0:
        cue+=1        
print("El numero de 0's capturados fué:",cue)
