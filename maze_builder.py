# ==============
# MAZE BUILDER
# ==============
# Maze generator algorithm using iterative implementation and backtracking method.
# See 'Iterative Implementation' at https://en.wikipedia.org/wiki/Maze_generation_algorithm
# ==============
# Future updates or improvements:
# - Keep track of longest path and display once complete
# - Allow user to draw obstacles prior to maze generation
# - Allow user to define an end point

# Import standard modules.
import sys

# Import non-standard modules.
import pygame as pg
from pygame.locals import *
from cell import Cell
from grid import Grid
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

    # Initialize grid
    grid = Grid()
    for row in range(settings.numRows):
        for col in range(settings.numCols):
            cell = Cell(settings, row, col)
            grid.cells.append(cell)

    # Choose the initial cell, mark it as visited and push it to the stack
    grid.stack.append(grid.cells[settings.startCell])
    grid.currentPath.append(grid.cells[settings.startCell].index)

    # Main game loop.
    dt = 1 / fps  # dt is the time since last frame.
    while True:
        gf.checkEvents()

        if settings.animate:
            gf.update(grid)
        else:
            while grid.stack:
                gf.update(grid)

        gf.draw(screen, settings, grid)

        dt = fpsClock.tick(fps)


runPyGame()