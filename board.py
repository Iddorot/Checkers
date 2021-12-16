import pygame, sys, os
import numpy as np
from pygame.locals import *
import configuration
from configuration import SQUARE_DIMENSION, BOARD_ROWS, BOARD_COLS, SQUARE_COLOR, screen, WHITE, DARK, background_img
from piece import Piece


class Board:
    def __init__(self):
        self.board = []
        self.dark_left = 12
        self.white_left = 12
        self.dark_kings = 0
        self.white_kings = 0
        self.create_board()
        self.get_square_under_mouse()

    def create_board(self):
        for row in range(BOARD_ROWS):
            self.board.append([])
            for col in range(BOARD_COLS):
                if col % 2 == ((row + 1) % 2):

                    if row < 3:
                        self.board[row].append(Piece(row, col, "white"))

                    elif row > 4:
                        self.board[row].append(Piece(row, col, "dark"))
                    else:
                        self.board[row].append(Piece(row, col, "blank"))
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

    def get_square_under_mouse(self):
        mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
        x, y = [int(v // SQUARE_DIMENSION) for v in mouse_pos]
        try:
            if x >= 0 and y >= 0:
                return self.board[y][x], x, y
        except IndexError:
            return "IndexError"
        return None, None, None

    def clean_screen(self):
        screen.blit(background_img, (0, 0))

    def make_move(self, from_point,to_point):
            self.board[to_point]=from_point.piece
            self.board[from_point]=empty
            self.board[to_point] = from_point.piece.change_pos(...)







