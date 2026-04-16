import pygame
from .piece import Piece
from ..utils.utilities import load_image

class King(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.max_step = 1

    def get_coordinates(self) -> list:
        return [(1, 0), (-1, 0), (0, 1), (0, -1),
                (1, 1), (1, -1), (-1, 1), (-1, -1)]

    def get_castling_move(self, direction: str):
        if self.has_move():
            return
        
        if direction == "right":
            return (self.file + 2, self.rank)
        elif direction == "left":
            return (self.file - 2, self.rank)
        return

    def load_piece_image(self) -> tuple[pygame.Surface, pygame.Rect]:
        if self.color == "white":
            return load_image("wK.png")
        else:
            return load_image("bK.png")

