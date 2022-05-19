number = int(input("Enter number: "))
counter = 1
factorial = 1;

while number > 0:
    factorial *= number
    number -= 1
    counter += 1

print(factorial)
