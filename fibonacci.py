n=int(input("enter number of terms: "))
def printFib(n):
    a=0
    b=1
    print(a,b,sep=",",end=",")
    for i in range(1,n-1):
        c=a+b
        print(c,end=",")
        a=b
        b=c

printFib(n)