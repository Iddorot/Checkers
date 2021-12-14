import pygame, sys, os
import numpy as np
from pygame.locals import *
import configuration
from configuration import SQUARE_DIMENSION, BOARD_ROWS, BOARD_COLS, SQUARE_COLOR, screen, WHITE, DARK, background_img
from piece import Piece


# TODO https://www.youtube.com/watch?v=hDu8mcAlY4E
class Crosshair(pygame.sprit.Sprite):
    def __init__(self):
        pass

    super().__init__()

    def get_square_under_mouse(self):
        mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
        x, y = [int(v // SQUARE_DIMENSION) for v in mouse_pos]
        try:
            if x >= 0 and y >= 0:
                return self.board[y][x], x, y
        except IndexError:
            return "IndexError"
        return None, None, None

    def clean_screen(self):
        screen.blit(background_img, (0, 0))
