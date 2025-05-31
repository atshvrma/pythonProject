
class Shape:
    def draw(self):
        print("Drawing shape")

class Circle(Shape):
    def show(self):
        print("Showing circle")
#
class Oval(Circle):
    def calculate(self):
        print("Oval formula")


class Square(Shape):
    def draw(self):
        print("Drawing square")

class Rectangle(Shape):
    def draw(self):
        print("drawing rectangle")

c1 = Circle()
s1 = Square()
c1.draw()
s1.draw()

o1 = Oval()
o1.draw()
o1.show()
o1.calculate()