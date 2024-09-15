#Inheritance is the capability of one class to derive or inherit the properties from another class. 

class Employee:#A parent class is a class whose properties are inherited by the child class.
    def __init__(self,name,pos):
        self.name=name
        self.position=pos
    def showDetails(self):
        print(f"my name is {self.name} and i am working in {self.position} in this organisation")

class Programmer(Employee):#A child class is a class that drives the properties from its parent class
    def showLanguage(self):
        print("this is written in python")
a=Employee("Aniket","Project alpha")
a.showDetails()
b=Programmer("Soumashree","Project alpha")
b.showDetails()
b.showLanguage()