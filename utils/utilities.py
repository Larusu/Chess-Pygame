import pygame
from pathlib import Path

assets_dir = Path(__file__).parent.parent.absolute() / "assets"


def load_image(file, scale=1):
    image_file = assets_dir.joinpath("images", file)
    image = pygame.image.load(image_file)

    width, height = image.get_size()
    size = (int(width * scale), int(height * scale))

    image = pygame.transform.scale(image, size)

    return image, image.get_rect()


def get_font_path(file):
    return assets_dir.joinpath("font", file)
