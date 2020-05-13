def create_board(game):
    '''Print updated board'''
    print(" -----------------")
    print("| ", game[0][0], " | ", game[0][1], " | ", game[0][2], " |")
    print(" -----------------")
    print("| ", game[1][0], " | ", game[1][1], " | ", game[1][2], " |")
    print(" -----------------")
    print("| ", game[2][0], " | ", game[2][1], " | ", game[2][2], " |")
    print(" -----------------")

def create_lines(matrix):
    ''' Create each of the 8 options for winning as an array.'''
    h1 = list(matrix[0])
    h2 = list(matrix[1])
    h3 = list(matrix[2])
    v1 = []
    v2 = []
    v3 = []
    d1 = []
    d2 = []
    for i in range(3):
        v1.append(matrix[i][0])
        v2.append(matrix[i][1])
        v3.append(matrix[i][2])
    for i in range(3):
        d1.append(matrix[i][i])
        d2.append(matrix[i][2 - i])
    return [v1, v2, v3, h1, h2, h3, d1, d2]


def winner(lines):
    '''For each line of 3 squares (including diagonals, count the occurences of x's and o's and empty squares to determi
     the result'''
    end = 0
    for line in lines:
        if line.count(" ") == 0:
            end += 1
        if line.count("x") == 3:
            print('Player 1 wins!')
            return False
        elif line.count("o") == 3:
            print('Player 2 wins!')
            return False
        else:
            continue
    if end == 8:
        print('Its a tie!')
        return False
    return True


def input_move():
    '''Request next player move and return coordinate on board'''
    move = input('Enter the coordinate of next move (row, col), 1 to 3 inclusive, Player {}: '.format(player)).split(',')
    return int(move[0]), int(move[1])


if __name__ == '__main__':

    playing = True
    game = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    player = 1
    dic = {1: "x", 2: "o"}
    while playing:
        create_board(game)
        a, b = input_move()
        if game[a-1][b-1] == " ":
            game[a-1][b-1] = dic[player]
            playing = winner(create_lines(game))
            if not playing:
                playing = input("Want to play again? (True/False): ")
                if playing:
                    game = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
            if player == 1:
                player = 2
            else:
                player = 1
        else:
            print('Please move to an empty square.')
