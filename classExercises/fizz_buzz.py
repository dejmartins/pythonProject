counter = 1

while counter <= 100:
    print(counter, end=" ")

    if counter % 15 == 0:
        print("FIZZBUZZ")
    elif counter % 3 == 0:
        print("FIZZ")
    elif counter % 5 == 0:
        print("BUZZ")
    else: print(counter)

    counter += 1



