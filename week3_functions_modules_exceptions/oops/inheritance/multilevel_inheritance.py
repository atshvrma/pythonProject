class Living:
    def lives(self):
        print("Lives on earth")

class Animal(Living):
    def breathe(self):
        print("Breathing...")

class Mammal(Animal):
    def walk(self):
        print("Walking...")

class Human(Mammal):
    def speak(self):
        print("Speaking...")

person = Human()
person.breathe()
person.walk()
person.speak()

mammal = Mammal()
mammal.breathe()
mammal.walk()
