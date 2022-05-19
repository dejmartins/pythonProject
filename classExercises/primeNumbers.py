import math

number = int(input("Input a number: "))
sqrt_of_number = math.sqrt(number)
counter = 2

while counter <= sqrt_of_number:
    if number % counter == 0:
        print("This is not a prime number")
        break
    counter += counter

if number % counter != 0:
    print("This is a prime number ")