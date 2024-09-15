"""Multilevel inheritance in object-oriented programming refers to a scenario where a class is derived from a class that is itself derived from another class. """

# Base class (level 1 in the inheritance chain)
class Animal:
    def __init__(self, animal):
        # Initializing the 'animal' attribute
        self.animal = animal

# Intermediate class (level 2), inherits from Animal
class Breed(Animal):
    def __init__(self, animal, breed):
        # Calling the constructor of the Animal class (level 1) to initialize the 'animal' attribute
        super().__init__(animal)
        # Initializing the 'breed' attribute specific to this level
        self.breed = breed

# Derived class (level 3), inherits from Breed, which itself inherits from Animal
class Color(Breed):
    def __init__(self, animal, breed, color):
        # Calling the constructor of the Breed class (level 2) to initialize 'animal' and 'breed' attributes
        super().__init__(animal, breed)
        # Initializing the 'color' attribute specific to this level
        self.color = color

    # Method to display the details of the object
    def showDetails(self):
        # This method uses the attributes from all levels of the inheritance hierarchy
        print(f"The animal is {self.animal}, breed is {self.breed}, and color is {self.color}")

# Creating an instance of the Color class, which is at the bottom of the inheritance chain
tommy = Color("Dog", "Golden Retriever", "Orange")

# Calling the showDetails method to display the attributes inherited from all classes
tommy.showDetails()
