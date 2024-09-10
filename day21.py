def isGreater(a, b=1): #a is required argument and b is default argument
    if a > b:
        print("The first number is greater")
    else:
        print("The second number is greater")

isGreater(7)
isGreater(b=9,a=8) #a and b are keyword arguments

isGreater(45,96)

def calavg(*numbers): #this is a way of variable length argument, numbers is a tuple
    s=0
    for i in numbers:
        s=s+i
    return s/len(numbers)

c=calavg(7,9,16,17)
print(c)

def intro(**name):
    print("hello i am",name["fname"],name["lname"])

intro(fname="Aniket",lname="Dey")

