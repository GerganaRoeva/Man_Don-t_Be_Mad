
import random
import pygame
import os

pygame.init()

winHeight = 600
winWidth = 600

screen = pygame.display.set_mode([winHeight, winWidth])

board = pygame.image.load(os.path.join('Assets', 'board.jpg'))
board = pygame.transform.scale(board, (winHeight, winWidth))

class Button:
    def __init__(self, color, text_color, x, y, width, height, text):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.text_color = text_color
        # self.hitbox = pygame.Rect(x, y, width, height)  # Може да се използва ако искаме да използваме функции от pygame.Rect

    def show_button(self, screen, outline_color, font):
        # Прави бутона да се изборазява.
        pygame.draw.rect(screen, outline_color, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)

        text = font.render(self.text, 1, self.text_color)
        screen.blit(text, (
            self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def is_hovering(self, pos):
        # Проверява дали мишката е върху бутона
        # Pos е координатите на мишката
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False

die_button = Button((170, 170, 170), (0, 0, 0), 301, 275, 60, 50, 'Roll Die')

die = 1


def draw():
    screen.fill((255, 255, 255))

    screen.blit(board, (0, 0))

    die_button.show_button(screen, (0, 0, 0), pygame.font.SysFont('Calibri', 20))

    if die:
        dietxt = 'dice' + str(die) + '.png'
        die_img = pygame.image.load(os.path.join('Assets', dietxt))
        die_img = pygame.transform.scale(die_img, (50, 50))
        screen.blit(die_img, (240, 275))


def mouse_hovering(event, pos):
    if event.type == pygame.MOUSEMOTION:
        if die_button.is_hovering(pos):
            die_button.color = (100, 100, 100)
        else:
            die_button.color = (170, 170, 170)


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