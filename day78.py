"""In Python, single inheritance refers to the concept where a child class (subclass) inherits from a single parent class (base class). This means the subclass can use the properties and methods of the parent class."""
class Employee:
    def __init__(self, name, id):
        # This is the constructor for the Employee class
        # It initializes the attributes 'name' and 'id' for an Employee object
        self.name = name
        self.id = id

class Programmer(Employee):  # Single inheritance: Programmer class inherits from Employee
    def __init__(self, name, id, lang):
        # The Programmer class extends the Employee class by adding the 'lang' attribute
        # It first calls the Employee class constructor using super() to initialize name and id
        super().__init__(name, id)
        self.lang = lang  # New attribute specific to the Programmer class

    def showDetails(self):
        # Method to display the details of the Programmer object
        print(f"My name is {self.name}, my ID is {self.id} and the language is {self.lang}")

# Creating an instance of the Programmer class
p = Programmer("Aniket", 46375, "JAVA")
p.showDetails()  # Output: My name is Aniket, my ID is 46375 and the language is JAVA
