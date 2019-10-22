b="T"
sumares=0
i=0
while(i<=1800):
    sumares+=1
    print(i)
    if(b=="T"):
        b="F"
        i+=2
    else:
        b="T"
        i+=3
print(f"suma total {sumares}")
