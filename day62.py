"""A Class in Python has three types of access modifiers:

Public Access Modifier: Theoretically, public methods and fields can be accessed directly by any class.
Protected Access Modifier: Theoretically, protected methods and fields can be accessed within the same class it is declared and its subclass.
Private Access Modifier: Theoretically, private methods and fields can be only accessed within the same class it is declared.
We are mentioning “Theoretically” because python doesn’t follow the textbook definition of such specifications."""
class Person: 
    def __init__(self,name,occupation,salary,address): 
        self.name=name
        self.occupation=occupation
        self.__salary=salary#way to declare private variable
        self._address=address#way to declare protected variable
    def info(self):
        print(f"{self.name} is a {self.occupation}")
class Programmer(Person):#A child class is a class that drives the properties from its parent class
    def showLanguage(self):
        print(f"this is written in python {self._address}")#protected member accesssed by subclass
Aniket=Person("Aniket","Software Developer",80000,"8/9c/1b")
Aniket.info() # All data members and member functions of a class are public by default. 
#print(Aniket.__salary) cannot be accessed and throws error because _salary is private member,but there is no such private it is stored with different name by name mangling
print(Aniket._Person__salary)#but can be accessed like this
print(Aniket._address)#there is nothing like protected in python it can still be accessed its just a denotation that it is protected for developers
Soumo=Programmer("Soumashree","Software developer",80000,"christopher road")
Soumo.showLanguage()