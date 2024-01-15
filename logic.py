import random


def get_num_from_index(y, x):
    return y * 4 + x + 1


def insert_2_or_4(lst, y, x):
    if random.random() <= 0.75:
        lst[y][x] = 2
    else:
        lst[y][x] = 4
    return lst


def get_index_from_num(num):
    num -= 1
    y, x = num // 4, num % 4
    return y, x


def get_empty_list(lst):
    empty = []
    for y in range(4):
        for x in range(4):
            if lst[y][x] == 0:
                num = get_num_from_index(y, x)
                empty.append(num)
    return empty


def moveLeft(board):
    shiftLeft(board)

    for i in range(4):
        for j in range(3):
            if board[i][j] == board[i][j + 1] and board[i][j] != 0:
                board[i][j] *= 2
                board[i][j + 1] = 0
                j = 0

    shiftLeft(board)
    return board


def moveUp(board):
    board = rotateLeft(board)
    board = moveLeft(board)
    board = rotateRight(board)
    return board


def moveRight(board):
    shiftRight(board)

    for i in range(4):
        for j in range(3, 0, -1):
            if board[i][j] == board[i][j - 1] and board[i][j] != 0:
                board[i][j] *= 2
                board[i][j - 1] = 0
                j = 0

    shiftRight(board)
    return board


def moveDown(board):
    board = rotateLeft(board)
    board = moveRight(board)
    shiftRight(board)
    board = rotateRight(board)
    return board


def shiftLeft(board):
    for i in range(4):
        nums, count = [], 0
        for j in range(4):
            if board[i][j] != 0:
                nums.append(board[i][j])
                count += 1
        board[i] = nums
        board[i].extend([0] * (4 - count))


def shiftRight(board):
    for i in range(4):
        nums, count = [], 0
        for j in range(4):
            if board[i][j] != 0:
                nums.append(board[i][j])
                count += 1
        board[i] = [0] * (4 - count)
        board[i].extend(nums)


def rotateLeft(board):
    b = [[board[j][i] for j in range(4)] for i in range(3, -1, -1)]
    return b


def rotateRight(board):
    b = rotateLeft(board)
    b = rotateLeft(b)
    return rotateLeft(b)
