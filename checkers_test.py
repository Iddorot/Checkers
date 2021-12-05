# MODULES
import pygame, sys, os
import numpy as np
from pygame.locals import *

# initializes pygame
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
# ---------
# CONSTANTS
# ---------
WIDTH = 800
HEIGHT = 800
BOARD_ROWS = 8
BOARD_COLS = 8
SPACE = 55
# rgb: red green blue
RED = (255, 0, 0)
BG_COLOR = (28, 170, 156)
SQUARE_COLOR = (147, 80, 0)

# ------
# SCREEN
# ------

background_img = pygame.image.load(r'C:\Users\Admin\Documents\Python\4549337167049_01_1260.png')
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('CHECKERS')
screen.blit(background_img, (0, 0))

screen_list = [0, 'w', 0, 'w', 0, 'w', 0, 'w']

# ------
# PIECES
# ------

white_p_img = pygame.image.load(r"C:\Users\Admin\Documents\Python\white_p.png")
white_p_img.convert()
white_p_img = pygame.transform.scale(white_p_img, (100, 100))
white_rect = white_p_img.get_rect()
white_rect.center = WIDTH // 2, HEIGHT // 2

dark_p_img = pygame.image.load(r"C:\Users\Admin\Documents\Python\dark_p.png")
dark_p_img.convert()
dark_p_img = pygame.transform.scale(dark_p_img, (100, 100))
dark_rect = white_p_img.get_rect()
dark_rect.center = WIDTH // 2, HEIGHT // 2

# -------------
# CONSOLE BOARD
# -------------
board = np.zeros((BOARD_ROWS, BOARD_COLS))


# ---------
# FUNCTIONS
# ---------
def draw_square():
    for l in range(0, 8, 2):
        for i in range(1, 8, 2):
            pygame.draw.rect(screen, SQUARE_COLOR, pygame.Rect(100 * i, l * 100, 100, 100))
    for l in range(1, 8, 2):
        for i in range(0, 8, 2):
            pygame.draw.rect(screen, SQUARE_COLOR, pygame.Rect(100 * i, l * 100, 100, 100))


def draw_pieces():
    white_p_count = 0
    dark_p_count = 0
    whitePos_lst = []
    darkPos_lst = []
    for l in range(0, 3):
        if l == 1:
            for i in range(0, 8, 2):
                screen.blit(white_p_img, (100 * i, 100 * l))
                white_p_img.convert()
                rect = white_p_img.get_rect()
                rect.center = WIDTH // 2, HEIGHT // 2
                white_p_count += 1
                whitePos_lst.append(current_str)

        else:

            for i in range(1, 8, 2):
                screen.blit(white_p_img, (100 * i, 100 * l))
                white_p_img.convert()
                rect = white_p_img.get_rect()
                rect.center = WIDTH // 2, HEIGHT // 2
                white_p_count += 1
                current_str = f"whiteP{l}+{i}"
                whitePos_lst.append(current_str)

    for l in range(5, 8):
        if l == 6:
            for i in range(1, 8, 2):
                screen.blit(dark_p_img, (100 * i, 100 * l))
                rect = dark_p_img.get_rect()
                rect.center = WIDTH // 2, HEIGHT // 2
                dark_p_count += 1
                current_str = f"darkP{l}+{i}"
                darkPos_lst.append(current_str)
        else:

            for i in range(0, 8, 2):
                screen.blit(dark_p_img, (100 * i, 100 * l))
                dark_p_count += 1
                rect = dark_p_img.get_rect()
                rect.center = WIDTH // 2, HEIGHT // 2
                current_str = f"darkP{l}+{i}"
                darkPos_lst.append(current_str)
    return white_p_count, dark_p_count, whitePos_lst, darkPos_lst

def pieces_map():
   screen = [[' ']*BOARD_ROWS]*BOARD_COLS
   if BOARD_ROWS < 4 :
      if BOARD_ 


def restart():
    screen.fill(BG_COLOR)
    draw_square()
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0


draw_square()
# ---------
# VARIABLES
# ---------
player = 1
game_over = False

# --------
# MAINLOOP
# --------
current_image = None
moving = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == MOUSEBUTTONDOWN:
            if white_rect.collidepoint(event.pos):
                moving = True
            elif dark_rect.collidepoint(event.pos):
                moving = True
        elif event.type == MOUSEBUTTONUP:
            moving = False

        elif event.type == MOUSEMOTION and moving:
            white_rect.move_ip(event.rel)


        elif event.type == MOUSEMOTION and moving:
            dark_rect.move_ip(event.rel)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                player = 1
                game_over = False

    draw_pieces()
    pygame.display.update()
