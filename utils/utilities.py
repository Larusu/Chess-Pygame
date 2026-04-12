import pygame
from ..gui.config import SQUARE_SIZE 
from pathlib import Path

assets_dir = Path(__file__).parent.parent.absolute() / "assets"

def load_image(file, scale=1):
    image_file = assets_dir.joinpath("images", file)
    image = pygame.image.load(image_file).convert_alpha()

    size = (int(SQUARE_SIZE), int(SQUARE_SIZE))

    image = pygame.transform.scale(image, size)

    return image, image.get_rect()

def get_font_path(file):
    return assets_dir.joinpath("font", file)
