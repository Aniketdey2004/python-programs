s=input("enter a string: ")
def isValid(s):
    le=len(s)
    u=0
    l=0
    for i in s:
        if(i>='A' and i<='Z'):
            u=1
        if(i>='a' and i<='z'):
            l=1
    
    if(le>8 and u==1 and l==1):
        return True
    else:
        return False

password=isValid(s)
if(password==True):
    print("The password is valid")
else:
    print("The pasword is inavlid")

