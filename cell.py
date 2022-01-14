import pygame as pg
import random

class Cell():
    """A class to represent the grid cells within the maze"""

    def __init__(self, settings, row, col):
        """Initialize the cell's settings"""
        self.size = settings.cellSize
        self.row = row
        self.col = col
        self.visited = False
        self.borders = {'top': True , 
                        'bottom' : True , 
                        'left' : True , 
                        'right' : True}
        self.rect = pg.Rect(self.col * self.size, self.row * self.size, self.size, self.size)