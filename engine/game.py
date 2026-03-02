import pygame
from .board import boardSurface
from .piece import Pawn

MAXHEIGHT = 555
MAXWIDTH = 555
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

    wPawn = Pawn(100, 100, True)
    allSprites = pygame.sprite.Group((wPawn))

    clock = pygame.Clock()
    running = True

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        board = boardSurface(squareSize = 65)

        allSprites.update()

        screen.blit(background, (0, 0))
        screen.blit(board, (0, 0))
        allSprites.draw(screen)

        pygame.display.flip()

    pygame.quit()