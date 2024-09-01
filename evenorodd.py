n=int(input("enter a number"))
def isEven(n):
    if(n%2==0):
        return True
    else:
        return False

check=isEven(n)
if(check==True):
    print("The number is even")
else:
    print("the number is odd")