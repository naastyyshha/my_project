import os
import sys
import pygame

from utils import mfont


class Barbie(pygame.sprite.Sprite):
    def __init__(self, image, *group):
        super().__init__(*group)
        self.image = load_image(image)
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 300

    def update(self, screen, x, y, n):
        self.scale = pygame.transform.scale(
            self.image, (self.image.get_width() // n,
                         self.image.get_height() // n))
        self.scale_rect = self.scale.get_rect(center=(x, y))
        screen.blit(self.scale, self.scale_rect)
        pygame.display.update(self.rect)


class Button():
    # Класс для создания кнопок
    def __init__(self, colour, x, y, width, height, text=""):
        self.colour = colour
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    # Функция для рисования конопок
    def draw_btn(self, win, text_col):
        pygame.draw.rect(win, self.colour, (self.x, self.y, self.width, self.height), 0, 20)
        # drawRoundRect(win, self.colour, (self.x, self.y, self.width, self.height))

        if self.text != "":
            font = pygame.font.SysFont(mfont, 20)
            text = font.render(self.text, 1, text_col)
            win.blit(text, (self.x + (self.width / 2 - text.get_width() / 2),
                            self.y + (self.height / 2 - text.get_height() / 2)))

    # Провека на прикосание к кнопки
    def touched(self, pos):
        if pos[0] > self.x and pos[0] < (self.x + self.width) and pos[1] > self.y and pos[1] < (self.y + self.height):
            return True
        return False


# Функция для загрузки картинок
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)

    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()

    return image


with open('best_score.txt', 'r') as f:
    bestscore = int(f.readline())
