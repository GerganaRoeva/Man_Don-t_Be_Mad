import random
import pygame
import os
from pawns import pawns
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

p1 = pygame.image.load(os.path.join('Assets', 'p1.png'))
p1 = pygame.transform.scale(p1, (50, 50))
p2 = pygame.image.load(os.path.join('Assets', 'p2.png'))
p2 = pygame.transform.scale(p2, (50, 50))
p3 = pygame.image.load(os.path.join('Assets', 'p3.png'))
p3 = pygame.transform.scale(p3, (50, 50))
p4 = pygame.image.load(os.path.join('Assets', 'p4.png'))
p4 = pygame.transform.scale(p4, (50, 50))

die = 0 # initial val 
gamestart = False

players = []
current_player = 1

class Player:
    def __init__(self, id):
        self.id = id


def draw_pawns() :
    for pawn in pawns:
        if pawn.player == 1:
            screen.blit(p1, pawn.pos)
        if pawn.player == 2:
            screen.blit(p2, pawn.pos)
        if pawn.player == 3 and len(players) > 2:
            screen.blit(p3, pawn.pos)
        if pawn.player == 4 and len(players) > 3:
            screen.blit(p4, pawn.pos)

def draw():
    if not gamestart:
        screen.blit(menu, (0, 0))
        two_players_button.show_button(screen, colors.black, small_calibri)
        three_players_button.show_button(screen, colors.black, small_calibri)
        four_players_button.show_button(screen, colors.black, small_calibri)

    else:
        screen.blit(board, (0, 0))
        die_button.show_button(screen, colors.black, smaller_corbel)
        draw_pawns()

        if die:
            dietxt = 'dice' + str(die) + '.png'
            die_img = pygame.image.load(os.path.join('Assets', dietxt))
            die_img = pygame.transform.scale(die_img, (50, 50))
            screen.blit(die_img, (240, 275))
            if die == 6:
                move_button.show_button(screen, colors.black, smaller_comic_sans)
                spawn_button.show_button(screen, colors.black, smaller_comic_sans)

    
def finish_pawn_check(pawn):
    if players[current_player - 1].id == 2:
        if pawn.pos[0] <= 10 and pawn.pos[1] <= 10:
            pawns.remove(pawn)
    elif players[current_player - 1].id == 1:
        if pawn.pos[0] >= 540 and pawn.pos[1] >= 540:
            pawns.remove(pawn)   
    elif players[current_player - 1].id == 4:
        if pawn.pos[0] >= 540 and pawn.pos[1] <= 10:
            pawns.remove(pawn) 
    elif players[current_player - 1].id == 3:
        if pawn.pos[0] <= 10 and pawn.pos[1] >= 540:
            pawns.remove(pawn)      

def check_player():
    counter = 0
    for pawn in pawns:
        if pawn.player == players[current_player - 1].id:
            counter += 1
    if counter == 0:
        players.remove(players[current_player - 1])


def run():
    global die
    global gamestart
    playing = True
    global players
    global current_player

    while playing:
        pygame.time.Clock().tick(60)
        draw()
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():                  
        
            mouse_hovering(event, mouse_pos)

            if event.type == pygame.QUIT:
                playing = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if die_button.is_hovering(mouse_pos):
                    die = random.randint(1, 6)
                    if die == 6:
                        for pawn in pawns:
                            # if event.type == pygame.MOUSEBUTTONDOWN:
                            #     if spawn_button.is_hovering(mouse_pos):
                            #         print("pressed spawn")
                                    if pawn.player == players[current_player - 1].id and not pawn.active:
                                        if players[current_player - 1].id == 1:
                                            pawn.pos = (540, 540)
                                            pawn.active = True
                                            break
                                        elif players[current_player - 1].id == 2:
                                            pawn.pos = (10, 10)
                                            pawn.active = True
                                            break
                                        elif players[current_player - 1].id == 3:
                                            pawn.pos = (10, 540)
                                            pawn.active = True
                                            break
                                        elif players[current_player - 1].id == 4:
                                            pawn.pos = (540, 10)
                                            pawn.active = True
                                            break
                            # if event.type == pygame.MOUSEBUTTONDOWN:
                            #     if move_button.is_hovering(mouse_pos):
                            #         print("pressed move")
                            #         for i in range (0, 6):
                            #             for pawn in pawns:
                            #                 if pawn.player == players[current_player - 1].id and pawn.active:
                            #                     if pawn.pos[0] > 10 and pawn.pos[1] >= 540:
                            #                         new_pos = (pawn.pos[0] - 76 , pawn.pos[1])
                            #                         pawn.pos = new_pos
                            #                         print(pawn.pos)
                            #                         finish_pawn_check(pawn)  
                            #                         break
                            #                     if pawn.pos[0] <= 10 and pawn.pos[1] > 10:
                            #                         new_pos = (pawn.pos[0], pawn.pos[1] - 76)
                            #                         pawn.pos = new_pos
                            #                         print(pawn.pos)
                            #                         finish_pawn_check(pawn)  
                            #                         break
                            #                     if pawn.pos[0] < 540 and pawn.pos[1] <= 10 :
                            #                         new_pos = (pawn.pos[0] + 76 , pawn.pos[1])
                            #                         pawn.pos = new_pos
                            #                         print(pawn.pos)
                            #                         finish_pawn_check(pawn)  
                            #                         break
                            #                     if pawn.pos[0] >= 540 and pawn.pos[1] < 540:
                            #                         new_pos = (pawn.pos[0], pawn.pos[1] + 76)
                            #                         pawn.pos = new_pos
                            #                         print(pawn.pos)
                            #                         finish_pawn_check(pawn)  
                            #                         break
                                    
                    else:
                        for i in range (0, die):
                            for pawn in pawns:
                                if pawn.player == players[current_player - 1].id and pawn.active:
                                    if pawn.pos[0] > 10 and pawn.pos[1] >= 540:
                                        new_pos = (pawn.pos[0] - 76 , pawn.pos[1])
                                        pawn.pos = new_pos
                                        print(pawn.pos)
                                        finish_pawn_check(pawn)  
                                        break
                                    if pawn.pos[0] <= 10 and pawn.pos[1] > 10:
                                        new_pos = (pawn.pos[0], pawn.pos[1] - 76)
                                        pawn.pos = new_pos
                                        print(pawn.pos)
                                        finish_pawn_check(pawn)  
                                        break
                                    if pawn.pos[0] < 540 and pawn.pos[1] <= 10 :
                                        new_pos = (pawn.pos[0] + 76 , pawn.pos[1])
                                        pawn.pos = new_pos
                                        print(pawn.pos)
                                        finish_pawn_check(pawn)  
                                        break
                                    if pawn.pos[0] >= 540 and pawn.pos[1] < 540:
                                        new_pos = (pawn.pos[0], pawn.pos[1] + 76)
                                        pawn.pos = new_pos
                                        print(pawn.pos)
                                        finish_pawn_check(pawn)  
                                        break
                        check_player()
                        current_player += 1
                        if current_player > len(players):
                            current_player = 1

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

            if gamestart:
                pass

                
        pygame.display.update()

    pygame.quit()

run()
