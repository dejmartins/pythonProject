# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __repr__(self):
#         return f"{self.__class__.__name__}(name={self.name}, age={self.age}"
#
#     def __str__(self):
#         return f"Your name is {self.name}"
#
#
# p1 = Person("Adeola", 16)
#
# print(p1)


from dataclasses import dataclass, field


# include frozen=True beside the dataclass to make sure you cannot reassign another value to name or age
# use order=True to check for greater than or less than
@dataclass
class Person:
    name: str
    age: int = field(default=16, init=False)
    children: list = field(default_factory=lambda: [])


p1 = Person("Adeola", 16)
print(p1)


