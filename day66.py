"""class variables are variables that are shared among all instances of a class. They are not unique to each instance but are common and can be accessed by all instances of the class. They are defined within the class construction but outside any instance methods.
Instance attributes are those attributes that are not shared by objects. Every object has its own copy of the instance attribute 
"""
class Employee:
    companyName="Apple" #class variable
    noOfEmployee=0
    def __init__(self,name):
        self.name=name
        self.raise_amount=0.02#instance variable asscociated with object
        Employee.noOfEmployee+=1
    def showDetails(self):
        print(f"the name of the employee is {self.name} and the raise amount is {self.raise_amount} sized {self.noOfEmployee} and working in company {self.companyName}")
emp1=Employee("Aniket")
emp2=Employee("Soumashree")
emp1.companyName="Google"#if instance exist that is hown else it searches for class variable
emp1.showDetails()
#emp2.companyName="Nestle"
Employee.companyName="Google"#class variable changed
emp2.showDetails()