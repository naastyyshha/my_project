import pygame
import random
from best_score import result, cur
from utils import CELL_NUMBER_COLORS, SCORE_LABEL_FONT, sizes, EMPTY_CELL_COLOR, CELL_COLORS, WIDTH, HEIGHT, \
    WHITE, terminate
from logic import bestscore, Barbie


class Board:
    def __init__(self, screen, difficulty):
        self.screen = screen
        self.difficulty = difficulty
        self.width = 4
        self.height = 4
        self.cell_size = 120
        self.left = 160
        self.board = [[2, 4, 16, 128],
                      [8, 2, 32, 128],
                      [64, 0, 8, 16],
                      [1024, 512, 512, 0]]  # The matrix that holds the values
        # self.board = [[0] * self.width for _ in range(self.height)]
        self.cells = []  # в первой ячейке число, во второй ячейке параметры для рисования
        self.score = [0, 0]  # в первой ячейке счет, во второй ячейке параметры для рисования
        self.over = [False,
                     False]  # В первой ячейке проверяется закончилась ли игра или нет, во второй ячейке проверяется выигрыш или проигрыш
        self.startGame()

    # Создание новой игры
    def startGame(self):

        # Добавляем две новые ячейки
        self.addNewCell()
        self.addNewCell()

        for y in range(1, self.height + 1):
            cell = []
            for x in range(self.width):
                rect = pygame.Rect(160 + x * 120, 10 + y * 120, 100, 100)
                textRect, textSurface = None, None
                if self.board[y - 1][x] != 0:
                    font = pygame.font.SysFont(SCORE_LABEL_FONT, sizes[self.board[y - 1][x]])
                    textSurface = font.render(str(self.board[y - 1][x]), True, CELL_NUMBER_COLORS[self.board[y - 1][x]])
                    textRect = textSurface.get_rect()
                    textRect.center = rect.center
                cell.append({
                    "rect": rect,
                    "textRect": textRect,
                    "textSurface": textSurface
                })
            self.cells.append(cell)

        # Создание окна с счетчиком
        scoreSurface = pygame.font.SysFont(SCORE_LABEL_FONT, 50).render('Score : ', True, WHITE)
        scoreRect = scoreSurface.get_rect()
        scoreRect.top = 25
        scoreRect.left = 30
        self.score[1] = [scoreSurface, scoreRect]

    def addNewCell(self):
        # Создание новой ячейки
        flag = True
        x, y = random.randrange(self.width), random.randrange(self.height)
        while flag:
            if self.board[y][x] == 0:
                flag = False
            else:
                x, y = random.randrange(self.width), random.randrange(self.height)
        if random.random() <= 0.75:
            self.board[y][x] = 2
        else:
            self.board[y][x] = 4

    def horMoves(self):
        # Проверка на возможность горизонтального движения
        for y in range(self.height):
            for x in range(self.width - 1):
                if self.board[y][x + 1] == self.board[y][x]:
                    return True
        return False

    def verMoves(self):
        # Проверка на возможность горизонтального движения
        for y in range(self.height - 1):
            for x in range(self.width):
                if self.board[y + 1][x] == self.board[y][x]:
                    return True
        return False

    def gameOver(self):
        # Проверка на окончание игры
        if any(self.difficulty in row for row in self.board):
            self.over = [True, True]
        if not any(0 in row for row in self.board) and not self.horMoves() and not self.verMoves():
            self.over = [True, False]

    def updateCells(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] != 0:
                    font = pygame.font.SysFont(SCORE_LABEL_FONT, sizes[self.board[y][x]])
                    textSurface = font.render(f'{self.board[y][x]}', True, CELL_NUMBER_COLORS[self.board[y][x]])
                    textRect = textSurface.get_rect()
                    textRect.center = self.cells[y][x]['rect'].center
                    self.cells[y][x]['textRect'] = textRect
                    self.cells[y][x]['textSurface'] = textSurface
                elif self.board[y][x] == 0:
                    self.cells[y][x]['textRect'] = None
                    self.cells[y][x]['textSurface'] = None

    def stack(self):
        # Перемещяет все ячейки влево
        new_board = [[0] * self.width for _ in range(self.height)]
        for y in range(self.height):
            position = 0
            for x in range(self.width):
                if self.board[y][x] != 0:
                    new_board[y][position] = self.board[y][x]
                    position += 1
        self.board = new_board

    def combine(self):
        # Cложение ячеек
        for y in range(4):
            for x in range(3):
                if self.board[y][x] != 0 and self.board[y][x] == self.board[y][x + 1]:
                    self.board[y][x] *= 2
                    self.board[y][x + 1] = 0
                    self.score[0] += self.board[y][x]

    def reverse(self):
        # Функция переворачивающая списки
        new_board = []
        for row in self.board:
            new_board.append(row[::-1])
        self.board = new_board

    def transpose(self):
        new_board = [[0] * 4 for _ in range(4)]
        for y in range(4):
            for x in range(4):
                new_board[x][y] = self.board[y][x]
        self.board = new_board

    def scs(self):
        # Несколько функций в одной
        old_board = self.board
        self.stack()
        self.combine()
        self.stack()
        return old_board

    def aug(self):
        # Функция добавляем новые ячейки и проверяет не закончилась ли игра
        self.addNewCell()
        self.updateCells()
        self.gameOver()

    def left_move(self):
        old_board = self.scs()
        if old_board == self.board:
            return
        self.aug()

    def right_move(self):
        old_board = self.board
        self.reverse()
        self.scs()
        self.reverse()
        if old_board == self.board:
            return
        self.aug()

    def up_move(self):
        old_board = self.board
        self.transpose()
        self.scs()
        self.transpose()
        if old_board == self.board:
            return
        self.aug()

    def down_move(self):
        old_board = self.board
        self.transpose()
        self.reverse()
        self.scs()
        self.reverse()
        self.transpose()
        if old_board == self.board:
            return
        self.aug()

    def reset(self):
        self.__init__(self.screen, difficulty=2048)


def drawing(window, board, cells, score, over, bestscore):
    # Функция, с помощью которой параметры показываются на экране
    background_img = pygame.transform.scale(pygame.image.load('./data/bgrnd.jpg'), (WIDTH, HEIGHT))
    window.blit(background_img, (0, 0))
    pygame.draw.rect(window, pygame.Color('#A5A398'),
                     (140, 110,
                      500, 500), 0, 10)
    window.blit(score[1][0], score[1][1])
    # Счетчик
    scoreSurface = pygame.font.SysFont(SCORE_LABEL_FONT, 50).render(str(score[0]), True, WHITE)
    scoreRect = scoreSurface.get_rect()
    scoreRect.top = 30
    scoreRect.left = score[1][1].right + 20
    window.blit(scoreSurface, scoreRect)
    # Все ячейки
    for y in range(4):
        for x in range(4):
            cell = cells[y][x]
            if board[y][x] != 0:
                pygame.draw.rect(window, CELL_COLORS[board[y][x]], cell['rect'], 0, 10)
                window.blit(cell['textSurface'], cell['textRect'])
            elif board[y][x] == 0:
                pygame.draw.rect(window, EMPTY_CELL_COLOR, cell['rect'], 0, 10)
    # Game Over
    if over[0] and over[1]:
        if score[0] > bestscore:
            NewRecord1 = pygame.font.SysFont(SCORE_LABEL_FONT, 25).render('Новый рекорд!', True,
                                                                          WHITE)
            NewRecord1Rect = NewRecord1.get_rect()
            NewRecord1Rect.center = (WIDTH // 2, HEIGHT // 2)
            bestscore = score[0]
            NewRecord2 = pygame.font.SysFont(SCORE_LABEL_FONT, 50).render(str(score[0]), True,
                                                                      WHITE)
            NewRecord2Rect = NewRecord2.get_rect()
            NewRecord2Rect.center = (WIDTH // 2, HEIGHT // 2 + 100)
            window.blit(NewRecord1, NewRecord1Rect)
            window.blit(NewRecord2, NewRecord2Rect)
        gameOverSurface1 = pygame.font.SysFont(SCORE_LABEL_FONT, 25).render('Вы выиграли!', True,
                                                                            WHITE)
        gameOverSurface2 = pygame.font.SysFont(SCORE_LABEL_FONT, 25).render('Нажмите Ctrl + q или крестик чтобы выйти',
                                                                            True,
                                                                            WHITE)

        gameOverRect1 = gameOverSurface1.get_rect()
        gameOverRect1.center = (WIDTH // 2, HEIGHT // 2 - 200)
        gameOverRect2 = gameOverSurface1.get_rect()
        gameOverRect2.center = (WIDTH // 2 - 150, HEIGHT // 2 - 130)
        background_img = pygame.transform.scale(pygame.image.load('./data/bgrn.jpg'), (WIDTH, HEIGHT))
        window.blit(background_img, (0, 0))
        window.blit(gameOverSurface1, gameOverRect1)
        window.blit(gameOverSurface2, gameOverRect2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                terminate()
    if over[0] and not over[1]:
        if score[0] > result:
            NewRecord1 = pygame.font.SysFont(SCORE_LABEL_FONT, 25).render('Новый рекорд!', True, WHITE)

            NewRecord1Rect = NewRecord1.get_rect()
            NewRecord1Rect.center = (WIDTH // 2, HEIGHT // 2)
        NewRecord2 = pygame.font.SysFont(SCORE_LABEL_FONT, 25).render(f'{score[0]}', True, WHITE)
        NewRecord2Rect = NewRecord2.get_rect()
        NewRecord2Rect.center = (WIDTH // 2, HEIGHT // 2)

        gameOverSurface1 = pygame.font.SysFont(SCORE_LABEL_FONT, 25).render('Вы проиграли.', True, WHITE)
        gameOverSurface2 = pygame.font.SysFont(SCORE_LABEL_FONT, 25).render('Нажмите Ctrl + q или крестик чтобы выйти',
                                                                            True, WHITE)
        gameOverRect1 = gameOverSurface1.get_rect()
        gameOverRect1.center = (WIDTH // 2, HEIGHT // 2 - 200)
        gameOverRect2 = gameOverSurface1.get_rect()
        gameOverRect2.center = (WIDTH // 2 - 100, HEIGHT // 2 - 130)

        background_img = pygame.transform.scale(pygame.image.load('./data/bgrn.jpg'), (WIDTH, HEIGHT))
        window.blit(background_img, (0, 0))
        window.blit(gameOverSurface1, gameOverRect1)
        window.blit(gameOverSurface2, gameOverRect2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                terminate()
    pygame.display.update()
