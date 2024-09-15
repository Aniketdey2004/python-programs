"""A class method is a method that is bound to the class and not the object of the class.
They have the access to the state of the class as it takes a class parameter that points to the class and not the object instance.
It can modify a class state that would apply across all the instances of the class. For example, it can modify a class variable that will be applicable to all the instances."""

class Employee:
    company="Tesla"
    def show(self):
        print(f"The name is {self.name} and company name is {self.company}")
    @classmethod#decorator to create class variable
    def changeCompany(cls,newCompany): 
        cls.company=newCompany #used to change class variable
e1=Employee()
e1.name="Aniket"
e1.show()
e1.changeCompany("Appple")
e1.show()