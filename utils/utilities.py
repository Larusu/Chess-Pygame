import pygame
from pathlib import Path 

assetsDir = Path(__file__).parent.parent.absolute() / 'assets'

def loadImage(file, scale = 1):
    imageFile = assetsDir.joinpath("images", file)
    image = pygame.image.load(imageFile)

    size = image.get_size()
    size = (size[0] * scale, size[1] * scale)
    image = pygame.transform.scale(image, size)

    return image, image.get_rect()

def getFontPath(file):
    return assetsDir.joinpath("font", file)