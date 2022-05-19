# num = 1
#
#
# def func():
#     global num
#
#     def func():
#         nonlocal num
#     num += 2
#     print(num)
#
#
# print(num)

def f():
    return 'foo', 'bar', 'baz', 'qux'

t = f()
print(t)
