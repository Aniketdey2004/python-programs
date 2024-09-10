l=[75,89,2,1,1,9,25,85,67]
l.append(7) #adds a single element to the list and modifies the original list
print(l)
l.sort()#sorts the list in ascending order
print(l)
l.sort(reverse=True)
print(l) #sorts the list in descending order
print(l.index(9))#this method return the index of the first occurence of the list item
print(l.count(1))#this method counts the total no. of occurence of a particular element
m=l #m points to same list any modification through m modifies original list
m[0]=0
print(l)
p=l.copy()#this function creates a copy of list and stores
l.insert(1,456)#inserts element at particular index
print(l)
m=[435,89,55,47]
l.extend(m)#adds list m to l
print(l)