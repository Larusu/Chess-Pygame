# piece.py is an interface class
import pygame
from abc import ABC, abstractmethod

class Piece(pygame.sprite.Sprite, ABC):
    def __init__(self, color, x, y):
        super().__init__()
        self.color = color
        self.image, self.rect = self.load_piece_image()
        self.file = x        # board x-position (0-7) = (a-h)
        self.rank = y        # board y-position (0-7) = (1-8)
        self.max_step = 7    # how long piece can move to board
        self.move_count = 0  # tracks piece movement

    def draw(self, screen):
       screen.blit(self.image, self.rect)

    def set_position(self, position):
        self.rect.topleft = position
    
    @abstractmethod
    def update(self):
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
        
    def move(self, new_position, new_file, new_rank):
        self.set_position(new_position)
        self.move_count += 1
        self.file, self.rank = new_file, new_rank

    def has_move(self) -> bool:
        return self.move_count > 0
     
    @abstractmethod
    def get_coordinates(self) -> list:
        pass   
    
    def get_board_position(self) -> tuple[int, int]:
        return (self.file, self.rank)

    def get_color(self):
        return self.color

    @abstractmethod
    def available_takes(self):
        pass
        
    @abstractmethod
    def load_piece_image(self) -> tuple[pygame.Surface, pygame.Rect]:
        pass
