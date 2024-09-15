"""A static method is also a method that is bound to the class and not the object of the class. This method can’t access or modify the class state. It is present in a class because it makes sense for the method to be present in class."""
class Math:
    def __init__(self,num):
        self.num=num
    def addtonum(self,n):
        self.num=self.num+n
    @staticmethod
    def add(a,b):
        return a+b
result=Math.add(7,5)
print(result)
a=Math(7)
print(a.add(7,8))
