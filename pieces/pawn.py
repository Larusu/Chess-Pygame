from .piece import Piece
from ..utils.utilities import load_image

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.max_step = 1
    
    def update(self):
        pass   
    
    def get_coordinates(self) -> list:
        if self.move_count > 1:
            if self.color == "white":
                return [(0, -1)]
            elif self.color == "black":
                return [(0, 1)]
        elif self.move_count == 1:
            if self.color == "white":
                return [(0, -1), (0, -2)]
            elif self.color == "black":
                return [(0, 1), (0, 2)]
        else: 
            return []

    def available_takes(self):
        pass

    def load_piece_image(self):
        if self.color == "white":
            return load_image("wP.png")
        else:
            return load_image("bP.png")

