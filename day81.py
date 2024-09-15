"""Hierarchical inheritance occurs when multiple derived classes inherit from the same base class."""
# Base class Animal
class Animal:
    # Constructor to initialize the 'animal' attribute
    def __init__(self, animal):
        self.animal = animal  # Sets the type of animal (e.g., Dog, Cat)

    # Method to display the type of animal
    def showType(self):
        print(f"The type of animal is {self.animal}")  # Prints the type of animal

# Derived class Dog, inheriting from Animal
class Dog(Animal):
    # Constructor to initialize both 'animal' and 'breed' attributes
    def __init__(self, animal, breed):
        super().__init__(animal)  # Calls the constructor of the Animal class to set 'animal'
        self.breed = breed  # Sets the breed of the dog (e.g., Golden Retriever)

    # Method to display details of the dog
    def showDetails(self):
        print(f"The animal is {self.animal} and breed is {self.breed}")  # Prints animal type and breed

# Derived class Cat, inheriting from Animal
class Cat(Animal):
    # Constructor to initialize both 'animal' and 'breed' attributes
    def __init__(self, animal, breed):
        super().__init__(animal)  # Calls the constructor of the Animal class to set 'animal'
        self.breed = breed  # Sets the breed of the cat (e.g., Pussy Cat)

    # Method to display details of the cat
    def showDetails(self):
        print(f"The animal is {self.animal} and breed is {self.breed}")  # Prints animal type and breed

# Creating an instance of the Dog class
d = Dog("Dog", "Golden Retriever")  # Initializes the Dog with animal type 'Dog' and breed 'Golden Retriever'

# Creating an instance of the Cat class
c = Cat("Cat", "Pussy Cat")  # Initializes the Cat with animal type 'Cat' and breed 'Pussy Cat'

# Calling the showDetails method for the Cat instance
c.showDetails()  # Outputs: The animal is Cat and breed is Pussy Cat

# Calling the showDetails method for the Dog instance
d.showDetails()  # Outputs: The animal is Dog and breed is Golden Retriever

# Calling the showType method for the Cat instance (inherited from Animal)
c.showType()  # Outputs: The type of animal is Cat

# Calling the showType method for the Dog instance (inherited from Animal)
d.showType()  # Outputs: The type of animal is Dog

"""Hybrid inheritance is a combination of more than one type of inheritance, for example, a mix of multiple and multilevel inheritance."""
class Animal:
    def speak(self):
        print("Animal speaks")


class Mammal(Animal):
    def give_birth(self):
        print("Mammal gives birth")


class Bird(Animal):
    def lay_eggs(self):
        print("Bird lays eggs")


class Platypus(Mammal, Bird):
    pass


platypus = Platypus()
platypus.speak()        # Method from Animal class
platypus.give_birth()   # Method from Mammal class
platypus.lay_eggs()    # Method from Bird class