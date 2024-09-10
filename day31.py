#sets are unordered collection of data items
#sets are immutable
#sets do not contain duplicate items
s={2,4,56,2}
print(s)

info={"Aniket",45,87,False}
print(info)
#since sets are unordered they cannot be accessed by index

harry={} #the syntax for dict and set are same so empty set cannot be initialised like this
print(type(harry))

#to create empty set
harry=set()
print(type(harry))

for value in info:
    print(value)