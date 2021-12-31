import pygame, sys, os
from pygame import Color, Surface
from pygame.locals import *
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
    game_board = board.Board()
    gui = player.Player()

    # --------
    # MAINLOOP
    # --------

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                piece, x, y = gui.get_square_under_mouse(game_board.board)
                if piece != 0:
                    if piece.color == "white" or piece.color == "dark":
                        rect = (x * SQUARE_DIMENSION, y * SQUARE_DIMENSION, SQUARE_DIMENSION, SQUARE_DIMENSION)
                        pygame.draw.rect(screen, RED, rect, 5)
                        from_point = (piece, x, y)

                    if piece.color == "blank":
                        to_point = (piece, x, y)

                        if gui.check_valid_move(game_board.board, from_point, to_point) == "one":
                            gui.clean_screen(game_board)
                            gui.make_move(game_board.board, from_point, to_point)

                        elif gui.check_valid_move(game_board.board, from_point, to_point) == "eat":

                            gui.clean_screen(game_board)
                            gui.eat(game_board.board, from_point, to_point)


        gui.draw_pieces(game_board.board)
