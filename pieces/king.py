from .piece import Piece
from ..utils.utilities import load_image
import pygame

class King(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def available_moves(self):
        pass

    def available_takes(self):
        pass

    def load_piece_image(self):
        if self.color == "white":
            return load_image("wK.png")
        else:
            return load_image("bK.png")

