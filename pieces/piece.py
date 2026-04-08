# piece.py is an interface class
from abc import ABC, abstractmethod
import pygame

class Piece(pygame.sprite.Sprite, ABC):
    def __init__(self, color, position):
        super().__init__()
        self.color = color
        self.position = position
        # self.image, self.rect = self.load_piece_image()
        # self.rect.topleft = position

    @abstractmethod
    def available_moves(self):
        pass

    @abstractmethod
    def available_takes(self):
        pass

    @abstractmethod
    def load_piece_image(self):
        pass
