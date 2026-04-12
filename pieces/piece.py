# piece.py is an interface class
import pygame
from abc import ABC, abstractmethod
from ..gui.config import SQUARE_SIZE, OFFSET
from ..engine.rules import check_for_blocked 

class Piece(pygame.sprite.Sprite, ABC):
    def __init__(self, color):
        super().__init__()
        self.color = color
        self.image, self.rect = self.load_piece_image()
        self.pos_x = self.pos_y = 0
        self.max_step = 7
        self.move_count = 1

    def draw(self, screen):
       screen.blit(self.image, self.rect)

    def set_position(self, position):
        self.rect.topleft = position
        self.pos_x, self.pos_y = position
    
    @abstractmethod
    def update(self):
        pass
    
    @abstractmethod
    def get_coordinates(self) -> list:
        pass

    def generate_directional_moves(self) -> list:
        current_x = int((self.pos_x - OFFSET) / SQUARE_SIZE)
        current_y = int((self.pos_y - OFFSET) / SQUARE_SIZE)
        
        possible_moves = []

        for x, y in self.get_coordinates():
            distance = 0
            while distance < self.max_step:
                new_x = ((distance + 1) * x) + current_x
                new_y = ((distance + 1) * y) + current_y

                if ((new_x < 0 or new_x > 7) or
                    (new_y < 0 or new_y > 7)):
                    break
                
                possible_moves.append((new_x, new_y))

                distance += 1

        return possible_moves

    def on_move(self, position, board):
        old_position = (self.pos_x, self.pos_y)
        positions = self.generate_directional_moves()

        # TODO: 
        # this checks for blocked pieces and for possible takes 
        # make sure that before you move is it is valid square

        for x, y in positions:
            rect = pygame.Rect((x * SQUARE_SIZE) + OFFSET,
                               (y * SQUARE_SIZE) + OFFSET,
                               SQUARE_SIZE,
                               SQUARE_SIZE)

            if rect.collidepoint(position):
                self.move_count += 1
                self.set_position((rect.x, rect.y))
                return
        # if move is invalid, set to old position
        self.set_position(old_position) 
    
    @abstractmethod
    def available_takes(self):
        pass
        
    @abstractmethod
    def load_piece_image(self):
        pass
