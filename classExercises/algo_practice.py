number = int(input("Enter a number: "))

while number != 1:
    if number % 2 != 0:
        number = number * 3 + 1
    elif number % 2 == 0:
        number = number // 2
    print(number, end=" ")
