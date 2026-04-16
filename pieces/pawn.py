import pygame
from .piece import Piece
from ..utils.utilities import load_image

class Pawn(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.max_step = 2
    
    def get_coordinates(self) -> list:
        if self.color == "white":
            return [(0, -1)]
        else:
            return [(0, 1)]

    def available_takes(self) -> list:
        takes = []
        coords = []

        if self.color == "white":
            coords = [(1, -1), (-1, -1)]
        elif self.color == "black":
            coords = [(1, 1), (-1, 1)]
        
        for x, y in coords:
            new_x = (1 * x) + self.file
            new_y = (1 * y) + self.rank
            
            if (new_x < 0 or new_x > 7) or (new_y < 0 or new_y > 7):
                break

            takes.append((new_x, new_y))

        return takes

    def move(self, new_position, new_file, new_rank):
        self.set_position(new_position)
        self.move_count += 1
        self.file, self.rank = new_file, new_rank
        self.max_step = 1 # move 1 square after moving

    def load_piece_image(self) -> tuple[pygame.Surface, pygame.Rect]:
        if self.color == "white":
            return load_image("wP.png")
        else:
            return load_image("bP.png")

