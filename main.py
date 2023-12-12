import pygame
pygame.init()

WIDTH, HEIGHT = 500, 500
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

WHITE = (255,255,255)

BOARD = pygame.image.load("Tic-tac-toe.png")
BOARD = pygame.transform.scale(BOARD, (450, 450))
X_IMG = pygame.image.load("X.png")
X_IMG = pygame.transform.scale(X_IMG, (80, 80))
O_IMG = pygame.image.load("O.png")
O_IMG = pygame.transform.scale(O_IMG, (80, 80))

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
graphical_board = [[[None, None], [None, None], [None, None]], 
                   [[None, None], [None, None], [None, None]],
                   [[None, None], [None, None], [None, None]]]

to_move = "X"

screen.fill(WHITE)
screen.blit(BOARD, (25, 25))

pygame.display.update()

def render_board(board, ximg, oimg):
    global graphical_board
    for i in range(3):
        for j in range(3):
            if board[i][j] == "X":
                graphical_board[i][j][0] = ximg
                graphical_board[i][j][1] = ximg.get_rect(center=(j*150+100, i*150+100))
            elif board[i][j] == "O":
                graphical_board[i][j][0] = oimg
                graphical_board[i][j][1] = oimg.get_rect(center=(j*150+100, i*150+100))


def add_XO(board, graphical_board, to_move):
    current_pos = pygame.mouse.get_pos()
    cell_size = 150
    row = (current_pos[1] - 50) // cell_size
    col = (current_pos[0]) // cell_size

    if board[row][col] != "O" and board[row][col] != "X":
        board[row][col] = to_move
        if to_move == "O":
            to_move = "X"
        else:
            to_move = "O"

    render_board(board, X_IMG, O_IMG)

    for i in range(3):
        for j in range(3):
            if graphical_board[i][j][0] is not None:
                screen.blit(graphical_board[i][j][0], graphical_board[i][j][1])

    return board, to_move

def check_win(board):
    winner = None
    for row in range(0, 3):
        if((board[row][0] == board[row][1] == board[row][2]) and (board [row][0] is not None)):
            winner = board[row][0]
            for i in range(0, 3):
                win_img = pygame.image.load(f"Winning {winner}.png")
                graphical_board[row][i][0] = pygame.transform.scale(win_img, (80, 80))
                screen.blit(graphical_board[row][i][0], graphical_board[row][i][1])
            pygame.display.update()
            return winner

    for col in range(0, 3):
        if((board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None)):
            winner =  board[0][col]
            for i in range(0, 3):
                win_img = pygame.image.load(f"Winning {winner}.png")
                graphical_board[i][col][0] = pygame.transform.scale(win_img, (80, 80))
                screen.blit(graphical_board[i][col][0], graphical_board[i][col][1])
            pygame.display.update()
            return winner
   
    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None):
        winner =  board[0][0]
        win_img = pygame.image.load(f"Winning {winner}.png")
        win_img = pygame.transform.scale(win_img, (80, 80))
        graphical_board[0][0][0] = win_img
        screen.blit(graphical_board[0][0][0], graphical_board[0][0][1])
        graphical_board[1][1][0] = win_img
        screen.blit(graphical_board[1][1][0], graphical_board[1][1][1])
        graphical_board[2][2][0] = win_img
        screen.blit(graphical_board[2][2][0], graphical_board[2][2][1])
        pygame.display.update()
        return winner
          
    if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):
        winner =  board[0][2]
        win_img = pygame.image.load(f"Winning {winner}.png")
        win_img = pygame.transform.scale(win_img, (80, 80))
        graphical_board[0][2][0] = win_img
        screen.blit(graphical_board[0][2][0], graphical_board[0][2][1])
        graphical_board[1][1][0] = win_img
        screen.blit(graphical_board[1][1][0], graphical_board[1][1][1])
        graphical_board[2][0][0] = win_img
        screen.blit(graphical_board[2][0][0], graphical_board[2][0][1])
        pygame.display.update()
        return winner
    
    if winner is None:
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != 'X' and board[i][j] != 'O':
                    return None
        return "DRAW"


game_finished = False
run = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board, to_move = add_XO(board, graphical_board, to_move)

            if game_finished:
                board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
                graphical_board = [[[None, None], [None, None], [None, None]], 
                                    [[None, None], [None, None], [None, None]], 
                                    [[None, None], [None, None], [None, None]]]

                to_move = 'X'

                screen.fill(WHITE)
                screen.blit(BOARD, (25, 25))

                game_finished = False

                pygame.display.update()
            
            if check_win(board) is not None:
                game_finished = True 

            
            pygame.display.update()


pygame.quit()