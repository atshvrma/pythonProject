class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):
        print("Bark")

class Cat(Animal):
    def speak(self):
        print("Meow")

# Polymorphism in action
for animal in [Dog(), Cat(), Animal()]:
    animal.speak()
