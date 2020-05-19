import random

user = 1
middle = 50
maximum = 100
minimum = 0
rounds = 1

while user:
    print("Number " + middle.__str__() + "?")
    user = int(input("0 - correct, 1 - too low, 2 - too high: "))

    if user == 1:
        minimum = middle
    elif user == 2:
        maximum = middle
    elif user == 0:
        print(rounds.__str__() + " rounds")

    middle = int((minimum + maximum)/2)
    rounds += 1

