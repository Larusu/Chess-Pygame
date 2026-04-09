# piece.py is an interface class
from abc import ABC, abstractmethod
import pygame

class Piece(pygame.sprite.Sprite, ABC):
    def __init__(self, color):
        super().__init__()
        self.color = color
        self.image, self.rect = self.load_piece_image()

    def draw(self, screen):
       screen.blit(self.image, self.rect)

    def set_position(self, position):
        self.rect.topleft = position
    
    @abstractmethod
    def update(self):
        pass
    
    @abstractmethod
    def available_moves(self):
        pass

    @abstractmethod
    def available_takes(self):
        pass

    @abstractmethod
    def load_piece_image(self):
        pass
