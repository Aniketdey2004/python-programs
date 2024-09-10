tup=(1,6,76,8,56,13)
print(type(tup))
print(len(tup))
print(tup[1])#we can access each element by their index
print(tup[-1])#negative indexing

if 76 in tup: #we can check the presence of a element
    print("yes")
else:
    print("No")

tup2=tup[1:5]#tuple slicing same as previous
print(tup2)