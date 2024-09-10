marks=[3,5,6]
print(marks)
print(type(marks))
print(marks[1])#we can access individual elements by their index

print(marks[-1])#negative index len-negative index
l=[1,9,2,46,"harry",True] #we can store different data types

if "harry" in l: #we can check the presence of a element
    print("yes")
else:
    print("No")

#list slicing
print(marks[1:3]) #same as string slicing
print(marks[0:5:2]) #in slicing we can also give jump index

lst=[i*i for i in range(10) if i%2==0]
print(lst)
