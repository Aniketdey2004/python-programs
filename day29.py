n=int(input("enter a number"))
def isEven(n):
    '''this function checks number is even or odd''' #function description i is differenet from comment as it is not ignored by interpreter
    if(n%2==0):
        return True
    else:
        return False

check=isEven(n)
print(isEven.__doc__)
if(check==True):
    print("The number is even")
else:
    print("the number is odd")