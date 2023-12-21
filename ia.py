import random

def getBoardCopy(board):
    #make a copy of the board list
    boardcopy = []
    for i in board:
        boardcopy.append(i)
    return boardcopy

def isSpace(board, move):
    #return True if move is free
    return board[move] == 0

def ai(board, sign):
    if difficulty == 1:
        x = int(random.randrange(0, 3))
        y = int(random.randrange(0, 3))

        while board[x][y] !=0:
            x = int(random.randrange(0, 3))
            y = int(random.randrange(0, 3))

        board[x][y] = sign

    elif difficulty == 2:
        for i in range(0, 3):
            for j in range(0, 3):
                boardcopy = getBoardCopy(markers)
                if isSpace(boardcopy, i):