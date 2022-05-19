import random
print("Input a number range 1 - 100")
myNumber = random.randint(1, 100)

counter = 1

while counter <= 3:
    guess = int(input("Number: "))
    if guess > myNumber:
        print("Too High")
    elif guess < myNumber:
        print("Too Low")
    elif guess == myNumber:
        print("Got it, you smart")
        break
    counter += 1

else:
    print("Three trials, that's enough!")
    print("My number is", myNumber)

