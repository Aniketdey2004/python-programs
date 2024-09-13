"""import math
print(math.sqrt(4))""" #every function or variable of module can be accessed by modulename.functionname
import harry #importing a predifined file
"""import math as m #using as keyword for shorter name
print(m.sqrt(16))
print(dir(m)) #dir keyword shows everything imported"""
harry.welcome() #we can access the methods and variables of harry file
print(harry.name)

from math import sqrt #the from keyword lets selective functions and variables to be accessed from a file
print(sqrt(16))
