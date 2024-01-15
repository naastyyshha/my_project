import pygame

from menu import main_menu
from main_board import Board
# from sprites import generate_level, tiles_group, player_group, all_sprite
from utils import terminate, SCREEN_SIZE, FPS, load_level, Camera

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)


def game():
    pygame.display.set_caption('2048')

    # game_level = load_level('map.txt')
    #
    # player = generate_level(game_level)
    board = Board(4, 4)
    board.set_view(160, 50, 120)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            # player.update(event)

        camera = Camera()
        clock = pygame.time.Clock()
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    board.get_click(event.pos)
            #     player.update(event)
            screen.fill('#E5E1D3')
            board.render(screen)
            #
            # camera.update(player)
            #
            # for sprite in all_sprite:
            #     camera.apply(sprite)
            #
            # tiles_group.draw(screen)
            # player_group.draw(screen)

            pygame.display.update()
            clock.tick(FPS)


clock = pygame.time.Clock()
run = True
while run:
    main_menu(screen)
    game()
