
import pygame

from utils import HEIGHT, WIDTH, terminate, FPS, BLACK


def main_menu(screen):
    intro_text = ["ЗАСТАВКА", "",
                  "Правила игры",
                  "Если в правилах несколько строк,",
                  "приходится выводить их построчно"]
    pygame.display.set_caption('2048')
    background_img = pygame.transform.scale(pygame.image.load('./data/fon.jpg'), (WIDTH, HEIGHT))
    font_obj = pygame.font.Font(None, 30)
    screen.blit(background_img, (0, 0))
    text_coord = 70
    for line in intro_text:
        string_rendered = font_obj.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    clock = pygame.time.Clock()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type in (pygame.MOUSEBUTTONDOWN, pygame.KEYDOWN):
                screen.fill('#E5E1D3')
                return
        pygame.display.update()
        clock.tick(FPS)
    #
    #     light_theme = Button(
    #         tuple(c["colour"]["light"]["2048"]), 200 - 70, 275, 45, 45, "light")
    #
    #     dark_theme = Button(
    #         tuple(c["colour"]["dark"]["2048"]), 270 - 70, 275, 45, 45, "dark")
    #
    #     theme = ""
    #     theme_selected = False
    #
    #
    #     _2048 = Button(tuple(c["colour"]["light"]["64"]),
    #                    130, 330, 45, 45, "2048")
    #     _1024 = Button(tuple(c["colour"]["light"]["2048"]),
    #                    200, 330, 45, 45, "1024")
    #     _512 = Button(tuple(c["colour"]["light"]["2048"]),
    #                   270, 330, 45, 45, "512")
    #     _256 = Button(tuple(c["colour"]["light"]["2048"]),
    #                   340, 330, 45, 45, "256")
    #
    #     # default difficulty
    #     difficulty = 0
    #     diff_selected = False
    #
    #     # create play button
    #     play = Button(tuple(c["colour"]["light"]["2048"]),
    #                   235, 400, 45, 45, "play")
    #
    #     # pygame loop for start screen
    #     while True:
    #         screen.fill(BLACK)

    #         screen.blit(pygame.transform.scale(
    #             pygame.image.load("images/icon.ico"), (200, 200)), (155, 50))
    #
    #         font = pygame.font.SysFont(c["font"], 15, bold=True)
    #
    #         theme_text = font.render("Theme: ", 1, WHITE)
    #         screen.blit(theme_text, (55, 285))
    #
    #         diff_text = font.render("Difficulty: ", 1, WHITE)
    #         screen.blit(diff_text, (40, 345))
    #
    #         # set fonts for buttons
    #         font1 = pygame.font.SysFont(c["font"], 15, bold=True)
    #         font2 = pygame.font.SysFont(c["font"], 14, bold=True)
    #
    #         # draw all buttons on the screen
    #         light_theme.draw(screen, BLACK, font1)
    #         dark_theme.draw(screen, (197, 255, 215), font1)
    #         _2048.draw(screen, BLACK, font2)
    #         _1024.draw(screen, BLACK, font2)
    #         _512.draw(screen, BLACK, font2)
    #         _256.draw(screen, BLACK, font2)
    #         play.draw(screen, BLACK, font1)
    #
    #         pygame.display.update()
    #
    #         for event in pygame.event.get():
    #             # store mouse position (coordinates)
    #             pos = pygame.mouse.get_pos()
    #
    #             if event.type == pygame.QUIT or \
    #                     (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
    #                 # exit if q is pressed
    #                 pygame.quit()
    #                 sys.exit()
    #
    #             # check if a button is clicked
    #             if event.type == pygame.MOUSEBUTTONDOWN:
    #                 # select light theme
    #                 if light_theme.isOver(pos):
    #                     dark_theme.colour = tuple(c["colour"]["dark"]["2048"])
    #                     light_theme.colour = tuple(c["colour"]["light"]["64"])
    #                     theme = "light"
    #                     theme_selected = True
    #
    #                 # select dark theme
    #                 if dark_theme.isOver(pos):
    #                     dark_theme.colour = tuple(c["colour"]["dark"]["background"])
    #                     light_theme.colour = tuple(c["colour"]["light"]["2048"])
    #                     theme = "dark"
    #                     theme_selected = True
    #
    #                 if _2048.isOver(pos):
    #                     _2048.colour = tuple(c["colour"]["light"]["64"])
    #                     _1024.colour = tuple(c["colour"]["light"]["2048"])
    #                     _512.colour = tuple(c["colour"]["light"]["2048"])
    #                     _256.colour = tuple(c["colour"]["light"]["2048"])
    #                     difficulty = 2048
    #                     diff_selected = True
    #
    #                 if _1024.isOver(pos):
    #                     _1024.colour = tuple(c["colour"]["light"]["64"])
    #                     _2048.colour = tuple(c["colour"]["light"]["2048"])
    #                     _512.colour = tuple(c["colour"]["light"]["2048"])
    #                     _256.colour = tuple(c["colour"]["light"]["2048"])
    #                     difficulty = 1024
    #                     diff_selected = True
    #
    #                 if _512.isOver(pos):
    #                     _512.colour = tuple(c["colour"]["light"]["64"])
    #                     _1024.colour = tuple(c["colour"]["light"]["2048"])
    #                     _2048.colour = tuple(c["colour"]["light"]["2048"])
    #                     _256.colour = tuple(c["colour"]["light"]["2048"])
    #                     difficulty = 512
    #                     diff_selected = True
    #
    #                 if _256.isOver(pos):
    #                     _256.colour = tuple(c["colour"]["light"]["64"])
    #                     _1024.colour = tuple(c["colour"]["light"]["2048"])
    #                     _512.colour = tuple(c["colour"]["light"]["2048"])
    #                     _2048.colour = tuple(c["colour"]["light"]["2048"])
    #                     difficulty = 256
    #                     diff_selected = True
    #
    #                 # play game with selected theme
    #                 if play.isOver(pos):
    #                     if theme != "" and difficulty != 0:
    #                         playGame(theme, difficulty)
    #
    #                 # reset theme & diff choice if area outside buttons is clicked
    #                 if not play.isOver(pos) and \
    #                         not dark_theme.isOver(pos) and \
    #                         not light_theme.isOver(pos) and \
    #                         not _2048.isOver(pos) and \
    #                         not _1024.isOver(pos) and \
    #                         not _512.isOver(pos) and \
    #                         not _256.isOver(pos):
    #                     theme = ""
    #                     theme_selected = False
    #                     diff_selected = False
    #
    #                     light_theme.colour = tuple(c["colour"]["light"]["2048"])
    #                     dark_theme.colour = tuple(c["colour"]["dark"]["2048"])
    #                     _2048.colour = tuple(c["colour"]["light"]["2048"])
    #                     _1024.colour = tuple(c["colour"]["light"]["2048"])
    #                     _512.colour = tuple(c["colour"]["light"]["2048"])
    #                     _256.colour = tuple(c["colour"]["light"]["2048"])
    #
    #             # change colour on hovering over buttons
    #             if event.type == pygame.MOUSEMOTION:
    #                 if not theme_selected:
    #                     if light_theme.isOver(pos):
    #                         light_theme.colour = tuple(c["colour"]["light"]["64"])
    #                     else:
    #                         light_theme.colour = tuple(c["colour"]["light"]["2048"])
    #
    #                     if dark_theme.isOver(pos):
    #                         dark_theme.colour = tuple(c["colour"]["dark"]["background"])
    #                     else:
    #                         dark_theme.colour = tuple(c["colour"]["dark"]["2048"])
    #
    #                 if not diff_selected:
    #                     if _2048.isOver(pos):
    #                         _2048.colour = tuple(c["colour"]["light"]["64"])
    #                     else:
    #                         _2048.colour = tuple(c["colour"]["light"]["2048"])
    #
    #                     if _1024.isOver(pos):
    #                         _1024.colour = tuple(c["colour"]["light"]["64"])
    #                     else:
    #                         _1024.colour = tuple(c["colour"]["light"]["2048"])
    #
    #                     if _512.isOver(pos):
    #                         _512.colour = tuple(c["colour"]["light"]["64"])
    #                     else:
    #                         _512.colour = tuple(c["colour"]["light"]["2048"])
    #
    #                     if _256.isOver(pos):
    #                         _256.colour = tuple(c["colour"]["light"]["64"])
    #                     else:
    #                         _256.colour = tuple(c["colour"]["light"]["2048"])
    #
    #                 if play.isOver(pos):
    #                     play.colour = tuple(c["colour"]["light"]["64"])
    #                 else:
    #                     play.colour = tuple(c["colour"]["light"]["2048"])

