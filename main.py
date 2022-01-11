import pygame
import os

pygame.init()

winHeight = 600
winWidth = 600

screen = pygame.display.set_mode([winHeight, winWidth])

board = pygame.image.load(os.path.join('Assets', 'board.jpg'))
board = pygame.transform.scale(board, (winHeight, winWidth))

running = True

while running:
    screen.blit(board, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()


pygame.quit()