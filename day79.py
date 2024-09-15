"""Multiple inheritance in Python allows a class to inherit attributes and methods from more than one parent class. This provides flexibility, allowing a subclass to inherit the features of multiple classes."""
class Employee:
    def __init__(self, name):
        # Constructor for Employee class initializes the 'name' attribute
        self.name = name
    
    def showDetails(self):
        # Method in Employee class to display the employee's name
        print(f"My name is {self.name}")

class Dancer:
    def __init__(self, dance):
        # Constructor for Dancer class initializes the 'dance' attribute
        self.dance = dance
    
    def showDetails(self):
        # Method in Dancer class to display the type of dance
        print(f"My dancing type is {self.dance}")

class Shivani(Employee, Dancer):  # Multiple inheritance: Shivani class inherits from Employee and Dancer
    def __init__(self, name, dance):
        # Shivani class constructor initializes both the 'name' and 'dance' attributes
        self.name = name  # Inherited from Employee
        self.dance = dance  # Inherited from Dancer

# Creating an instance of Shivani class
p = Shivani("Shivani", "Kathak")
p.showDetails()  # Output: "My name is Shivani"
