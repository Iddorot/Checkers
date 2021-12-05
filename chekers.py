import pygame, sys, os
import numpy as np
from pygame.locals import *
import configuration
from configuration import screen
import board

# initializes pygame
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()


class Game:

    # ---------
    # VARIABLES
    # ---------

    player = 1
    game_over = False

    # --------
    # MAINLOOP
    # --------

    #moving = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # elif event.type == MOUSEBUTTONDOWN:
            #     if white_rect.collidepoint(event.pos):
            #         moving = True
            #     elif dark_rect.collidepoint(event.pos):
            #         moving = True
            # elif event.type == MOUSEBUTTONUP:
            #     moving = False
            #
            # elif event.type == MOUSEMOTION and moving:
            #     white_rect.move_ip(event.rel)
            #
            #
            # elif event.type == MOUSEMOTION and moving:
            #     dark_rect.move_ip(event.rel)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:

                    player = 1
                    game_over = False

        game_board = board.Board()
        game_board.draw(screen)


        pygame.display.update()
