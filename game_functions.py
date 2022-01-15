# Import standard modules.
import sys
import random as rand

 
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

    # While the stack is not empty
    if grid.stack:
        # Pop a cell from the stack and make it a current cell
        grid.currentCell = grid.stack.pop()
        (row, col) = grid.currentCell
        numRows = settings.numRows
        numCols = settings.numCols
        index = getIndex(row, col, numRows, numCols)

        options = []
        up = getIndex(row - 1, col, numRows, numCols)
        down = getIndex(row + 1, col, numRows, numCols)
        left = getIndex(row, col - 1, numRows, numCols)
        right = getIndex(row, col + 1, numRows, numCols)

        if up and not grid.cells[up].visited:
            options.append(up)
        if down and not grid.cells[down].visited:
            options.append(down)
        if left and not grid.cells[left].visited:
            options.append(left)
        if right and not grid.cells[right].visited:
            options.append(right)
        
        # If the current cell has any neighbours which have not been visited 
        if len(options) >= 1:

            # Push the current cell to the stack
            grid.stack.append(grid.currentCell)
            
            # Choose one of the unvisited neighbours
            newIndex = options[rand.randint(0, len(options) - 1)]

            # Remove the wall between the current cell and the chosen cell
            if newIndex == down:
                grid.cells[index].borders['bottom'] = False
                grid.cells[newIndex].borders['top'] = False
            elif newIndex == up:
                grid.cells[index].borders['top'] = False
                grid.cells[newIndex].borders['bottom'] = False
            elif newIndex == right:
                grid.cells[index].borders['right'] = False
                grid.cells[newIndex].borders['left'] = False
            elif newIndex == left:
                grid.cells[index].borders['left'] = False
                grid.cells[newIndex].borders['right'] = False

            # Mark the chosen cell as visited and push it to the stack
            grid.cells[newIndex].visited = True
            grid.stack.append(getCoordinates(grid, newIndex, numCols))

    
def draw(screen, settings, grid):
    """Draw things to the window. Called once per frame."""
    screen.fill(settings.bgColor) # Fill the screen with black.
  
    # Redraw screen here.
    for cell in grid.cells:

        # """Draws the cell to the screen"""
        rect = cell.rect
        borders = cell.borders
        borderThickness = settings.borderThickness
        borderColor = settings.borderColor
        
        # Draw cell
        ################################################################
        # Current cell is showing up as green before red. Need to dig into it
        ################################################################
        if (cell.row, cell.col) == grid.currentCell:
            fill = settings.cellFillCurrent
        elif (cell.row, cell.col) in grid.stack:
            fill = settings.cellFillStack
        elif cell.visited:
            fill = settings.cellFillVisited
        else:
            fill = settings.cellFillUnvisited
        pg.draw.rect(screen, fill, rect, 0)

    ####################################################################
    # For lines to look good, need to draw rects first
    # then draw borders. Need to find a way to draw on 
    # different 'layers'. Sprite groups maybe? Want to remove
    # this second loop below
    ####################################################################
    for cell in grid.cells:
        rect = cell.rect
        borders = cell.borders
        borderThickness = settings.borderThickness
        borderColor = settings.borderColor
    ####################################################################

        # Draw borders
        if borders['top']:
            topLeft = (rect.left - int(borderThickness / 2) + 1, rect.top)
            topRight = (rect.right + int(borderThickness / 2), rect.top)
            pg.draw.line(screen, borderColor, topLeft, topRight, borderThickness)
            # pg.draw.line(screen, (255, 255, 255), topLeft, topRight)
        if borders['bottom']:
            ####################################################################
            # Not showing up at bottom edge of screen. Need to check coordinates
            ####################################################################
            bottomLeft = (rect.left - int(borderThickness / 2) + 1, rect.bottom)
            bottomRight = (rect.right + int(borderThickness / 2), rect.bottom)
            # pg.draw.line(screen, borderColor, bottomLeft, bottomRight, borderThickness)
            pg.draw.line(screen, (255, 255, 255), bottomLeft, bottomRight)
        if borders['left']:
            topLeft = (rect.left, rect.top - int(borderThickness / 2) + 1)
            bottomLeft = (rect.left, rect.bottom + int(borderThickness / 2))
            pg.draw.line(screen, borderColor, topLeft, bottomLeft, borderThickness)
            # pg.draw.line(screen, (255, 255, 255), topLeft, bottomLeft)
        if borders['right']:
            ####################################################################
            # Not showing up at right edge of screen. Need to check coordinates
            #################################################################### 
            topRight = (rect.right, rect.top - int(borderThickness / 2) + 1)
            bottomRight = (rect.right, rect.bottom + int(borderThickness / 2))
            # pg.draw.line(screen, borderColor, topRight, bottomRight, borderThickness)
            pg.draw.line(screen, (255, 255, 255), topRight, bottomRight)
  
    # Flip the display so that the things we drew actually show up.
    pg.display.flip()

def getIndex(row, col, numRows, numCols):
    """Returns the index within the grid of the cell at row, col"""
    if row < 0 or col < 0 or row >= numRows or col >= numCols: return False
    return row * numCols + col

def getCoordinates(grid, index, numCols):
    """Returns the coordinates of a cell within the grid for a given index"""
    if index < 0 or index >= len(grid.cells): return False
    row = int(index / numCols)
    col = index % numCols
    return (row, col)
