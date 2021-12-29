import pygame, sys, os
from pygame import Color, Surface
import numpy as np
from pygame.locals import *
import configuration
from configuration import screen, SQUARE_DIMENSION, RED
import board
import piece
import player

# initializes pygame
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()


class Game:
    # ---------
    # VARIABLES
    # ---------
    clock = pygame.time.Clock()

    game_over = False

    mouse_click = 0

    # --------
    # MAINLOOP
    # --------
    game_board = board.Board()
    gui = player.Player()
    # moving = False
    while True:


        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                piece, x, y = gui.get_square_under_mouse(game_board.board)
                if piece != 0:
                    if piece.color == "white" or piece.color == "dark":
                        rect = (x * SQUARE_DIMENSION, y * SQUARE_DIMENSION, SQUARE_DIMENSION, SQUARE_DIMENSION)
                        pygame.draw.rect(screen, RED, rect, 10)
                        mouse_click += 1
                        from_point = (piece, x, y)

                    if piece.color == "blank":
                        to_point = (piece, x, y)
                        gui.clean_screen()
                        game_board.draw_sqaures(screen)
                        gui.make_move(game_board.board, from_point, to_point)
                        gui.draw_pieces(game_board.board)


        gui.draw_pieces(game_board.board)



        clock.tick(60)

        pygame.display.update()
