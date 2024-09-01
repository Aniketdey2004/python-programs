i=0
while(i<3):
    print(i)
    i=i+1

while(i<=10):
    print(i,end=",")
    if(i==7):
        break
    i=i+1

j=0
while(j<8):
    
    j=j+1
    if(j>4):
        continue
    else:
        print(j)
else:
    print("j is greater than equal to 8")