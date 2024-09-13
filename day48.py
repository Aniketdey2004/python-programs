x=10 #global variables accessible by all functions
def my_function():
    global x
    x=4 #we are accessing the global variable
    print(x)
    y=5#local variable its existence is only within the function
    print(y)

