"""In Python, getters and setters are not the same as those in other object-oriented programming languages. Basically, the main purpose of using getters and setters in object-oriented programs is to ensure data encapsulation"""

""" property() function in Python has four arguments property(fget, fset, fdel, doc), fget is a function for retrieving an attribute value. fset is a function for setting an attribute value. fdel is a function for deleting an attribute value. doc creates a docstring for attribute. A property object has three methods, getter(), setter(), and delete() to specify fget, fset and fdel individually."""
class MyClass:
    def __init__(self,value):
        self._value=value
    def show(self):
        print(f"Value is {self._value}")
    @property #we are defining a getter method by using @property the function is used to assign value to a class property, it is a way of doing encapsulation
    def value(self):
        return self._value
    
    @value.setter
    def value(self,new_value):
        self._value=new_value
obj=MyClass(10)
v=obj.value
print(v)
obj.value=49
v=obj.value
print(v)