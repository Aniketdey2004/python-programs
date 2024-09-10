ep1={122:45,123:89,567:69}
ep2={222:47,457:96}
ep1.update(ep2) #adds the key value pair to the dictionary
print(ep1)

ep1.clear() #deletes all key value pairs 
print(ep1)
p={"tamojit":"langra","Aniket":"bokachoda"}
p.pop("tamojit") #pops a value corresponding to the key
print(p)
p.popitem() #deletes the last element
print(p)

del ep2 #deletes the dictionary
print(ep2)