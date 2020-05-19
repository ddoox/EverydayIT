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

    elif a =="rock" and b == "scissors":
        print("A wins")
        print("Rematch?")
        print("y/n")
        if input() == "n":
            break
        else:
            continue

    elif a =="paper" and b == "rock":
        print("A wins")
        print("Rematch?")
        print("y/n")
        if input() == "n":
            break
        else:
            continue

    elif a =="scissors" and b == "paper":
        print("A wins")
        print("Rematch?")
        print("y/n")
        if input() == "n":
            break
        else:
            continue

    else:
        print("B wins")
        print("Rematch?")
        print("y/n")
        if input() == "n":
            break
        else:
            continue
