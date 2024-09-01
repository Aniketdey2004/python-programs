n=int(input("enter a number: "))
def sumOfDigits(n):
    s=0
    while(n>0):
        s=s+n%10
        n=n//10
    return s

s=sumOfDigits(n)
print("The sum of digits=",s)