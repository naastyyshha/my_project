import sys
from copy import deepcopy

import pygame
from logic import insert_2_or_4
from menu import main_menu
from main_board import Board
from utils import terminate, SCREEN_SIZE, FPS, BLACK, WHITE

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)


def game():
    pygame.display.set_caption('2048')

    board = Board(4, 4, screen)
    board.set_view(160, 50, 120)
    run = True
    while run:
        clock = pygame.time.Clock()
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
            board.update()
            pygame.display.update()
            clock.tick(FPS)


clock = pygame.time.Clock()
run = True
while run:
    main_menu(screen)
    game()
