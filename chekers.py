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
    player_turn = 'white'
    # --------
    # MAINLOOP
    # --------

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                piece, x, y = gui.get_square_under_mouse(game_board.board)
                rect = (x * SQUARE_DIMENSION, y * SQUARE_DIMENSION, SQUARE_DIMENSION, SQUARE_DIMENSION)

                if piece != 0:
                    if player_turn == "white":
                        if piece.color == player_turn:
                            from_piece, rect_counter = gui.draw_rect(rect, piece, rect_counter, game_board)

                        elif rect_counter and piece.color == "blank":
                            rect_counter = gui.second_click(game_board, rect_counter, piece, player_turn, from_piece)
                            if not rect_counter:
                                player_turn = 'dark'

                    elif player_turn == "dark":
                        if piece.color == player_turn:
                            from_piece, rect_counter = gui.draw_rect(rect, piece, rect_counter, game_board)

                        elif rect_counter and piece.color == "blank":
                            rect_counter = gui.second_click(game_board, rect_counter, piece, player_turn, from_piece)
                            if not rect_counter:
                                player_turn = 'white'

        gui.draw_pieces(game_board.board)


#TODO Kings move
#winnig  ->end game/another one
#Welome - names
