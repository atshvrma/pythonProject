class Shape:
    def area(self):
        print("Area not defined")

    def printName(self):
        print("printed name")

    def another_method(self):
        print("another method")

class Circle(Shape):
    def area(self):
        print("Area = π * r^2")

    def printName(self):
        print("Print my name inside circle")


class Rectangle(Shape):
    def area(self):
        print("Area = l * b")

c = Circle()
c.area()
c.printName()
c.another_method()
#
# s = Shape()
# s.area()
# s.printName()

# List of shapes
# shapes = [Circle(), Rectangle(), Shape()]

# for shape in shapes:
#     shape.area()
#     shape.printName()

