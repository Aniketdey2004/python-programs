import math
n=int(input("enter a number: "))
def digitCount(n):
    c=0
    while(n>0):
        c=c+1
        n=n//10
    return c
c=digitCount(n)
def isArmstrong(n,c):
    s=0
    while(n>0):
        s=s+math.pow(n%10,c)
        n=n//10
    return s
s=isArmstrong(n,c)
if(s==n):
    print("Armstrong number")
else:
    print("not a armstrong number")