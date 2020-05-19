import random


def score(_goal, _user_input):
    bulls_counter = 0
    cows_counter = 0

    for i in range(0, 4):

        if _user_input[i] == _goal[i]:
            cows_counter += 1
            bulls_counter -= 1

        if _user_input[i] in set(_goal):
            bulls_counter += 1

    return cows_counter, bulls_counter


if __name__ == "__main__":
    goal = str(random.randint(1000, 9999))
    won = False
    iterations = 1
    temp_score = (0, 0)

    print(goal)

    while not won:

        print("Please input number: ")
        user_input = str(input())

        tmp_score = score(goal, user_input)

        # +ifs for language things
        if tmp_score == (4, 0):
            print("You won in " + str(iterations) + " turns")
            won = True

        else:
            print(str(tmp_score[0]) + " cows, " + str(tmp_score[1]) + " bulls")
            iterations += 1
