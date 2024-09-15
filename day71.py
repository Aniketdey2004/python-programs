
# Define a class Person with attributes name and version
class Person:
    def __init__(self, name, version):
        self.name = name
        self.version = version

# Create an instance of the Person class
p = Person("Aniket", "3.1.5")
"""dir()

Function: Returns a list of attributes and methods (functions) belonging to an object.
Purpose: Used for introspection, allowing you to explore what properties and actions are available for an object."""

# Print the list of attributes and methods of the Person object
print(dir(p))
""". __dict__

Attribute: Special attribute representing a dictionary-like object containing the object's instance attributes.
Purpose: Accesses the current state of an object's attributes after creation or modification."""
# Print the dictionary containing instance attributes of the Person object
print(p.__dict__)
"""
help()

Function: Provides built-in help documentation for an object, function, module, or keyword.
Purpose: Used to get information about available methods, their arguments, and return values."""
# Attempt to get help for the Person object (might not be informative)
print(help(p))