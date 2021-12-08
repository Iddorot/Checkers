import pygame, sys, os
import numpy as np
from pygame.locals import *
import configuration
import board
from configuration import SQUARE_DIMENSION, screen


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
        screen.blit(self.color, (self.x, self.y))

    def __repr__(self):
        return str(self.color)
