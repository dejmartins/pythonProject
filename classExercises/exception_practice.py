# def divide(a, b):
#     if b == 0:
#         raise ValueError("Denominator can not be zero")
#     return a // b
#
#
# num = int(input("Enter a numerator: "))
# den = int(input("Enter a denominator: "))
#
# while True:
#     try:
#         print(divide(num, den))
#         break
#     except:
#         print("Wrong value")
#         num = int(input("Enter a numerator: "))
#         den = int(input("Enter a denominator: "))

try:
    print("life's good")
    print([1, 2, 3, 4][5])
    print("After Life")
except ZeroDivisionError as e:
    print("Zero Index", e)
except IndexError as e:
    print("Index Index", e)
else:
    print("Else I run only when there's no error")
finally:
    print("Finally, I run every time")