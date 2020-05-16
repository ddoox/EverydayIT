import random

user = 1
number = random.randint(0, 100)
maxn = 100
minn = 0
rounds = 1

while user:
    print("Number " + number.__str__() + "?")
    user = int(input("0 - correct, 1 - too low, 2 - too high: "))
    if user == 1:
        minn = number
    elif user == 2:
        maxn = number
    elif user == 0:
        print(rounds.__str__() + " rounds")
    rounds += 1

    number = random.randint(minn + 1, maxn - 1)
