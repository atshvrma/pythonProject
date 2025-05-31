# def bark():
#     print("Woof !")

class Dog:

    def bark(self, attack=""):
        print("Woof! Woof!")
        if attack:
            print(attack)

    def eat(self):
        print("Always hungry !!")

    def sleep(self):
        print("during daytime !")

# Creating an object/instance of Dog Class
# german shepherd
my_dog = Dog()
my_dog.bark()
my_dog.eat()
my_dog.bark("I will bite you ")

print("Another Dog Object")

# French bulldog
another_dog = Dog()
another_dog.bark()