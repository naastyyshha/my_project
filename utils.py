import sys
import pygame

# Переменные
GRID_COLOR = "#E5E1D3"
EMPTY_CELL_COLOR = "#B6B6B2"
SCORE_LABEL_FONT = "Verdana"

mfont = "Verdana"

SCREEN_SIZE = WIDTH, HEIGHT = 800, 700
FPS = 60

WHITE = (255, 255, 255)

CELL_COLORS = {
    4: "#ffcff1",
    2: "#ffe5ec",
    16: "#cf91b5",
    512: "#8e3563",
    32: "#d996a7",
    256: "#b55385",
    128: "#ff8fab",
    64: "#ffc0ee",
    8: "#e0bbd2",
    1024: "#db76bc",
    2048: "#572649"
}

sizes = {2: 45,
         4: 45,
         8: 45,
         16: 40,
         32: 40,
         64: 40,
         128: 35,
         256: 35,
         512: 35,
         1024: 35,
         2048: 35}

CELL_NUMBER_COLORS = {
    2: "#695c57",
    4: "#695c57",
    8: "#ffffff",
    16: "#ffffff",
    32: "#ffffff",
    64: "#ffffff",
    128: "#ffffff",
    256: "#ffffff",
    512: "#ffffff",
    1024: "#ffffff",
    2048: "#ffffff"
}


def terminate():
    pygame.quit()
    sys.exit()



