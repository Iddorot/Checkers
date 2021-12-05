import pygame, sys, os
import numpy as np
from pygame.locals import *
import configuration
from configuration import SQUARE_DIMENSION, BOARD_ROWS, BOARD_COLS, SQUARE_COLOR, screen, WHITE, DARK
from piece import Piece

class Board:
    def __init__(self):
        self.board = list()
        self.dark_left = 12
        self.white_left = 12
        self.dark_kings = 0
        self.white_kings = 0
        self.create_board()

    def create_board(self):
        for row in range(BOARD_ROWS):
            self.board.append([])
            for col in range(BOARD_COLS):
                if col % 2 == ((row + 1) % 2):

                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, DARK))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw_sqaures(self, screen):
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if col % 2 == ((row + 1) % 2):
                    pygame.draw.rect(screen, SQUARE_COLOR,
                                    pygame.Rect(row * SQUARE_DIMENSION, col * SQUARE_DIMENSION, SQUARE_DIMENSION,
                                                SQUARE_DIMENSION))

    def draw(self, screen):
        self.draw_sqaures(screen)
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(screen)


