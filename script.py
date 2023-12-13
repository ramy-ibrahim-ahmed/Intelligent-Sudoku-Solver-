def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = " "
    return False


def valid(board, num, pos):
    for i in range(len(board[0])):
        if num == board[pos[0]][i] and pos[1] != i:
            return False
    for i in range(len(board)):
        if num == board[i][pos[1]] and pos[0] != i:
            return False
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0:
            print(" - - - - - - - - - - - - - - ")
        for j in range(len(board[0])):
            if j % 3 == 0:
                print(" | ", end="")
            if j == 8:
                print(f"{board[i][j]} |")
            else:
                print(f"{board[i][j]} ", end="")
    print(" - - - - - - - - - - - - - - ")


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == " ":
                return (i, j)
    return None