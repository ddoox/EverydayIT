# from os import system, name
#
#
# def clear():
#     system('cls' if name == 'nt' else 'clear')


def draw(_x, _y, moves):

    for i in range(0, _x):   #first row
        print(" ---", end="")
    print()

    for k in range(0, _y):

        for i in range(0, _x + 1):
            print("|", end="")

            if i < _x:
                if moves[k][i] == 0:
                    print("   ", end="")
                if moves[k][i] == 1:
                    print(" o ", end="")
                if moves[k][i] == 2:
                    print(" x ", end="")
        print()

        for i in range(0, _x):
            print(" ---", end="")
        print()


def check(moves):  # 1 - win "o", 2 - win "x", 404 - draw
    draw = []
    for i in range(0, 3):
        draw.append(moves[0][i])
        draw.append(moves[i][0])
        if moves[i][0] != 0 and moves[i][0] == moves[i][1] and moves[i][1] == moves[i][2]:  # horizontal
            return moves[i][0]
        elif moves[i][0] != 0 and moves[0][i] == moves[1][i] and moves[1][i] == moves[2][i]:  # vertical
            return moves[0][i]

    if moves[0][0] != 0 and moves[0][0] == moves[1][1] and moves[1][1] == moves[2][2]:  # 1st diagonal
        return moves[0][0]
    if moves[0][2] != 0 and moves[0][2] == moves[1][1] and moves[1][1] == moves[2][0]:  # 2nd diagonal
        return moves[2][0]

    if 0 not in draw:
        return 404


def user_input(iteration, moves):  # input = x,y;    o=1, x=2
    now_playing_o = iteration % 2

    if now_playing_o:
        move = input("o: ").split(",")
        moves[int(move[0]) - 1][int(move[1]) - 1] = 1
        return moves
    else:
        move = input("x: ").split(",")
        moves[int(move[0]) - 1][int(move[1]) - 1] = 2
        return moves


game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]


play = True

while play:

    play = int(input("Do you want play a game? 1-yes, 0-no "))

    if play == 0:
        break

    iteration = 1

    while True:

        draw(3, 3, game)
        user_input(iteration, game)
        draw(3, 3, game)

        result = check(game)
        if result == 1:
            print("o won")
            break
        elif result == 2:
            print("x won")
            break
        elif result == 404:
            print("It's a draw")
            break
        iteration += 1


