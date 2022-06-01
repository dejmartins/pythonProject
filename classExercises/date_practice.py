# from datetime import datetime
#
# d = datetime.now()
# print(d)
# print(d.strftime("%A %d %B %Y"))


# def gen():
#     count = 0
#     while True:
#         yield count
#         count += 1
#
#
# for i in gen():
#     print(i)

# s = "Hello"
# it = iter(s)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
import collections


def counter(high, low):
    while low < high:
        yield low
        low += 1


print(list(counter(10, 3)))


Person = collections.namedtuple("Person", "name age")
p1 = Person(name="Adeola", age=16)

print(p1.name)
