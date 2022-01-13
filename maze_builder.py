# Maze Builder

# Import standard modules.
import sys

# Import non-standard modules.
import pygame as pg
from pygame.locals import * 
from cell import Cell
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
    grid = {}
    grid['cells'] = []
    for row in range(settings.numRows):
        for col in range(settings.numCols):
            cell = Cell(settings, row, col)
            grid['cells'].append(cell)
    
    # Choose the initial cell, mark it as visited and push it to the stack
    grid['cells'][0].visited = True
    grid['stack'] = [(0, 0)]

    # Main game loop.
    dt = 1/fps # dt is the time since last frame.
    while True: # Loop forever!
        gf.update(dt, settings, grid) # You can update/draw here, I've just moved the code for neatness.
        gf.draw(screen, settings, grid)

        dt = fpsClock.tick(fps)

runPyGame()