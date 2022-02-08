import pygame, sys, os
from pygame import Color, Surface
from pygame.locals import *
from configuration import screen, SQUARE_DIMENSION,background_img, SQUARE_COLOR,BRIGHT_SQUARE_COLOR
import board
import piece
import player

# initializes pygame
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()


class Game():
    def __init__(self):
        self.welcome_menu()

    def welcome_menu(self):
        run = True
        screen.blit(background_img, (0, 0))
        font = pygame.font.Font('freesansbold.ttf', 32)

        while run:

            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                    run = False

                if 400 + 100 > mouse[0] > 400 and 275 + 50 > mouse[1] > 275:
                    pygame.draw.rect(screen, BRIGHT_SQUARE_COLOR, (400, 275, 100, 50))

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.game_loop(self)
                else:
                    pygame.draw.rect(screen, SQUARE_COLOR, (400, 275, 100, 50))

                screen.blit(font.render("Checkers", True, (255, 255, 255)), (325, 50))
                screen.blit(font.render("Play", True, (0, 0, 0)), (417, 285))

            pygame.display.flip()




    def end_game(self):
        pass

    def game_loop(self):

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
                                rect_counter = gui.second_click(game_board, rect_counter, piece, player_turn,
                                                                from_piece)
                                if not rect_counter:
                                    player_turn = 'dark'

                        elif player_turn == "dark":
                            if piece.color == player_turn:
                                from_piece, rect_counter = gui.draw_rect(rect, piece, rect_counter, game_board)

                            elif rect_counter and piece.color == "blank":
                                rect_counter = gui.second_click(game_board, rect_counter, piece, player_turn,
                                                                from_piece)
                                if not rect_counter:
                                    player_turn = 'white'

            gui.draw_pieces(game_board.board)


# Welome - names
# winnig  ->end game/another one
test = Game
test.welcome_menu(test)