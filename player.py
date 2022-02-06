import pygame
from pygame.locals import *
from configuration import SQUARE_DIMENSION, BOARD_ROWS, BOARD_COLS, SQUARE_COLOR, screen, WHITE, DARK, background_img, \
    RED
from piece import Piece
import board
from board import Board


class Player:
    def __init__(self):

        self.white_kings = 0
        self.dark_kings = 0

    def draw_pieces(self, board):

        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                piece = board[row][col]
                if piece != 0:
                    piece.draw(screen)
        pygame.display.update()

    def get_square_under_mouse(self, board):
        mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
        x, y = [int(v // SQUARE_DIMENSION) for v in mouse_pos]
        try:
            if x >= 0 and y >= 0:
                return board[y][x], x, y
        except IndexError:
            return "IndexError"
        return None, None, None

    def clean_screen(self, board):
        screen.blit(background_img, (0, 0))
        board.draw_squares(screen)

    def move_one(self, board, from_piece, to_piece):

        board[to_piece.row][to_piece.col].color = from_piece.color
        board[from_piece.row][from_piece.col].color = "blank"
        self.draw_pieces(board)

    def eat(self, board, from_piece, to_piece):

        row_avg = (from_piece.row + to_piece.row) // 2
        col_avg = (from_piece.col + to_piece.col) // 2

        board[to_piece.row][to_piece.col].color = from_piece.color
        board[from_piece.row][from_piece.col].color = "blank"
        board[row_avg][col_avg].color = "blank"
        self.draw_pieces(board)

    def check_valid_move(self, board, from_piece, to_piece):

        col_check_one = (from_piece.col == to_piece.col + 1 or from_piece.col == to_piece.col - 1)
        col_check_two = (from_piece.col == to_piece.col + 2 or from_piece.col == to_piece.col - 2)
        row_avg = (from_piece.row + to_piece.row) // 2
        col_avg = (from_piece.col + to_piece.col) // 2

        if to_piece.color == "blank":

            if not from_piece.king:

                if from_piece.color == "white":

                    if to_piece.row == from_piece.row + 1 and col_check_one:
                        return "one"

                    elif to_piece.row == from_piece.row + 2 and col_check_two and board.board[row_avg][
                        col_avg].color == "dark":
                        return "eat"


                elif from_piece.color == "dark":
                    if to_piece.row == from_piece.row - 1 and col_check_one:
                        return "one"

                    elif to_piece.row == from_piece.row - 2 and col_check_two and board.board[row_avg][
                        col_avg].color == "white":
                        return "eat"


    def make_move(self, board, from_piece, to_piece, what_move):
        self.clean_screen(board)
        if what_move == "one":
            self.move_one(board.board, from_piece, to_piece)
            self.king(to_piece)

        elif what_move == "eat":
            board.reduce_piece(from_piece)
            self.eat(board.board, from_piece, to_piece)
            self.king(to_piece)

    def king(self, piece):
        if piece.row == 7 and piece.color == "white":
            piece.make_king()
        elif piece.row == 0 and piece.color == "dark":
            piece.make_king()

    def draw_rect(self, rect, piece, rect_counter, game_board):
        if not rect_counter:
            pygame.draw.rect(screen, RED, rect, 5)
            from_piece = piece
            rect_counter = True
            return from_piece, rect_counter
        elif rect_counter:
            self.clean_screen(game_board)
            pygame.draw.rect(screen, RED, rect, 5)
            from_piece = piece
            rect_counter = True
            return from_piece, rect_counter

    def second_click(self, game_board, rect_counter, piece, player_turn, from_piece):
        to_piece = piece
        what_move = self.check_valid_move(game_board, from_piece, to_piece)

        if what_move is not None:
            self.make_move(game_board, from_piece, to_piece, what_move)
            rect_counter = False
            return rect_counter
        else:
            rect_counter = True
            return rect_counter


