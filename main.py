import random
import pygame
import os
from buttons import *
from fonts import *

pygame.init()

winHeight = 600
winWidth = 600

screen = pygame.display.set_mode([winHeight, winWidth])

board = pygame.image.load(os.path.join('Assets', 'board.png'))
board = pygame.transform.scale(board, (winHeight, winWidth))

menu = pygame.image.load(os.path.join('Assets', 'menu.png'))
menu = pygame.transform.scale(menu, (winHeight, winWidth))



die = 0 # initial val 
gamestart = False

class Player:
    def __init__(self, id):
        self.id = id


def draw():
    if not gamestart:
        screen.blit(menu, (0, 0))
        two_players_button.show_button(screen, colors.black, fonts.calibri)
        three_players_button.show_button(screen, colors.black, fonts.calibri)
        four_players_button.show_button(screen, colors.black, fonts.calibri)

    else:
        screen.blit(board, (0, 0))
        die_button.show_button(screen, colors.black, smaller_corbel)

        if die:
            dietxt = 'dice' + str(die) + '.png'
            die_img = pygame.image.load(os.path.join('Assets', dietxt))
            die_img = pygame.transform.scale(die_img, (50, 50))
            screen.blit(die_img, (240, 275))

    


def run():

    global die
    global gamestart

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

            if not gamestart:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    player1 = Player(1)
                    player2 = Player(2)
                    if two_players_button.is_hovering(mouse_pos):
                        players = [player1, player2]
                        gamestart = True
                        screen.blit(board, (0, 0))
                    if three_players_button.is_hovering(mouse_pos):
                        player3 = Player(3)
                        players = [player1, player2, player3]
                        gamestart = True
                        screen.blit(board, (0, 0))
                    if four_players_button.is_hovering(mouse_pos):
                        player3 = Player(3)
                        player4 = Player(4)
                        players = [player1, player2, player3, player4]
                        gamestart = True
                        screen.blit(board, (0, 0))

                

        pygame.display.update()

    pygame.quit()

run()