def func():
    try:
        l=[1,5,7,9]
        i=int(input("enter the index: "))
        print(l[i])
        return 1
    except:
        print("some error occured")
        return 0
    finally:#finally is always executed whether try or block is executed and they have returned
        print("I am always executed")
    #print("i am always executed")
x=func()
print(x)