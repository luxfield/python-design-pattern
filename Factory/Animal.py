from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak():
        pass

#depcreated
class Tiger(Animal):
    def speak(self):
        print("Auuuummm")


class Cat(Animal):
    def speak(self):
        print("Meow")


class Dog(Animal):
    def speak(self):
        print("Guk guk")
