import copy
import sys

import pygame
import random


class Board:
    def __init__(self, width, height, screen):
        self.width = width
        self.height = height
        self.screen = screen
        self.board = [[None] * width for _ in range(height)]
        self.numbers = ['2', '4', '8', '16', '32', '64', '128',
                        '256', '512', '1024', '2048', '4048', '8096']
        self.colors = [pygame.Color('#B6B6B2')]
        self.current_color = 0

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, surf):
        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                pygame.draw.rect(
                    surface=surf,
                    color=pygame.Color('#A5A398'),
                    rect=(x * self.cell_size + self.left,
                          y * self.cell_size + self.top,
                          self.cell_size,
                          self.cell_size))

                pygame.draw.rect(
                    surface=surf,
                    color=pygame.Color('#B6B6B2'),
                    rect=(
                        x * self.cell_size + self.left + 10,
                        y * self.cell_size + self.top + 10,
                        self.cell_size - 20,
                        self.cell_size - 20))

    def get_cell(self, mouse_pos):
        mx, my = mouse_pos
        cell_x = (mx - self.left) // self.cell_size
        cell_y = (my - self.top) // self.cell_size
        if 0 <= cell_y < self.height and 0 <= cell_x < self.width:
            return cell_x, cell_y
        return None

    def on_click(self, cell_coords):
        x, y = cell_coords
        self.change_cell_color(x, y)

    def change_cell_color(self, x, y):
        x, y = x, y
        if self.board[y][x] == 1:
            self.board[y][x] = 0
        else:
            self.board[y][x] = 1

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)

    def get_move(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)


class Moves(Board):
    def __init__(self, wight, height, screen):
        super().__init__(wight, height, screen)

        # self.acceptable = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (3, 3), (2, 3), (1, 3)]
        self.create_cell = [2, 4]

    def new_cell(self):
        temp_board = copy.deepcopy(self.board)
        flag = True
        x, y = random.randrange(self.width), random.randrange(self.height)
        while flag:
            if temp_board[y][x] == None:
                flag = False
            else:
                x, y = random.randrange(self.width), random.randrange(self.height)

        num = random.choice(self.create_cell)
        temp_board[y][x] = num
        self.board = copy.deepcopy(temp_board)

    def right_move(self):
        self.new_cell()

    def left_move(self):
        self.new_cell()

    def up_move(self):
        self.new_cell()

    def down_move(self):
        self.new_cell()

    def update(self):
        flag = True
        while flag:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    sys.exit()
                if i.type == pygame.KEYDOWN:
                    if i.key == pygame.K_LEFT:
                        self.left_move()
                        flag = False
                    if i.key == pygame.K_RIGHT:
                        self.right_move()
                        flag = False
                    if i.key == pygame.K_UP:
                        self.up_move()
                        flag = False
                    if i.key == pygame.K_DOWN:
                        self.down_move()
                        flag = False
        for y in range(self.height):
            for x in range(self.width):
                # ----------------------- интерфейс -------------------------
                pygame.draw.rect(self.screen, pygame.Color('#A5A398'),
                                 (x * self.cell_size + self.left, y * self.cell_size + self.top,
                                  self.cell_size, self.cell_size))
                pygame.draw.rect(self.screen, pygame.Color('#B6B6B2'),
                                 (x * self.cell_size + self.left + 10, y * self.cell_size + self.top + 10,
                                  self.cell_size - 20, self.cell_size - 20))
                # -------------------------------------------------------------
                if self.board[y][x] != None:
                    color = 'blue'
                    pygame.draw.rect(self.screen, color,
                                     rect=(x * self.cell_size + self.left + 10, self.top + self.cell_size * y + 10,
                                           self.cell_size - 20, self.cell_size - 20))
                    font = pygame.font.Font(None, 100)
                    text = font.render(f'{str(self.board[y][x])}', True, (255, 255, 255))
                    place = text.get_rect(center=(x * self.cell_size + self.left + self.cell_size // 2,
                                                  self.top + self.cell_size * y + self.cell_size // 2))
                    self.screen.blit(text, place)
