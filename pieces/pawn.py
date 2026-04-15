import pygame
from .piece import Piece
from ..utils.utilities import load_image

class Pawn(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.max_step = 1
    
    def update(self):
        pass   
    
    def get_coordinates(self) -> list:
        # first move
        if not self.has_move():
            if self.color == "white":
                return [(0, -1), (1, -1), 
                        (-1, -1), (0, -2)]
            else:
                return [(0, 1), (1, 1),
                        (-1, 1), (0, 2)]
        # second, third, ...nth, move
        else:
            if self.color == "white":
                return [(0, -1), (1, -1), (-1, -1)]
            else:
                return [(0, 1), (1, 1), (-1, 1)]

    def available_takes(self):
        pass

    def load_piece_image(self) -> tuple[pygame.Surface, pygame.Rect]:
        if self.color == "white":
            return load_image("wP.png")
        else:
            return load_image("bP.png")

