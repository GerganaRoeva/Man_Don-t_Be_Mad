import pygame
import os
pygame.init()
pygame.mixer.init()

move_sound = pygame.mixer.Sound(os.path.join('Audio', 'pawn.wav'))
theme1 = pygame.mixer.Sound(os.path.join('Audio', 'theme1.wav'))
theme2 = pygame.mixer.Sound(os.path.join('Audio', 'theme2.wav'))
theme3 = pygame.mixer.Sound(os.path.join('Audio', 'theme3.wav'))
theme4 = pygame.mixer.Sound(os.path.join('Audio', 'theme4.wav'))
theme5 = pygame.mixer.Sound(os.path.join('Audio', 'theme5.wav'))
themes = [theme1, theme2, theme3, theme4, theme5]