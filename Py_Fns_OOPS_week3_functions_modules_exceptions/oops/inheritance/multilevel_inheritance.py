from abc import ABC, abstractmethod

class Living(ABC):
    @abstractmethod
    def lives(self):
        print("Lives on earth")

class Animal(Living):
    def breathe(self):
        print("Breathing...")

    def lives(self):
        print("Living in india")

a = Animal()
a.lives()



class Mammal(Animal):
    def walk(self):
        print("Walking...")

class Human(Mammal):
    def speak(self):
        print("Speaking...")
#
# person = Human()
# person.breathe()
# person.walk()
# person.speak()
#
# mammal = Mammal()
# mammal.breathe()
# mammal.walk()
