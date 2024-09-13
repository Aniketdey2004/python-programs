a=[1,8,9,4]
b=[1,8,9,4]
if(a is b): #is checks for whether both variables point to the same object in memory
    print("yes")
else:
    print("No")

if(a==b):#== checks whether both variables have the same value
    print("value same")
else:
    print("Value not same")
#if the object is immutable python only create that object once in memory and all variables point to it
c=(1,2)
d=(1,2)
if(c is d): #is checks for whether both variables point to the same object in memory
    print("yes")
else:
    print("No")

if(c==d):#== checks whether both variables have the same value
    print("value same")
else:
    print("Value not same")