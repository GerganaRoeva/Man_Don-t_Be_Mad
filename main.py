import random
import pygame
import os
from buttons import *
from fonts import *

pygame.init()

winHeight = 600
winWidth = 600

screen = pygame.display.set_mode([winHeight, winWidth])

board = pygame.image.load(os.path.join('Assets', 'board.jpg'))
board = pygame.transform.scale(board, (winHeight, winWidth))

die = 0 # initial val 

def draw():
    screen.blit(board, (0, 0))

    die_button.show_button(screen, colors.black, smaller_corbel)

    if die:
        dietxt = 'dice' + str(die) + '.png'
        die_img = pygame.image.load(os.path.join('Assets', dietxt))
        die_img = pygame.transform.scale(die_img, (50, 50))
        screen.blit(die_img, (240, 275))


def run():

    global die

    running = True
    while running:
        pygame.time.Clock().tick(60)
        draw()
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            mouse_hovering(event, mouse_pos)

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if die_button.is_hovering(mouse_pos):
                    die = random.randint(1, 6)

        pygame.display.update()

    pygame.quit()

run()