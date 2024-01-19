import pygame
from best_score import result
from logic import Button, bestscore, Barbie
from main_board import Board, drawing
from utils import terminate, FPS, SCREEN_SIZE, HEIGHT, WIDTH, WHITE, CELL_COLORS, mfont

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)

difficulty = 2048


# Функция главного меню
def showMenu():
    # создание кнопок
    btn_2048 = Button(CELL_COLORS[32], 300, 270, 80, 80, "2048")
    btn_1024 = Button(CELL_COLORS[16], 400, 270, 80, 80, "1024")
    btn_512 = Button(CELL_COLORS[32], 500, 270, 80, 80, "512")
    btn_256 = Button(CELL_COLORS[16], 600, 270, 80, 80, "256")

    # выбираем уровень сложности
    diff_selected = False
    global difficulty
    all_sprites = pygame.sprite.Group()
    barbie1 = Barbie('barb.png', all_sprites)
    # кнопка пуска
    btn_play = Button(CELL_COLORS[32], 360, 550, 100, 100, "play")

    run = True
    while run:

        # Добавляем задний фон
        background_img = pygame.transform.scale(pygame.image.load('./data/valentines_14.jpg'), (WIDTH, HEIGHT))
        screen.blit(background_img, (0, 0))

        screen.blit(pygame.transform.scale(
            pygame.image.load("./data/pngegg (1).png"), (300, 200)), (250, 50))

        font = pygame.font.SysFont(mfont, 30, bold=True)

        diff_text = font.render("Сложность: ", 1, (255, 255, 255))
        screen.blit(diff_text, (70, 290))

        # Рисовка кнопок на экране
        btn_2048.draw_btn(screen, WHITE)
        btn_1024.draw_btn(screen, WHITE)
        btn_512.draw_btn(screen, WHITE)
        btn_256.draw_btn(screen, WHITE)
        btn_play.draw_btn(screen, WHITE)

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            # Выход из игры
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                terminate()

            # Проверка на нажатие кнопки, если нажата - выделяем ее
            if event.type == pygame.MOUSEBUTTONDOWN:

                if btn_2048.touched(pos):
                    btn_2048.colour = CELL_COLORS[512]
                    btn_1024.colour = CELL_COLORS[32]
                    btn_512.colour = CELL_COLORS[32]
                    btn_256.colour = CELL_COLORS[32]
                    difficulty = 2048
                    diff_selected = True

                if btn_1024.touched(pos):
                    btn_1024.colour = CELL_COLORS[512]
                    btn_2048.colour = CELL_COLORS[32]
                    btn_512.colour = CELL_COLORS[32]
                    btn_256.colour = CELL_COLORS[32]
                    difficulty = 1024
                    diff_selected = True

                if btn_512.touched(pos):
                    btn_512.colour = CELL_COLORS[512]
                    btn_1024.colour = CELL_COLORS[32]
                    btn_2048.colour = CELL_COLORS[32]
                    btn_256.colour = CELL_COLORS[32]
                    difficulty = 512
                    diff_selected = True

                if btn_256.touched(pos):
                    btn_256.colour = CELL_COLORS[512]
                    btn_1024.colour = CELL_COLORS[32]
                    btn_512.colour = CELL_COLORS[32]
                    btn_2048.colour = CELL_COLORS[32]
                    difficulty = 256
                    diff_selected = True

                if btn_play.touched(pos):
                    if difficulty != 0:
                        game(difficulty)

                    btn_2048.colour = CELL_COLORS[32]
                    btn_1024.colour = CELL_COLORS[32]
                    btn_512.colour = CELL_COLORS[32]
                    btn_256.colour = CELL_COLORS[32]

            # смена цвета кнопки при движении
            if event.type == pygame.MOUSEMOTION:

                if not diff_selected:
                    if btn_2048.touched(pos):
                        btn_2048.colour = CELL_COLORS[512]
                    else:
                        btn_2048.colour = CELL_COLORS[32]

                    if btn_1024.touched(pos):
                        btn_1024.colour = CELL_COLORS[512]
                    else:
                        btn_1024.colour = CELL_COLORS[32]

                    if btn_512.touched(pos):
                        btn_512.colour = CELL_COLORS[512]
                    else:
                        btn_512.colour = CELL_COLORS[32]

                    if btn_256.touched(pos):
                        btn_256.colour = CELL_COLORS[512]
                    else:
                        btn_256.colour = CELL_COLORS[32]

                if btn_play.touched(pos):
                    btn_play.colour = CELL_COLORS[512]
                else:
                    btn_play.colour = CELL_COLORS[32]
        barbie1.update(screen, 150, 730, 1.5)
        pygame.display.flip()


# Функция главного окна
def game(difficulty):
    running = True
    clock = pygame.time.Clock()
    game_board = Board(screen, difficulty)

    while running:
        clock.tick(FPS)

        drawing(screen, game_board.board, game_board.cells, game_board.score, game_board.over, bestscore)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            # Ходы игры
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    game_board.left_move()
                if event.key == pygame.K_RIGHT:
                    game_board.right_move()
                if event.key == pygame.K_UP:
                    game_board.up_move()
                if event.key == pygame.K_DOWN:
                    game_board.down_move()
                if event.key == pygame.K_q and pygame.key.get_mods() & pygame.KMOD_CTRL and game_board.over:
                    game_board.reset()


clock = pygame.time.Clock()
run = True
while run:
    showMenu()
    game(difficulty)
