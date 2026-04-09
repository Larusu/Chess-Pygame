from .piece import Piece
from ..utils.utilities import load_image
import pygame

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
    
    def update(self):
        pass

    def available_moves(self):
        pass

    def available_takes(self):
        pass

    def load_piece_image(self):
        if self.color == "white":
            return load_image("wR.png")
        else:
            return load_image("bR.png")

