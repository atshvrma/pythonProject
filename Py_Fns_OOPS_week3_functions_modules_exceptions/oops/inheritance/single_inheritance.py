class Vehicle:
    def start(self):
        print("Starting engine...")

class Car(Vehicle):
    def drive(self):
        print("Driving car")

c = Car()
c.start()
c.drive()
