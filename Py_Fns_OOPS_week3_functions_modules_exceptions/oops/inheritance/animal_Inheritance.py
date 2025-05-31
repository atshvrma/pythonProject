class Animal:
    def __init__(self):
        print("Self construct")

    # def __init__(self, how_many_legs):
    #     print("total legs are" + str(how_many_legs))

    def speak(self):
        print("Animal sound")
    def sleep(self):
        print("sleeping")

class Dog(Animal):
    def speak(self):
        print("Dog barks")
    def sleep(self):
        print("All time")

class Cat(Animal):
    def speak(self):
        print("Cat Meows")

    def play(self):
        print("playing")

class Elephant(Animal):
    def speak(self):
        print("Trunk noises")

# Object
a = Animal()
d = Dog()
c = Cat()

a.speak()  # Animal sound
d.speak()  # Dog barks
c.speak()

a.sleep()
d.sleep()
c.sleep()