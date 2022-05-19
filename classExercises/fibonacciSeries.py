number_limit = int(input("Input number limit: "))

counter = 1
previous_number = 1
current_number = 0


while counter <= number_limit:
    sum = previous_number + current_number
    print(sum, end=" ")
    previous_number = current_number
    current_number = sum
    counter += 1
