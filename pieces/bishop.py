from .piece import Piece
from ..utils.utilities import load_image

class Bishop(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
    
    def update(self):
        pass

    def get_coordinates(self) -> list:
        return [(1, 1), (1, -1), (-1, 1), (-1, -1)]

    def available_takes(self):
        pass

    def load_piece_image(self):
        if self.color == "white":
            return load_image("wB.png")
        else:
            return load_image("bB.png")

