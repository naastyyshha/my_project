import copy
import sys
import pygame
from logic import *
from utils import terminate, CP

pygame.init()


class Board:
    def __init__(self, width, height, screen, theme='light'):
        self.theme = theme
        self.width = width
        self.height = height
        self.screen = screen
        self.board = [[0] * width for _ in range(height)]
        self.numbers = ['2', '4', '8', '16', '32', '64', '128',
                        '256', '512', '1024', '2048', '4048', '8096']
        self.colors = [pygame.Color('#B6B6B2')]
        pygame.font.init()
        # self.myfont = pygame.font.SysFont("Comic Sans MS", 30)

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def insert_2_or_4(self):
        temp_board = copy.deepcopy(self.board)
        flag = True
        x, y = random.randrange(self.width), random.randrange(self.height)
        while flag:
            if temp_board[y][x] == 0:
                flag = False
            else:
                x, y = random.randrange(self.width), random.randrange(self.height)
        if random.random() <= 0.75:
            temp_board[y][x] = 2
        else:
            temp_board[y][x] = 4
        self.board = copy.deepcopy(temp_board)

    def right_move(self):
        self.insert_2_or_4()
        temp_board = copy.deepcopy(self.board)
        tmp = moveRight(temp_board)
        self.board = copy.deepcopy(tmp)

    def left_move(self):
        self.insert_2_or_4()
        temp_board = copy.deepcopy(self.board)
        moveLeft(temp_board)
        self.board = copy.deepcopy(temp_board)

    def up_move(self):
        self.insert_2_or_4()
        temp_board = copy.deepcopy(self.board)
        tmp = moveUp(temp_board)
        self.board = copy.deepcopy(tmp)

    def down_move(self):
        self.insert_2_or_4()
        temp_board = copy.deepcopy(self.board)
        tmp = moveDown(temp_board)
        self.board = copy.deepcopy(tmp)

    def update(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.left_move()
                        run = False
                    if event.key == pygame.K_RIGHT:
                        self.right_move()
                        run = False
                    if event.key == pygame.K_UP:
                        self.up_move()
                        run = False
                    if event.key == pygame.K_DOWN:
                        self.down_move()
                        run = False
        # if new_board != board:
        #     # fill 2/4 after every move
        #     self.insert_2_or_4()
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
                if self.board[y][x] != 0:
                    color = CP[self.board[y][x]]
                    pygame.draw.rect(self.screen, color,
                                     rect=(x * self.cell_size + self.left + 10, self.top + self.cell_size * y + 10,
                                           self.cell_size - 20, self.cell_size - 20))
                    font = pygame.font.Font(None, 100)
                    text = font.render(f'{str(self.board[y][x])}', True, (255, 255, 255))
                    place = text.get_rect(center=(x * self.cell_size + self.left + self.cell_size // 2,
                                                  self.top + self.cell_size * y + self.cell_size // 2))
                    self.screen.blit(text, place)

    # def restart(board, theme, text_col):
    #     """
    #     Ask user to restart the game if 'n' key is pressed.
    #
    #     Parameters:
    #         board (list): game board
    #         theme (str): game interface theme
    #         text_col (tuple): text colour
    #     Returns:
    #         board (list): new game board
    #     """
    #     # Fill the window with a transparent background
    #     s = pygame.Surface((c["size"], c["size"]), pygame.SRCALPHA)
    #     s.fill(c["colour"][theme]["over"])
    #     screen.blit(s, (0, 0))
    #
    #     screen.blit(my_font.render("RESTART? (y / n)", 1, text_col), (85, 225))
    #     pygame.display.update()
    #
    #     while True:
    #         for event in pygame.event.get():
    #             if event.type == QUIT or \
    #                     (event.type == pygame.KEYDOWN and event.key == K_n):
    #                 pygame.quit()
    #                 sys.exit()
    #
    #             if event.type == pygame.KEYDOWN and event.key == K_y:
    #                 board = newGame(theme, text_col)
    #                 return board

    def newGame(self, theme, text_col):
        temp_board = copy.deepcopy(self.board)
        temp_board = [[0] * self.width for _ in range(self.height)]
        self.board = copy.deepcopy(temp_board)
        self.insert_2_or_4()
        self.insert_2_or_4()
        # display(board, theme)
        self.update()

        # screen.blit(my_font.render("NEW GAME!", 1, text_col), (130, 225))
        # pygame.display.update()
        # wait for 1 second before starting over
        # time.sleep(1)




    # def new_cell(self):
    #     temp_board = copy.deepcopy(self.board)
    #     flag = True
    #     x, y = random.randrange(self.width), random.randrange(self.height)
    #     while flag:
    #         if temp_board[y][x] == None:
    #             flag = False
    #         else:
    #             x, y = random.randrange(self.width), random.randrange(self.height)
    #
    #     num = random.choice(self.create_cell)
    #     temp_board[y][x] = num
    #     self.board = copy.deepcopy(temp_board)
