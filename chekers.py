import pygame, sys, os
from pygame import Color, Surface
from pygame.locals import *
from configuration import screen, SQUARE_DIMENSION, background_img, SQUARE_COLOR, BRIGHT_SQUARE_COLOR, HEIGHT, WIDTH, \
    TEXT_SIZE,FONT
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
        font = pygame.font.Font(FONT,TEXT_SIZE)
        game_board = board.Board()
        screen.blit(background_img, (0, 0))

        while run:

            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                    run = False

                if (WIDTH / 2 + 125 > mouse[0] > 300) and HEIGHT / 2 + 50 > mouse[1] > HEIGHT / 2 - 50:
                    pygame.draw.rect(screen, BRIGHT_SQUARE_COLOR, (WIDTH / 2 - 100, HEIGHT / 2 - 50, 220, 110))

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        gui = player.Player()
                        gui.clean_screen(game_board)
                        self.game_loop(self)

                else:
                     pygame.draw.rect(screen, SQUARE_COLOR, (WIDTH / 2 - 100, HEIGHT / 2 - 50, 220, 110))

                screen.blit(font.render("Checkers", True, (255, 255, 255)), (WIDTH / 4 - 25, 50))
                screen.blit(font.render("Play", True, (0, 0, 0)), (WIDTH / 2 - 100, HEIGHT / 2 - 50))

            pygame.display.flip()

    def end_game(self):
        run = True
        font = pygame.font.Font(FONT, TEXT_SIZE)
        game_board = board.Board()
        screen.blit(background_img, (0, 0))
        exit_rect = (WIDTH / 2 - 100, HEIGHT / 2 - 50, 200, 100)
        restart_rect = (WIDTH / 2 - 175, HEIGHT / 2 + 150, 350, 110)
        while run:

            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                    run = False

                if (300 < mouse[0] < WIDTH / 2 + 125) and HEIGHT / 2 - 50 < mouse[1] < HEIGHT / 2 + 50:
                    pygame.draw.rect(screen, BRIGHT_SQUARE_COLOR, exit_rect)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        exit()

                elif 225 < mouse[0] < 575 and 550 < mouse[1] < 650:
                    pygame.draw.rect(screen, BRIGHT_SQUARE_COLOR, restart_rect)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        gui = player.Player()
                        gui.clean_screen(game_board)
                        self.game_loop(self)

                else:
                    pygame.draw.rect(screen, SQUARE_COLOR, exit_rect)
                    pygame.draw.rect(screen, SQUARE_COLOR, restart_rect)

                screen.blit(font.render("Checkers", True, (SQUARE_COLOR)), (WIDTH / 4 - 20, 55))
                screen.blit(font.render("Checkers", True, (255, 255, 255)), (WIDTH / 4 - 25, 50))
                screen.blit(font.render("Exit", True, (0, 0, 0)), (WIDTH / 2 - 100, HEIGHT / 2 - 50))
                screen.blit(font.render("Restart", True, (0, 0, 0)), (WIDTH / 2 - 175, HEIGHT / 2 + 150))

            pygame.display.flip()

    def game_loop(self):

        clock = pygame.time.Clock()
        game_board = board.Board()
        gui = player.Player()
        rect_counter = False
        player_turn = 'white'
        game_over = False
        # --------
        # MAINLOOP
        # --------

        while not game_over:

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
                                    if gui.check_win(game_board) is not None:
                                        game_over = True
                                        sys.exit()
                                        self.end_game(self)
                                    else:
                                        player_turn = 'dark'

                        elif player_turn == "dark":
                            if piece.color == player_turn:
                                from_piece, rect_counter = gui.draw_rect(rect, piece, rect_counter, game_board)

                            elif rect_counter and piece.color == "blank":
                                rect_counter = gui.second_click(game_board, rect_counter, piece, player_turn,
                                                                from_piece)
                                if not rect_counter:
                                    if gui.check_win(game_board) is not None:
                                        game_over = True
                                        sys.exit()
                                        self.end_game(self)
                                    else:
                                        player_turn = 'white'

            gui.draw_pieces(game_board.board)


# Welome - names
# winnig  ->end game/another one
test = Game
test.welcome_menu(test)
