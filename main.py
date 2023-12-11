import pygame
pygame.init()

WIDTH, HEIGHT = 500, 500
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

WHITE = (255,255,255)
BOARD = pygame.image.load("Tic-tac-toe.png")
BOARD = pygame.transform.scale(BOARD, (450, 450))

run = True

while run:
    screen.fill(WHITE)
    screen.blit(BOARD, (25, 25))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()


pygame.quit()