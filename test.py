import pygame
from pygame.locals import *

pygame.init()

WIDTH, HEIGHT = 300, 300
GRAY = (60, 60, 60)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')


markers = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pos = []
player = 1
winner = 0
game_over = False

font = pygame.font.SysFont(None, 40)

# def rect for click button
again_rect = Rect(WIDTH // 2 - 85, HEIGHT // 2, 170, 50)

# load images
BOARD = pygame.image.load("Tic-tac-toe.png")
BOARD = pygame.transform.scale(BOARD, (300, 300)) # rescale images
X_IMG = pygame.image.load("X.png")
X_IMG = pygame.transform.scale(X_IMG, (70, 70))
O_IMG = pygame.image.load("O.png")
O_IMG = pygame.transform.scale(O_IMG, (70, 70))

# draw X and O on the screen
def draw_markers():
    x_pos = 0
    for x in markers:
        y_pos = 0
        for y in x:
            if y == 1:
                SCREEN.blit(X_IMG, (x_pos*100 + 15, y_pos*100 + 15))
            if y == 2:
                SCREEN.blit(O_IMG, (x_pos*100 + 15, y_pos*100 + 15))
            y_pos += 1
        x_pos += 1

def win_condition():
    global winner, game_over

    for i in range(0, 3):
        if markers[i][0] == markers[i][1] == markers[i][2] != 0:
            winner = markers[i][0]
            game_over = True
        if markers[0][i] == markers[1][i] == markers[2][i] != 0:
            winner = markers[0][i]
            game_over = True
        if markers[0][0] == markers[1][1] == markers[2][2] != 0:
            winner = markers[0][0]
            game_over = True
        if markers[0][2] == markers[1][1] == markers[2][0] != 0:
            winner = markers[0][2]
            game_over = True

    if game_over == False:
        for i in range(len(markers)):
            for j in range(len(markers)):
                if markers[i][j] != 1 and markers[i][j] != 2:
                    return None
        game_over = True

def draw_winner(winner):
    if winner != 0:
        win_text = f"Player {winner} win !"
        win_img = font.render(win_text, True, WHITE)
        pygame.draw.rect(SCREEN, BLACK, (WIDTH // 2 - 100, HEIGHT // 2 - 60, 200, 50))
        SCREEN.blit(win_img, (WIDTH //2 - 90, HEIGHT // 2 - 50))
    else:
        draw_text = "DRAW"
        draw_img = font.render(draw_text, True, WHITE)
        pygame.draw.rect(SCREEN, BLACK, (WIDTH // 2 - 55, HEIGHT // 2 -60, 100, 50))
        SCREEN.blit(draw_img, (WIDTH // 2 - 50, HEIGHT // 2 - 50))

    again_text = "Play again ?"
    again_img = font.render(again_text, True, WHITE)
    pygame.draw.rect(SCREEN, BLACK, again_rect)
    SCREEN.blit(again_img, (WIDTH // 2 - 80, HEIGHT // 2 + 10))
        
# main loop
run = True
while run:

    SCREEN.fill(GRAY) # draw background
    SCREEN.blit(BOARD, (0, 0)) # draw boardgame
    draw_markers() # draw X and O

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if game_over == 0:
            if event.type == pygame.MOUSEBUTTONDOWN: # collect user input
                pos = pygame.mouse.get_pos() # get mouse position
                cell_x = pos[0]
                cell_y = pos[1]
                if markers[cell_x // 100][cell_y //100] == 0: # if case empty
                    markers[cell_x // 100][cell_y // 100] = player # place a X or O in fonction of the player
                    player = 3 - player # change player between 1 and 2
                    win_condition()

    if game_over == True:
        draw_winner(winner)
        # check for click on Play again
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if again_rect.collidepoint(pos):
                # reset variable
                markers = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                pos = []
                player = 1
                winner = 0
                game_over = False


    pygame.display.update()

pygame.quit() 