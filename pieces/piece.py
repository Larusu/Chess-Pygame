# piece.py is an interface class
import pygame
from abc import ABC, abstractmethod
from ..gui.config import SQUARE_SIZE, OFFSET

class Piece(pygame.sprite.Sprite, ABC):
    def __init__(self, color, x, y):
        super().__init__()
        self.color = color
        self.image, self.rect = self.load_piece_image()
        self.file = x        # board x-position (0-7) = (a-h)
        self.rank = y        # board y-position (0-7) = (1-8)
        self.max_step = 7    # how long piece can move to board
        self.move_count = 1  # tracks piece movement

    def draw(self, screen):
       screen.blit(self.image, self.rect)

    def set_position(self, position):
        self.rect.topleft = position
        self.current_x, self.current_y = position
    
    @abstractmethod
    def update(self):
        pass
    
    @abstractmethod
    def get_coordinates(self) -> list:
        pass

    def _handle_move_calculation(self, x, y) -> list:
        direction = []

        distance = 0
        while distance < self.max_step:
            new_x = ((distance + 1) * x) + self.file
            new_y = ((distance + 1) * y) + self.rank

            if (new_x < 0 or new_x > 7) or (new_y < 0 or new_y > 7):
                break
            
            direction.append((new_x, new_y))

            distance += 1

        return direction

    def generate_possible_moves(self) -> list:
        possible_moves = []

        for x, y in self.get_coordinates():
            direction = self._handle_move_calculation(x, y)
            possible_moves.append(direction)

        return possible_moves
        
    def move(self, new_pos):
        move_paths = self.generate_possible_moves()

        for direction in move_paths:
            for x, y in direction:
                rect = pygame.Rect((x * SQUARE_SIZE) + OFFSET,
                                   (y * SQUARE_SIZE) + OFFSET,
                                   SQUARE_SIZE,
                                   SQUARE_SIZE)

                if rect.collidepoint(new_pos):
                    self.move_count += 1
                    self.file, self.rank = x, y
                    self.set_position((rect.x, rect.y))
                    return

        # if move is invalid, set to old position
        self.set_position((self.current_x, self.current_y)) 
    
    def get_color(self):
        return self.color

    @abstractmethod
    def available_takes(self):
        pass
        
    @abstractmethod
    def load_piece_image(self):
        pass
