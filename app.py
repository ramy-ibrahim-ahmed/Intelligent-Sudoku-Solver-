from script import *
board = [
    [7, 8, " ", 4, " ", " ", 1, 2, " "],
    [6, " ", " ", " ", 7, 5, " ", " ", 9],
    [" ", " ", " ", 6, " ", 1, " ", 7, 8],
    [" ", " ", 7, " ", 4, " ", 2, 6, " "],
    [" ", " ", 1, " ", 5, " ", 9, 3, " "],
    [9, " ", 4, " ", 6, " ", " ", " ", 5],
    [" ", 7, " ", 3, " ", " ", " ", 1, 2],
    [1, 2, " ", " ", " ", 7, 4, " ", " "],
    [" ", 4, 9, 2, " ", 6, " ", " ", 7],
]


print_board(board)
solve(board)
print_board(board)