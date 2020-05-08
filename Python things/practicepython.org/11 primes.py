number = int(input())

if number > 1:
    for i in range (2,number):
        if number%i == 0:
            print("nope")
            break
        elif i == number - 1:
            print("yep")

