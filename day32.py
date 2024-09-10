s1={1,85,6}
s2={1,9,6,13}
print(s1.union(s2))#gives the union of two set but does not update the original set
s1.update(s2) #updates the original set s1 with the union of two sets 
print(s1)
print(s1.isdisjoint(s2)) #return true if there is no common elements

print(s1.issuperset(s2)) #return true if all elements of s2 are present in s1

print(s2.issubset(s1))
print(s1.intersection(s2))#gives the intersection of two sets but doesnt change the original one
s1.intersection_update(s2)#updates the s1 set with intersection elements of s1 and s2
print(s1)

cities={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","seoul","Kabul","Madrid"}
print(cities.symmetric_difference(cities2)) #creates a new set having AUB-A intersection B
cities.symmetric_difference_update(cities2)#updates cities with elements having AUB-A intersection B
print(cities)


c1={"Tokyo","Madrid","Berlin","Delhi"}
c2={"Seoul","Kabul","Delhi"}
print(c1.difference(c2)) #gives only not common elements of c1
c1.difference_update(c2) #updates c1 by removing common elements
print(c1)

c1.add("Helsinki") #to add single element to set
print(c1)
 
c1.remove("Tokyo") #removes element specified from set
print(c1)

c1.discard("Berlin")#does same work as remove() but diff is remove raises an error if element not found but discard does not
print(c1)

print(c1.pop()) #the last element gets poped but we dont know which oneas set is unordered

del c1 #deletes the set
#print(c1)

c2.clear() #makes the set empty
print(c2)
