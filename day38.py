a=int(input("enter salary: "))
if(a<40000):
    raise ValueError("Such less salary not acceptable")#we can raise customerrors like this