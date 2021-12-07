import pygame, sys, os
import numpy as np
from pygame.locals import *
import configuration
from configuration import screen, SQUARE_DIMENSION,BOARD_POS
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

            # if event.type == pygame.MOUSEBUTTONDOWN:
            # x, y = pygame.mouse.get_pos()
        piece, x, y = game_board.get_square_under_mouse()

        if x is not None:
            rect = (BOARD_POS[0] + x * SQUARE_DIMENSION, BOARD_POS[1] + y * SQUARE_DIMENSION, SQUARE_DIMENSION, SQUARE_DIMENSION)
            pygame.draw.rect(screen, (255, 0, 0, 50), rect, 2)

        clock.tick(60)



        pygame.display.update()
