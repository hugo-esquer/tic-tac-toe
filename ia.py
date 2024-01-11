import random

def ai(board, sign):
        x = int(random.randrange(0, 3))
        y = int(random.randrange(0, 3))

        while board[x][y] !=0:
            x = int(random.randrange(0, 3))
            y = int(random.randrange(0, 3))

        board[x][y] = sign