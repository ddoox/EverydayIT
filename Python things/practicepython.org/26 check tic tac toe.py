def check(moves):   # 1,2 - win, 404 - draw
    draw = []
    for i in range(0, 3):
        draw.append(moves[0][i])
        draw.append(moves[i][0])
        if moves[i][0] != 0 and moves[i][0] == moves[i][1] and moves[i][1] == moves[i][2]:  # horizontal
            return True, moves[i][0]
        elif moves[i][0] != 0 and moves[0][i] == moves[1][i] and moves[1][i] == moves[2][i]:  # vertical
            return True, moves[0][i]

    if moves[0][0] != 0 and moves[0][0] == moves[1][1] and moves[1][1] == moves[2][2]:  # 1st diagonal
        return True, moves[0][0]
    if moves[0][2] != 0 and moves[0][2] == moves[1][1] and moves[1][1] == moves[2][0]:  # 2nd diagonal
        return True, moves[0][0]

    if 0 not in draw:
        return True, 404


game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

game = [[1, 1, 2],
        [2, 2, 1],
        [1, 1, 2]]

print(check(game))
