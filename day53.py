l=[1,9,14,6,4,12]
double=list(map(lambda x:x*x,l)) #map takes two arguments a function and a variable list and return a new list
print(double)
f=list(filter(lambda x:x>9,l))#filter takes two arguments a function that returns true or false and if the item matches condition it is added in new list
print(f)
#reduce need to be imported before use
from functools import reduce
num=[1,3,7,13,6]
sum=reduce(lambda x,y:x+y,num)#the reduce function applies the function to a sequence and returns a single value
print(sum)