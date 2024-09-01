n=int(input("enter a number: "))
def isPrime(n):
    c=0
    for i in range(1,(n//2)+1):
        if(n%i==0):
            c=c+1
    if(c==1):
        return True
    else:
        return False
    
check=isPrime(n)
if(check==True):
    print("prime number")
else:
    print("not a prime number")