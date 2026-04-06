import pygame
from ..utils.utilities import load_image

class Piece:
    def __init__():
        
        alive = True
    
    def move():
        pass

class Pawn(pygame.sprite.Sprite): 
    white : bool

    # next task is assign the x and y coordinates of the pieces
    def __init__(self, x, y, white = True):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("wP.png") if (white) else load_image("bP.png")
        self.rect.x = x
        self.rect.y = y
