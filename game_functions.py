# Import standard modules.
import sys
import random as rand

# Import non-standard modules.
import pygame as pg
from pygame.locals import *


def checkEvents():
    """Check for key events. Called once per frame."""

    # Go through events that are passed to the script by the window.
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()


def update(grid):
    """Update maze"""

    # While the stack is not empty
    if grid.stack:
        # Pop a cell from the stack and make it a current cell
        currentCell = grid.stack.pop()
        grid.currentCell = currentCell
        currentCell.visited = True

        # Find unvisited cell neighbors
        neighbors = []
        top = currentCell.neighbors['top']
        bottom = currentCell.neighbors['bottom']
        left = currentCell.neighbors['left']
        right = currentCell.neighbors['right']

        if top != None and not grid.cells[top].visited:
            neighbors.append(top)
        if bottom != None and not grid.cells[bottom].visited:
            neighbors.append(bottom)
        if left != None and not grid.cells[left].visited:
            neighbors.append(left)
        if right != None and not grid.cells[right].visited:
            neighbors.append(right)

        # If the current cell has any neighbours which have not been visited
        if neighbors:

            # Push the current cell to the stack
            grid.stack.append(currentCell)

            # Choose one of the unvisited neighbours
            newIndex = neighbors[rand.randint(0, len(neighbors) - 1)]
            nextCell = grid.cells[newIndex]

            # Remove the wall between the current cell and the chosen cell
            if newIndex == bottom:
                currentCell.borders['bottom'] = False
                nextCell.borders['top'] = False
            elif newIndex == top:
                currentCell.borders['top'] = False
                nextCell.borders['bottom'] = False
            elif newIndex == right:
                currentCell.borders['right'] = False
                nextCell.borders['left'] = False
            elif newIndex == left:
                currentCell.borders['left'] = False
                nextCell.borders['right'] = False

            # Push nextCell to the stack
            grid.stack.append(nextCell)


def draw(screen, settings, grid):
    """Draw things to the window. Called once per frame."""
    screen.fill(settings.bgColor)

    # Redraw screen here.
    for cell in grid.cells:

        rect = cell.rect
        borders = cell.borders
        borderThickness = settings.borderThickness
        borderColor = settings.borderColor

        # Draw cell
        if cell is grid.currentCell:
            fill = settings.cellFillCurrent
        elif cell.visited:
            if cell in grid.stack:
                fill = settings.cellFillStack
            else:
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
            pg.draw.line(screen, borderColor, topLeft, topRight,
                         borderThickness)
        if borders['bottom']:
            bottomLeft = (rect.left - int(borderThickness / 2) + 1,
                          rect.bottom)
            bottomRight = (rect.right + int(borderThickness / 2), rect.bottom)
            pg.draw.line(screen, borderColor, bottomLeft, bottomRight,
                         borderThickness)
        if borders['left']:
            topLeft = (rect.left, rect.top - int(borderThickness / 2) + 1)
            bottomLeft = (rect.left, rect.bottom + int(borderThickness / 2))
            pg.draw.line(screen, borderColor, topLeft, bottomLeft,
                         borderThickness)
        if borders['right']:
            topRight = (rect.right, rect.top - int(borderThickness / 2) + 1)
            bottomRight = (rect.right, rect.bottom + int(borderThickness / 2))
            pg.draw.line(screen, borderColor, topRight, bottomRight,
                         borderThickness)

    pg.display.flip()


def getIndex(row, col, numRows, numCols):
    """Returns the index within the grid of the cell at row, col"""
    if row < 0 or col < 0 or row >= numRows or col >= numCols: return None
    return row * numCols + col


def getCoordinates(grid, index, numCols):
    """Returns the coordinates of a cell within the grid for a given index"""
    if index < 0 or index >= len(grid.cells): return False
    row = int(index / numCols)
    col = index % numCols
    return (row, col)