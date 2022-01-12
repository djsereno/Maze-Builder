# Maze Builder

# Import standard modules.
import sys

# Import non-standard modules.
import pygame as pg
from pygame.locals import *
from square import Square
import game_functions as gf
from settings import Settings


def runPyGame():
    # Initialise PyGame.
    pg.init()

    # Set up the clock. This will tick every frame and thus maintain a relatively constant framerate. Hopefully.
    fps = 60.0
    fpsClock = pg.time.Clock()

    # Create settings
    settings = Settings()

    # Set up the window.
    width, height = settings.screenWidth, settings.screenHeight
    screen = pg.display.set_mode((width, height))
    pg.display.set_caption("Maze Builder")

    # screen is the surface representing the window.
    # PyGame surfaces can be thought of as screen sections that you can draw onto.
    # You can also draw surfaces onto other surfaces, rotate surfaces, and transform surfaces.

    # Initialize grid
    grid = []
    for row in range(settings.numRows):
        for col in range(settings.numCols):
            square = Square(settings, row, col)
            grid.append(square)

    # Main game loop.
    dt = 1/fps # dt is the time since last frame.
    while True: # Loop forever!
        gf.update(dt, settings, grid) # You can update/draw here, I've just moved the code for neatness.
        gf.draw(screen, settings, grid)

        dt = fpsClock.tick(fps)

runPyGame()