total = 0
new_number = int(input("Enter a number: "))
counter = 1

while new_number >= 1:
    total += new_number
    new_number -= 1
    counter += 1

print("The sum is", total)

for i in range(1, new_number + 1):
    total += i

print(total)
print()


