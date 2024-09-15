class Employee:
    def __init__(self, name, salary):
        self.name = name  # Instance variable for name
        self.salary = salary  # Instance variable for salary

    def parentMethod(self):
        print("Hi, I am Aniket")  # Method in parent class

class Programmer(Employee):
    def __init__(self, name, salary, version):
        # super() is a function that returns a temporary object of the superclass.
        # It allows you to call methods and access attributes from the parent class.
        # Here, super() is used to call the __init__ method of the parent class Employee
        # to initialize 'name' and 'salary' for the Programmer instance.
        super().__init__(name, salary)
        
        self.version = version  # Additional attribute for the child class

    def parentMethod(self):
        # super() is used here to call the parent class's parentMethod()
        # It allows us to execute the original method in the parent class (Employee)
        # before extending its behavior in the child class.
        super().parentMethod()
        
        # After calling the parent class method, we add additional functionality.
        print("Parent method was accessed")  # Additional message specific to Programmer class

    def showDetails(self):
        # Accesses instance variables directly via self to display the details.
        print(f"name={self.name}, salary={self.salary}, version={self.version}")

# Create an instance of Programmer
p = Programmer("Aniket", 13564, "3.14.8787")

# Call the parentMethod() in Programmer, which first calls the parent class method
# via super(), then prints additional information from the Programmer class.
p.parentMethod()

# Call the showDetails() method to display the details of the Programmer instance
p.showDetails()
