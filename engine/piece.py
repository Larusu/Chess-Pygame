import pygame
from ..utils.utilities import loadImage

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
        self.image, self.rect = loadImage("wP.png") if (white) else loadImage("bP.png")
        self.rect.x = x
        self.rect.y = y
