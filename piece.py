
from configuration import SQUARE_DIMENSION, screen, WHITE, DARK, WHITE_KING, DARK_KING


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
        if self.row == 7 and self.color == "white":
            self.king = True
        elif self.row == 0 and self.color == "dark":
            self.king = True

    def draw(self, screen):
        if self.color == "white":
            if self.king:
                screen.blit(WHITE, (self.x, self.y))
                screen.blit(WHITE_KING, (self.x + (SQUARE_DIMENSION / 4), self.y + (SQUARE_DIMENSION / 4)))
            else:
                screen.blit(WHITE, (self.x, self.y))

        if self.color == "dark":
            if self.king:
                screen.blit(DARK, (self.x, self.y))
                screen.blit(DARK_KING, (self.x + (SQUARE_DIMENSION / 4), self.y + (SQUARE_DIMENSION / 4)))
            else:
                screen.blit(DARK, (self.x, self.y))



    def __repr__(self):
        return str(self.color)
