import colors
import fonts
import pygame


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
        pygame.draw.rect(screen, outline_color, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)

        text = font.render(self.text, 1, self.text_color)
        screen.blit(text, (
            self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def is_hovering(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False


die_button = Button(colors.pink, colors.black, 301, 275, 60, 50, 'Roll Die')
move_button = Button(colors.pink, colors.black, 370, 285, 50, 30, 'Move')
spawn_button = Button(colors.pink, colors.black, 180, 285, 50, 30, 'Spawn')
audio_button = Button(colors.pink, colors.black, 150, 200, 120, 60, 'Audio ON/OFF')
theme_button = Button(colors.pink, colors.black, 740, 150, 120, 60, 'Change Music')
two_players_button = Button(colors.pink, colors.black, 300, 300, 200, 60, 'Two Players')
three_players_button = Button(colors.pink, colors.black, 300, 400, 200, 60, 'Three Players')
four_players_button = Button(colors.pink, colors.black, 300, 500, 200, 60, 'Four Players')

def change_button(button, pos):
    if button.is_hovering(pos):
            button.color = colors.dark_pink
    else:
        button.color = colors.pink

def mouse_hovering(event, pos):
    if event.type == pygame.MOUSEMOTION:
        change_button(die_button, pos)
        change_button(audio_button, pos)
        change_button(theme_button, pos)
        change_button(two_players_button, pos)
        change_button(three_players_button, pos)
        change_button(four_players_button, pos)
        change_button(move_button, pos)
        change_button(spawn_button, pos)

        
            