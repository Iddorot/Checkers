import pygame, sys, os
from pygame import Color, Surface
import numpy as np
from pygame.locals import *
import configuration
from configuration import screen, SQUARE_DIMENSION
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
        game_board.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_click = mouse_click + 1

                if mouse_click % 2 == 0:
                    game_board.clean_screen()


                else:
                    piece, x, y = game_board.get_square_under_mouse()

                    if x is not None:
                        rect = (x * SQUARE_DIMENSION, y * SQUARE_DIMENSION, SQUARE_DIMENSION, SQUARE_DIMENSION)
                        pygame.draw.rect(screen, (255, 0, 0, 50), rect, 10)

        clock.tick(60)

        pygame.display.update()
