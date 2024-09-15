class Point:
    def __init__(self, x, y):
        # Magic method for initialization (constructor)
        self.x = x
        self.y = y

    def __add__(self, other):
        # Magic method for the '+' operator. Adds the coordinates of two Point objects.
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        # Magic method for the '-' operator. Subtracts the coordinates of two Point objects.
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        # Magic method for the '*' operator. Multiplies the coordinates of two Point objects.
        return Point(self.x * other.x, self.y * other.y)

    def __str__(self):
        # Magic method for converting the object to a string (used in print() function).
        return f"Point({self.x}, {self.y})"

    def __repr__(self):
        # Magic method for formal string representation, typically for debugging purposes.
        return f"Point(name={self.x}, age={self.y})"

    def __lt__(self, other):
        # Magic method for the '<' operator. Compares the x-coordinate of two Point objects.
        return self.x < other.x

    def __gt__(self, other):
        # Magic method for the '>' operator. Compares the x-coordinate of two Point objects.
        return self.x > other.x

    def __eq__(self, other):
        # Magic method for the '==' operator. Checks if both x and y coordinates are equal.
        return self.x == other.x and self.y == other.y

# Creating Point objects
p1 = Point(2, 4)
p2 = Point(1, 9)

# Magic method __add__ is called for p1 + p2
p3 = p1 + p2
print(p3)  # Output: Point(3, 13)

# Magic method __sub__ is called for p1 - p2
print(p1 - p2)  # Output: Point(1, -5)

# Magic method __mul__ is called for p1 * p2
print(p1 * p2)  # Output: Point(2, 36)

# Magic method __repr__ is called for repr(p1)
print(repr(p1))  # Output: Point(name=2, age=4)

# Magic method __lt__ is called for p1 < p2 (compares x-coordinates)
print(p1 < p2)  # Output: False (since 2 is not less than 1)

# Magic method __gt__ is called for p1 > p2 (compares x-coordinates)
print(p1 > p2)  # Output: True (since 2 is greater than 1)

# Magic method __eq__ is called for p1 == p2
print(p1 == p2)  # Output: False (since both x and y coordinates are not equal)

# Example of using the __call__ magic method
class Adder:
    def __init__(self, x):
        self.x = x

    def __call__(self, y):
        # Magic method for making an instance callable as if it were a function.
        return self.x + y

# Creating an instance of Adder
adder = Adder(10)

# Magic method __call__ is used here. The object 'adder' is treated like a function.
print(adder(5))  # Output: 15 (since 10 + 5 = 15)
