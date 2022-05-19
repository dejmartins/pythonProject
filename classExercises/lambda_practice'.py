# add = lambda x, y: x + y
# sub = lambda x, y: x - y
# print(add.__name__)
# print(sub.__name__)


# def multiply(x, y):
#     return x * y
#
#
# def operate(x, y, func):
#     return func(x, y)
#
#
# val_multiply = operate(9, 5, multiply)
# print(val_multiply)
#
#
# div = operate(10, 2, lambda x, y: x // y)
# print(div)
#
# def multiple(x, func):
#     return func(x)
#
# val_double = multiple(4, lambda x: x * 2)
# val_triple = multiple(4, lambda x: x * 3)
#
# print(val_double)
# print(val_triple)


# print(all([1, 2, 3, 4, 0, 6, 0]))
# print(all([1, 2, 7, 4, 8, 6, 5]))
# print(any([0, 0, 0, 4, 0, 0, 0]))
# print(any([0, 0, 0, 0, 0, 0, 0]))
#
# print()
#
# names = ["Amaka", "Segun", "comb", "Samson", "foil"]
#
# print(all(names.istitle() for name in names))

# peoples = [
#     {"name": "Omosetan Omorele", "age": 30, "year_of_exp": 4, "language": ["Python", "Java"]},
#     {"name": "John Doe", "age": 25, "year_of_exp": 2, "language": ["JavaScript", "C#"]},
#     {"name": "Amaka Stephen", "age": 19, "year_of_exp": 5, "language": ["Python"]},
#     {"name": "Florence Segun", "age": 28, "year_of_exp": 15, "language": ["Python", "HTML"]},
#     {"name": "Ernest Adeola", "age": 30, "year_of_exp": 4, "language": ["Kotlin", "Java"]},
# ]
#
#
# print([people["age"] <= 28 and "Python" in people["language"] for people in peoples])
# print([any(people["age"] <= 28 or "Python" in people["language"] for people in peoples)])
# print([people["name"] for people in peoples if "Python" in people["language"] and people["age"] > 19])


# lst = map(lambda x: x**2, range(1, 10))
# lst1 = list(lst)
# lst2 = list(lst)
# print(lst1)
# print(lst2)

# def isEven(x):
#     return x % 2 == 0
#
# filter_obj = list(filter(isEven, range(1, 10)))
# print(filter_obj)
from functools import reduce

# sum = reduce(lambda x, y: x + y, range(1, 11))
#
# print(sum )


fruits = ["Apple", "Pear", "Pineapple", "Watermelon", "Orange", "Banana"]
smallest = reduce(lambda x, y: x if len(x) < len(y) else y, fruits)
print(smallest)

print(max(fruits, key=len))
print(sorted(fruits, key=len, reverse=True))
print(sorted(fruits, key=lambda x: x[-1]))