while(1):
    print("Player A: ")
    a = input()
    print("Player B: ")
    b = input()

    if a == b:
        print("Rematch?")
        print("y/n")
        if input() == "n":
            break
        else:
            continue

    if a =="rock" and b == "scissors":
        print("A wins")
        print("Rematch?")
        print("y/n")
        if input() == "n":
            break
        else:
            continue

    if a =="rock" and b == "paper":
        print("B wins")
        print("Rematch?")
        print("y/n")
        if input() == "n":
            break
        else:
            continue

# etc....