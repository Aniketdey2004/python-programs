"""Method overriding occurs when a subclass provides its own implementation of a method that is already defined in its parent class. This allows the subclass to customize or completely change the behavior of the inherited method."""

class Shape:
    def __init__(self, x, y):
        # Constructor for Shape class, takes two parameters x and y (dimensions of the shape)
        self.x = x
        self.y = y

    def area(self):
        # Method to calculate the area of a generic shape (x * y)
        return self.x * self.y

class Circle(Shape):
    def __init__(self, radius):
        # Constructor for Circle class, calls the parent class (Shape) constructor using super()
        # A circle's area is π * r^2, so both x and y are the radius
        super().__init__(radius, radius)

    def area(self):
        # Method overriding: This overrides the area method in the Shape class.
        # Here, it first calls the parent class's area method using super() and then
        # multiplies the result by 3.14 (an approximation of π) to calculate the circle's area.
        print(3.14 * super().area())

# Create a Circle object with radius 4
c = Circle(4)
# Call the overridden area method
c.area()  # Output: 50.24 (because area of the circle = π * r^2 = 3.14 * 4 * 4)
