from random import choice


def show_board(board):
    for line in board:
        print(line)


def free_spaces(board):
    spaces_to_play = []
    for i, line in enumerate(board):
        for j, col in enumerate(line):
            if col == 0:
                spaces_to_play.append([i, j])

    return spaces_to_play


def move(line, col, board, player_num):
    if board[line][col] == 0:
        board[line][col] = player_num


def check_winner(board):
    # only 1 or 2 in some line
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != 0:
            return board[i][0]

    # only 1 or 2 in some column:
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != 0:
            return board[0][i]

    # only 1 or 2 in some diagonal
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != 0:
        return board[0][2]

    return 0


def randomized_game(board):
    new_board = board.copy()

    player = 0
    while True:
        player = (player + 1) % 2
        spaces = free_spaces(new_board)

        # if draw
        if len(spaces) == 0:
            return 0

        play = choice(spaces)
        move(play[0], play[1], new_board, player + 1)

        # if some players win
        if check_winner(new_board) != 0:
            return player+1


def copy_board(board):
    new_board = []
    for line in board:
        line_new_board = []
        for element in line:
            line_new_board.append(element)
        new_board.append(line_new_board)

    return new_board


def monte_carlo_simulation(board, n_simulations=1000):
    results = []
    spaces = free_spaces(board)

    for i, j in spaces:
        results.append(0)

        for _ in range(n_simulations):
            # Creating a new board with no references from original board
            new_board = copy_board(board)
            new_board[i][j] = 2
            result = randomized_game(new_board)

            if result == 2:
                results[-1] += 5
            elif result == 1:
                results[-1] += 1

    if argmax(results) is not None:
        return spaces[argmax(results)]
    return None


def argmax(vector):
    if not vector:
        return None

    idx_max = 0
    value_max = vector[0]

    for position, value in enumerate(vector):
        if value > value_max:
            idx_max = position

    return idx_max


if __name__ == '__main__':
    board_game = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]

    player = 0
    while True:
        player = (player+1) % 2
        if player == 1:
            player_choice = input().split()
            if board_game[int(player_choice[0])][int(player_choice[1])] == 0:
                board_game[int(player_choice[0])][int(player_choice[1])] = 1
            else:
                print("invalid play.")
                exit(-1)

        else:
            alg_choice = monte_carlo_simulation(board_game)
            if alg_choice is not None:
                board_game[alg_choice[0]][alg_choice[1]] = 2

        if free_spaces(board_game) == 0:
            show_board(board_game)
            print("DRAW!!")
            break

        winner = check_winner(board_game)
        if winner != 0:
            show_board(board_game)
            print(f"WINNER: {winner}!!")
            break

        show_board(board_game)
        print()

