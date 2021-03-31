#! /usr/bin/python3

grid = [[None, None, None],
        [None, None, None],
        [None, None, None]]


def print_grid():
    for row in grid:
        print(row)


def game_over():
    return False


turn = "X"


def change_turn():
    if(turn == "X"):
        return "O"
    else:
        return "X"


while not game_over():
    print_grid()
    print("It is "+turn+"'s turn")
    selection = input("enter a selection as x,y: ")
    coords = selection.split(",")
    if(len(coords) != 2 or not coords[0].isnumeric() or not coords[1].isnumeric()):
        print("unexpected input, expected: 'x,y' (row, then column)")
        continue
    else:
        x = int(coords[0])
        y = int(coords[1])
        if(not grid[y][x] == None):
            continue
        grid[y][x] = turn
        turn = change_turn()
