import pygame
from pygame.locals import *
from configuration import SQUARE_DIMENSION, BOARD_ROWS, BOARD_COLS, SQUARE_COLOR, screen, WHITE, DARK, background_img
from piece import Piece



class Board:
    def __init__(self):
        self.dark_left = 0
        self.white_left = 0
        self.board = []
        self.create_board()
        self.draw_squares(screen)



    def create_board(self):
        for row in range(BOARD_ROWS):
            self.board.append([])
            for col in range(BOARD_COLS):
                if col % 2 == ((row + 1) % 2):

                    if row < 3:
                        self.board[row].append(Piece(row, col, "white"))
                        self.white_left += 1
                    elif row > 4:
                        self.board[row].append(Piece(row, col, "dark"))
                        self.dark_left += 1


                    else:
                        self.board[row].append(Piece(row, col, "blank"))
                else:
                    self.board[row].append(0)


    def draw_squares(self, screen):
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if col % 2 == ((row + 1) % 2):
                    pygame.draw.rect(screen, SQUARE_COLOR,
                                     pygame.Rect(row * SQUARE_DIMENSION, col * SQUARE_DIMENSION, SQUARE_DIMENSION,
                                                 SQUARE_DIMENSION))

    def reduce_piece(self, piece):
        if piece.color == "white":
            self.dark_left -= 1
        elif piece.color == "dark":
            self.white_left -= 1
