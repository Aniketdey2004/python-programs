s=input("Enter a string: ")
def count(s):
    c=1
    for i in s:
        if(i==' '):
            c=c+1
    return c

c=count(s)
print("the number of words=",c)
