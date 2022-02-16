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
TEXT_SIZE = 100

# rgb: red green blue
RED = (255, 0, 0)
SQUARE_COLOR = (147, 80, 0)
BRIGHT_SQUARE_COLOR = (160, 90, 0)
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
white_p_img = pygame.transform.scale(white_p_img, (SQUARE_DIMENSION, SQUARE_DIMENSION))
WHITE = white_p_img

white_king_img = pygame.image.load("white_king.png")
white_king_img.convert()
white_king_img = pygame.transform.scale(white_king_img, (SQUARE_DIMENSION // 2, SQUARE_DIMENSION // 2))
WHITE_KING = white_king_img

dark_p_img = pygame.image.load("dark_p.png")
dark_p_img.convert()
dark_p_img = pygame.transform.scale(dark_p_img, (SQUARE_DIMENSION, SQUARE_DIMENSION))
DARK = dark_p_img

dark_king_img = pygame.image.load("dark_king.png")
dark_king_img.convert()
dark_king_img = pygame.transform.scale(dark_king_img, (SQUARE_DIMENSION // 2, SQUARE_DIMENSION // 2))
DARK_KING = dark_king_img

# -------------
# CONSOLE BOARD
# -------------
board = np.zeros((BOARD_ROWS, BOARD_COLS))



