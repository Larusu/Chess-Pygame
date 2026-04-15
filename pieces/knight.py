import pygame
from .piece import Piece
from ..utils.utilities import load_image

class Knight(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.max_step = 1

    def update(self):
        pass   
    
    def get_coordinates(self) -> list:
        return [( 1,  2),
                (-1,  2),
                ( 2,  1),
                ( 2, -1),
                ( 1, -2),
                (-1, -2),
                (-2,  1),
                (-2, -1)]

    def available_takes(self):
        pass

    def load_piece_image(self) -> tuple[pygame.Surface, pygame.Rect]:
        if self.color == "white":
            return load_image("wN.png")
        else:
            return load_image("bN.png")

