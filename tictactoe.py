def board(game):

    # adding elements of game state to the rows

    # grid[0:2] is row 1    1,1 1,2 1,3
    # grid[3:5] is row 2    2,1 2,2 2,3
    # grid[6:8] is row 3    3,1 3,2 3,3

    grid = [game[index] for index in range(9)]

    return grid


def display(grid):

    # displaying the board
    # box[] prints a vertical element for box[0]
    # and horizontal one for box[1]
    # printing grid and state of play

    # defining box as a list

    box = ["|", "---------"]

    print(box[1])
    print(box[0], grid[0], grid[1], grid[2], box[0])
    print(box[0], grid[3], grid[4], grid[5], box[0])
    print(box[0], grid[6], grid[7], grid[8], box[0])
    print(box[1])


def input_check():
    state = input()
    allowed = {"X", "O", "_"}

    for char in state:
        if char not in allowed:
            print("Please include only symbols 'X', 'O', '_'")
            return input_check()

    return state


def analyze_game(grid):

    # changing parameter - list with a state of the board - into a string

    state_of_game = "".join(grid)

    # input read in rows, columns and on diagonals

    rows = [state_of_game[index:index + 3] for index in range(0, 9, 3)]
    columns = [state_of_game[index::3] for index in range(0, 3, 1)]
    diagonals = [state_of_game[index:9 - index:4 - index] for index in range(0, 3, 2)]

    x_win_set = "XXX"
    o_win_set = "OOO"

    result = [x_win_set in rows or x_win_set in columns or x_win_set in diagonals,
              o_win_set in rows or o_win_set in columns or o_win_set in diagonals]

    if abs(state_of_game.count("X") - state_of_game.count("O")) <= 1 and state_of_game.count("_") > 0:

        if result[0]:
            if result[1]:
                result = 0
            else:
                result = 1
        elif result[1]:
            result = 2
        else:
            result = 4

    elif state_of_game.count("_") == 0:

        if result[0]:
            result = 1
        elif result[1]:
            result = 2
        else:
            result = 3

    else:
        result = 0

    return result


def move_x(grid):

    allowed = {1, 2, 3}
    rows = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    while True:

        index = input().split()
        index_row = index[0]
        index_column = index[1]

        if index_row.isdigit():
            if index_column.isdigit():
                if int(index_row) in allowed:
                    if int(index_column) in allowed:
                        if grid[rows[int(index_row) - 1][int(index_column) - 1]] == "_":
                            grid[rows[int(index_row) - 1][int(index_column) - 1]] = "X"
                            break
                        else:
                            print("This cell is occupied! Choose another one!")
                    else:
                        print("Coordinates should be from 1 to 3!")
                else:
                    print("Coordinates should be from 1 to 3!")
            else:
                print("You should enter numbers!")
        else:
            print("You should enter numbers!")

    return grid


def move_o(grid):

    allowed = {1, 2, 3}
    rows = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    while True:

        index = input().split()
        index_row = index[0]
        index_column = index[1]

        if index_row.isdigit():
            if index_column.isdigit():
                if int(index_row) in allowed:
                    if int(index_column) in allowed:
                        if grid[rows[int(index_row) - 1][int(index_column) - 1]] == "_":
                            grid[rows[int(index_row) - 1][int(index_column) - 1]] = "O"
                            break
                        else:
                            print("This cell is occupied! Choose another one!")
                    else:
                        print("Coordinates should be from 1 to 3!")
                else:
                    print("Coordinates should be from 1 to 3!")
            else:
                print("You should enter numbers!")
        else:
            print("You should enter numbers!")

    return grid


# game code starts here:

# game state for start of the game is an empty board - string "_________"

game_state = "_________"

# display() displays the game,
# board converts string into the 9 elements list defining all squares

board_state = board(game_state)

display(board_state)

# first move of the user - X
# move() checks if input correct and updates grid returning the grid list.
# board_state is updated with new state of the board after the move
# variable turn is used as a counter for turns - even for O player, odd for X player

turn = 1

# loop with a game engine

while True:

    if turn % 2 == 0:
        board_state = move_o(board_state)
    else:
        board_state = move_x(board_state)

    display(board_state)

    # analyze_game() checks the progress of the game

    results = analyze_game(board_state)

    if results == 1:
        print("X wins")
        break
    elif results == 2:
        print("O wins")
        break
    elif results == 3:
        print("Draw")
        break

    turn += 1
