# Import standard modules.
import sys
 
# Import non-standard modules.
import pygame as pg
from pygame.locals import *

def update(dt, settings, grid):
    """Update game. Called once per frame."""
  
    # Go through events that are passed to the script by the window.
    for event in pg.event.get():
        # We need to handle these events. Initially the only one you'll want to care
        # about is the QUIT event, because if you don't handle it, your game will crash
        # whenever someone tries to exit.
        if event.type == QUIT:
            pg.quit() # Opposite of pygame.init
            sys.exit() # Not including this line crashes the script on Windows. Possibly
            # on other operating systems too, but I don't know for sure.

    (x, y) = pg.mouse.get_pos()
    row, col = int(y / settings.squareSize), int(x / settings.squareSize)
    index = getIndex(settings, row, col)
    grid[index].visit(settings)

    
def draw(screen, settings, grid):
    """Draw things to the window. Called once per frame."""
    screen.fill(settings.bgColor) # Fill the screen with black.
  
    # Redraw screen here.
    for square in grid:
        # square.draw(screen)


        # """Draws the square to the screen"""
        rect = square.rect
        borders = square.borders
        borderThickness = 2
        
        topLeft = (rect.left, rect.top)
        topRight = (rect.right, rect.top)
        bottomLeft = (rect.left, rect.bottom)
        bottomRight = (rect.right, rect.bottom)
        
        if square.visited:
            fill = settings.squareFillVisited
        else:
            fill = settings.squareFillUnvisited
        pg.draw.rect(screen, fill, rect, 0)

        if borders['top']:
            pg.draw.line(screen, settings.borderColor, topLeft, topRight, borderThickness)
        if borders['bottom']:
            pg.draw.line(screen, settings.borderColor, bottomLeft, bottomRight, borderThickness)
        if borders['left']:
            pg.draw.line(screen, settings.borderColor, topLeft, bottomLeft, borderThickness)
        if borders['right']:
            pg.draw.line(screen, settings.borderColor, topRight, bottomRight, borderThickness)
  
    # Flip the display so that the things we drew actually show up.
    pg.display.flip()

def getIndex(settings, row, col):
    """Returns the index within the grid of the square at row, col"""
    return row * settings.numCols + col
