import pygame
from .piece import Piece
from ..utils.utilities import load_image

class Rook(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
    
    def get_coordinates(self) -> list:
        return [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def load_piece_image(self) -> tuple[pygame.Surface, pygame.Rect]:
        if self.color == "white":
            return load_image("wR.png")
        else:
            return load_image("bR.png")

