import pygame as pg
import game_functions as gf


class Cell():
    """A class to represent the grid cells within the maze"""

    def __init__(self, settings, row, col):
        """Initialize the cell's settings"""
        self.size = settings.cellSize
        self.row = row
        self.col = col
        self.index = gf.getIndex(row, col, settings.numRows, settings.numCols)
        self.visited = False
        self.neighbors = self.getNeighbors(settings)
        self.borders = {
            'top': True,
            'bottom': True,
            'left': True,
            'right': True
        }
        self.rect = pg.Rect(
            self.col * self.size + int(settings.borderThickness / 2),
            self.row * self.size + int(settings.borderThickness / 2),
            self.size, self.size)

    def getNeighbors(self, settings):
        """Returns a dictionary containing the indices of the neighboring cells.
        Neighbors which fall beyond the grid edge evaluate as None"""
        neighbors = {}
        neighbors['top'] = gf.getIndex(self.row - 1, self.col,
                                       settings.numRows, settings.numCols)
        neighbors['bottom'] = gf.getIndex(self.row + 1, self.col,
                                          settings.numRows, settings.numCols)
        neighbors['left'] = gf.getIndex(self.row, self.col - 1,
                                        settings.numRows, settings.numCols)
        neighbors['right'] = gf.getIndex(self.row, self.col + 1,
                                         settings.numRows, settings.numCols)
        return neighbors
