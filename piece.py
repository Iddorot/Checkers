
from configuration import SQUARE_DIMENSION, screen, WHITE, DARK


class Piece:

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_DIMENSION * self.col
        self.y = SQUARE_DIMENSION * self.row

    def make_king(self):
        self.king = True

    def draw(self, screen):
        if self.color == "white":
            screen.blit(WHITE, (self.x, self.y))
        if self.color == "dark":
            screen.blit(DARK, (self.x, self.y))

    def __repr__(self):
        return str(self.color)
