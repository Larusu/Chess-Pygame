from .piece import Piece
from ..utils.utilities import load_image
import pygame

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)

    def set_position(self, position):
        self.rect.topleft = position

    def available_moves(self):
        pass

    def available_takes(self):
        pass

    def load_piece_image(self):
        if self.color == "white":
            return load_image("wQ.png")
        else:
            return load_image("bQ.png")

