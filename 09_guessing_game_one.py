import random

score = 0
loops = 0

while(1):

    number = random.randint(1,9)
    print("Your pick:")
    kek = input()
    if kek == "exit":
        print("Score: " + str(score))
        break


    print("The number is: " + str(number))

    if int(kek) == number:
        print("Nice")
        score += 1
    elif int(kek) < number:
        print("Too low")
    elif int(kek) > number:
        print("Too high")

    loops += 1
    print("Avg: " + str(score/loops))
