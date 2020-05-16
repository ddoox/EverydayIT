def draw(_x, _y):

    for i in range(0, _x):   #first row
        print(" ---", end="")
    print()

    for k in range(0, _y):

        for i in range(0, _x + 1):
            print("|", end="")
            print("   ", end="")
        print()

        for i in range(0, _x):
            print(" ---", end="")
        print()


x = 10
y = 3

draw(x, y)
