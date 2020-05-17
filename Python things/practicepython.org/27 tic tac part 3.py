def user_input(iteration, _game):   # input = x,y;    o=1, x=2
    now_playing_o = iteration % 2

    if now_playing_o:
        move = input("o: ").split(",")
        _game[int(move[0])-1][int(move[1])-1] = 1
        return _game
    else:
        move = input("x: ").split(",")
        _game[int(move[0])-1][int(move[1])-1] = 2
        return _game


game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

print(user_input(1, game))
