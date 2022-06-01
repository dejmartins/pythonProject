class Playground:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        self._age = age

    @age.deleter
    def age(self):
        print("Deleting age...")
        del self._age


p1 = Playground(78)
print(p1.age)
p1.age = 16
print(p1.age)

# del p1.age
# print(p1.age)
