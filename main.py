import pygame
import os

pygame.init()

screen = pygame.display.set_mode([1000, 500])

board = pygame.image.load(os.path.join('Assets', 'board.jpg'))
board = pygame.transform.scale(board, (1000, 500))

running = True

while running:
    screen.blit(board, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()


pygame.quit()