class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I speak"


class Dog(Animal):
    pass


class Cat(Animal):
    pass


cat = Cat("Kitty")
print(cat.name)
