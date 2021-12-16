import pygame, sys, os
from pygame import Color, Surface
import numpy as np
from pygame.locals import *
import configuration
from configuration import screen, SQUARE_DIMENSION, RED
import board
import piece

# initializes pygame
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()


class Game:
    # ---------
    # VARIABLES
    # ---------
    clock = pygame.time.Clock()

    player = 1
    game_over = False
    moving = False
    mouse_click = 0

    # --------
    # MAINLOOP
    # --------

    # moving = False
    while True:
        game_board = board.Board()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                piece, x, y = game_board.get_square_under_mouse()

                if piece != 0:
                    rect = (x * SQUARE_DIMENSION, y * SQUARE_DIMENSION, SQUARE_DIMENSION, SQUARE_DIMENSION)
                    pygame.draw.rect(screen, RED, rect, 10)
                    mouse_click += 1
                    from_point = (piece, x, y)

                if mouse_click % 2 == 0:
                    to_point = (piece, x, y)

                    game_board.clean_screen()
        game_board.draw(screen)
        clock.tick(60)

        pygame.display.update()
