import math

number = int(input("Enter a number: "))
length = math.ceil(math.log10(number))
square = math.pow(number, 2)

new_number = square % math.pow(10, length)
if number == new_number:
    print("This number is an ambigram")
else:
    print("This number is not an ambigram")
