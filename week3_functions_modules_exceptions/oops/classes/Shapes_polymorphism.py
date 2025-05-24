class Shape:
    def area(self):
        print("Area not defined")

class Circle(Shape):
    def area(self):
        print("Area = π * r^2")

class Rectangle(Shape):
    def area(self):
        print("Area = l * b")


# List of shapes
shapes = [Circle(), Rectangle(), Shape()]

for shape in shapes:
    shape.area()
