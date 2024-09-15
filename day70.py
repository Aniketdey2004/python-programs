class Employee:
    """Represents an employee with a name and salary."""

    def __init__(self, name, salary):
        """Constructor for the Employee class.

        Args:
            name (str): The employee's name.
            salary (int): The employee's annual salary.
        """
        self.name = name
        self.salary = salary

    @classmethod
    def fromstr(cls, string):
        """Creates an Employee object from a string.

        Args:
            string (str): A string containing the name and salary separated by a hyphen.

        Returns:
            Employee: A new Employee object.
        """
        name, salary = string.split("-")
        return cls(name, int(salary))

# Create an Employee object using the constructor
e1 = Employee("Aniket", 12000)
print(e1.name)  # Output: Aniket
print(e1.salary)  # Output: 12000

# Create an Employee object using the class method
string = "John-12000"
e2 = Employee.fromstr(string)
print(e2.name)  # Output: John
print(e2.salary)  # Output: 12000