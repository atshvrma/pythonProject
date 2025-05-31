from abc import ABC, abstractmethod
#
# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass
#
# class Dog(Animal):
#     def make_sound_1(self):
#         print("Bark")
#
# class Cat(Animal):
#     def make_sound(self):
#         print("Cat")
#





class Remote(ABC):
    @abstractmethod
    def increase_sound(self):
        pass

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def decrease_sound(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class Samsung_Remote(Remote):

    def decrease_sound(self):
        pass

    def turn_off(self):
        pass

    def turn_on(self):
        print("Samsung TV turned on")

    def increase_sound(self):
        print("Samsung TV col increased")

    def change_picture_quality(self):
        print("Showing in HD now !!")

class Sony_Remote(Remote):

    def decrease_sound(self):
        pass

    def turn_off(self):
        pass

    def increase_sound(self):
        print("Sony TV col increased")

    def turn_on(self):
        print("Sony TV turned on")

    def change_volume_quality(self):
        print("High quality sound now !!")


s1 = Samsung_Remote()
s1.increase_sound()
s1.change_picture_quality()