import pygame
import numpy as np
from pygame.locals import *

# CONSTANTS
# ---------
WIDTH = 800
HEIGHT = 800
BOARD_ROWS = 8
BOARD_COLS = 8
SQUARE_DIMENSION = WIDTH // BOARD_COLS

# rgb: red green blue
RED = (255, 0, 0)
BG_COLOR = (28, 170, 156)
SQUARE_COLOR = (147, 80, 0)

# ------
# SCREEN
# ------

background_img = pygame.image.load('BG.png')
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('CHECKERS')
screen.blit(background_img, (0, 0))

# ------
# PIECES
# ------

white_p_img = pygame.image.load("white_p.png")
white_p_img.convert()
white_p_img = pygame.transform.scale(white_p_img, (100, 100))
WHITE = white_p_img

dark_p_img = pygame.image.load("dark_p.png")
dark_p_img.convert()
dark_p_img = pygame.transform.scale(dark_p_img, (100, 100))
DARK = dark_p_img
# -------------
# CONSOLE BOARD
# -------------
board = np.zeros((BOARD_ROWS, BOARD_COLS))
