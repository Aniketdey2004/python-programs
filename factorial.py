n=int(input("enter a number: "))
def factorial(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

cal=factorial(n)
print("factorial=",cal)