import pygame

from utils import load_image

# tile_images = {
#     'wall': load_image('box.png'),
#     'empty': load_image('grass.png')
# }
# player_img = load_image('mar.png')
#
# tile_width = tile_height = 100

all_sprite = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
walls = pygame.sprite.Group()
player_group = pygame.sprite.Group()


# class Tile(pygame.sprite.Sprite):
#     def __init__(self, tile_type, x, y):
#         super().__init__(all_sprite, tiles_group)
#         self.image = pygame.transform.scale(tile_images.get(tile_type),
#                                             (tile_width, tile_height))
#         self.rect = self.image.get_rect().move(tile_width * x, tile_height * y)
#         if tile_type == 'wall':
#             self.add(walls)


# class Player(pygame.sprite.Sprite):
#     def __init__(self, x, y):
#         super().__init__(all_sprite, player_group)
#         self.image = pygame.transform.scale(player_img, (48, 80))
#         self.rect = self.image.get_rect().move(tile_width * x + 25, tile_height * y + 5)

#     def update(self, event):
#         dx, dy = 0, 0
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_w:
#                 dy = -tile_height
#             if event.key == pygame.K_s:
#                 dy = tile_height
#             if event.key == pygame.K_a:
#                 dx = -tile_width
#             if event.key == pygame.K_d:
#                 dx = tile_width
#
#         self.rect = self.rect.move(dx, dy)
#         if pygame.sprite.spritecollide(self, walls, dokill=False):
#             self.rect = self.rect.move(-dx, -dy)
#
#
# def generate_level(level):
#     new_player = None
#     for y, row in enumerate(level):
#         for x, cell in enumerate(row):
#             if cell == '#':  # создается стенка
#                 Tile('wall', x, y)
#             elif cell == '.':  # создается дорожка
#                 Tile('empty', x, y)
#             elif cell == '@':  # создается место героя
#                 Tile('empty', x, y)
#                 new_player = Player(x, y)
#     return new_player

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.numbers = ['2', '4', '8', '16', '32', '64', '128',
                        '256', '512', '1024', '2048', '4048', '8096']
        self.colors = [pygame.Color('#B6B6B2'), pygame.Color(255, 0, 0), pygame.Color(0, 0, 255)]
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
                    color=pygame.Color('#A5A398'),
                    rect=(
                        x * self.cell_size + self.left,
                        y * self.cell_size + self.top,
                        self.cell_size,
                        self.cell_size),
                    width=1)

                pygame.draw.rect(
                    surface=surf,
                    color=self.colors[self.board[y][x]],
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
        if self.board[y][x] == 1:
            self.board[y][x] = 2
        elif self.board[y][x] == 2:
            self.board[y][x] = 0
        else:
            self.board[y][x] = 1

    # def get_click(self, mouse_pos):
    #     cell = self.get_cell(mouse_pos)
    #     if cell:
    #         self.on_click(cell)
    def get_move(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)
