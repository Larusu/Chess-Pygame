import pygame
from .board import board_surface
from ..config.config import BOARD_SIZE, BACKGROUND_COLOR

MAX_HEIGHT = BOARD_SIZE
MAX_WIDTH = BOARD_SIZE

def run():
    pygame.init()

    screen = pygame.display.set_mode(
        (MAX_WIDTH, MAX_HEIGHT),
        pygame.SCALED
    )

    pygame.display.set_caption("Chess")
    pygame.mouse.set_visible(True)

    background = pygame.Surface(screen.get_size()).convert()
    background.fill(BACKGROUND_COLOR)

    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Create board once
    board = board_surface()

    # w_pawn = Pawn(100, 100, True)
    # all_sprites = pygame.sprite.Group(w_pawn)

    clock = pygame.Clock()
    running = True

    while running:
        clock.tick(60)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif (
                event.type == pygame.KEYDOWN
                and event.key == pygame.K_ESCAPE
            ):
                running = False

        # all_sprites.update()

        screen.blit(background, (0, 0))
        screen.blit(board, (0, 0))
        # all_sprites.draw(screen)

        pygame.display.flip()

    pygame.quit()