import pygame, sys, os
from pygame.locals import *
from configuration import SQUARE_DIMENSION, BOARD_ROWS, BOARD_COLS, SQUARE_COLOR, screen, WHITE, DARK, background_img
from piece import Piece
import board
from board import Board


class Player:
    def __init__(self):
        self.dark_left = 12
        self.white_left = 12
        self.dark_kings = 0
        self.white_kings = 0

    def draw_pieces(self, board):

        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                piece = board[row][col]
                if piece != 0:
                    piece.draw(screen)

    def get_square_under_mouse(self, board):
        mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
        x, y = [int(v // SQUARE_DIMENSION) for v in mouse_pos]
        try:
            if x >= 0 and y >= 0:
                return board[y][x], x, y
        except IndexError:
            return "IndexError"
        return None, None, None

    def clean_screen(self):
        screen.blit(background_img, (0, 0))

    def make_move(self, board, from_point, to_point):
        (from_piece, from_x, from_y) = from_point
        (to_piece, to_x, to_y) = to_point
        board[to_y][to_x] = from_piece
        from_piece.row = to_y
        from_piece.col = to_x
        from_piece.calc_pos()
        board[from_y][from_x] = to_piece
        to_piece.row = from_y
        to_piece.col = from_x
        to_piece.calc_pos()

    def check_valid_move(self, from_point, to_point):
        (from_piece, from_x, from_y) = from_point
        (to_piece, to_x, to_y) = to_point

        if from_piece == "white" and to_y == from_y + 1 and (from_x == to_x + 1 or from_x == to_x - 1) and from_piece:
            return True

        if from_piece == "dark" and to_y == from_y - 1 and (from_x == to_x + 1 or from_x == to_x - 1):
            return True
