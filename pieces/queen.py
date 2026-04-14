from .piece import Piece
from ..utils.utilities import load_image

class Queen(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
    
    def update(self):
        pass
    
    def get_coordinates(self) -> list:
        return [(1, 0), (-1, 0), (0, 1), (0, -1),
                (1, 1), (1, -1), (-1, 1), (-1, -1)]

    def available_takes(self):
        pass

    def load_piece_image(self):
        if self.color == "white":
            return load_image("wQ.png")
        else:
            return load_image("bQ.png")

