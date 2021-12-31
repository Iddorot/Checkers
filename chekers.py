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
    rect_counter = False
    player_counter = 1
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
                    if player_counter % 2 == 1:

                        if piece.color == "white":
                            if not rect_counter:
                                rect = (x * SQUARE_DIMENSION, y * SQUARE_DIMENSION, SQUARE_DIMENSION, SQUARE_DIMENSION)
                                pygame.draw.rect(screen, RED, rect, 5)
                                from_piece = piece
                                rect_counter = True
                            elif rect_counter:
                                gui.clean_screen(game_board)
                                rect = (x * SQUARE_DIMENSION, y * SQUARE_DIMENSION, SQUARE_DIMENSION, SQUARE_DIMENSION)
                                pygame.draw.rect(screen, RED, rect, 5)
                                from_piece = piece
                                rect_counter = True

                        elif piece.color == "blank" and rect_counter:
                            to_piece = piece
                            gui.make_move(game_board, from_piece, to_piece)
                            rect_counter = False
                            player_counter += 1
                    else:

                        if piece.color == "dark":
                            if not rect_counter:
                                rect = (x * SQUARE_DIMENSION, y * SQUARE_DIMENSION, SQUARE_DIMENSION, SQUARE_DIMENSION)
                                pygame.draw.rect(screen, RED, rect, 5)
                                from_piece = piece
                                rect_counter = True
                            elif rect_counter:
                                gui.clean_screen(game_board)
                                rect = (x * SQUARE_DIMENSION, y * SQUARE_DIMENSION, SQUARE_DIMENSION, SQUARE_DIMENSION)
                                pygame.draw.rect(screen, RED, rect, 5)
                                from_piece = piece
                                rect_counter = True
                        elif piece.color == "blank" and rect_counter:
                            to_piece = piece
                            gui.make_move(game_board, from_piece, to_piece)
                            rect_counter = False
                            player_counter += 1

        gui.draw_pieces(game_board.board)
