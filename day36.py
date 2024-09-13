"""a=input("Enter a number: ")
print(f"multiplication table of  {a} is: ")
try: #in the try block we put the code we think a error can occur
    for i in range(1,11):
        print(f"{int(a)}x{i}={int(a)*i}")
except Exception as e: #we can print the error like this
    print(e)

print("some imp lines of  code")
print("end program")"""
try:
    num=int(input("enter a number: "))
    a=[6,3]
    print(a[num])
except ValueError: #for specific error we can write separate except 
    print("Number entered is not an integer")
except IndexError: 
    print("Index error")
