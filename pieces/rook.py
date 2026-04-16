import pygame
from .piece import Piece
from ..utils.utilities import load_image
from ..gui.config import SQUARE_SIZE

class Rook(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
    
    def get_coordinates(self) -> list:
        return [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def move(self, new_position, new_file, new_rank):
        print(f"rook old file, rank: {self.file}, {self.rank}")
        self.file, self.rank = new_file, new_rank
        print(f"rook new file, rank: {self.file}, {self.rank}")
        
        if new_position == "king": 
            self.set_position((self.rect.x - (SQUARE_SIZE * 2), self.rect.y))
        elif new_position == "queen":
            self.set_position((self.rect.x + (SQUARE_SIZE * 3), self.rect.y))
        else:
            self.set_position(new_position)
            self.move_count += 1
            
    def load_piece_image(self) -> tuple[pygame.Surface, pygame.Rect]:
        if self.color == "white":
            return load_image("wR.png")
        else:
            return load_image("bR.png")

