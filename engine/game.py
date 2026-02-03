import pygame
from .board import boardSurface

MAXHEIGHT = 700
MAXWIDTH = 850
BACKGROUNDCOLOR = (48, 46, 43)

def run():
    pygame.init()
    screen = pygame.display.set_mode((MAXWIDTH, MAXHEIGHT), pygame.SCALED)
    pygame.display.set_caption("Chess")
    pygame.mouse.set_visible(True)

    background = pygame.Surface(screen.get_size()).convert()
    background.fill(BACKGROUNDCOLOR)
    
    screen.blit(background, (0, 0))
    pygame.display.flip()

    clock = pygame.Clock()
    running = True

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        screen.blit(background, (0, 0))
        screen.blit(boardSurface(squareSize = 50), (10, 10))
        pygame.display.flip()

    pygame.quit()