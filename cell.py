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
        # self.fillColor = settings.cellFillUnvisited
        # self.borderColors = {'top': settings.borderColor , 
        #                 'bottom' : settings.borderColor , 
        #                 'left' : settings.borderColor , 
        #                 'right' : settings.borderColor}
        self.rect = pg.Rect(self.col * self.size, self.row * self.size, self.size, self.size)

    # def draw(self, screen):
    #     """Draws the cell to the screen"""
    #     rect = self.rect
    #     borderColors = self.borderColors
    #     borders = self.borders
    #     borderThickness = 2
        
    #     topLeft = (rect.left, rect.top)
    #     topRight = (rect.right, rect.top)
    #     bottomLeft = (rect.left, rect.bottom)
    #     bottomRight = (rect.right, rect.bottom)
        
    #     pg.draw.rect(screen, self.fillColor, rect, 0)
    #     if borders['top']:
    #         pg.draw.line(screen, borderColors['top'], topLeft, topRight, borderThickness)
    #     if borders['bottom']:
    #         pg.draw.line(screen, borderColors['bottom'], bottomLeft, bottomRight, borderThickness)
    #     if borders['left']:
    #         pg.draw.line(screen, borderColors['left'], topLeft, bottomLeft, borderThickness)
    #     if borders['right']:
    #         pg.draw.line(screen, borderColors['right'], topRight, bottomRight, borderThickness)

    # def visit(self, settings):
    #     """Updates cell settings once visited"""
    #     self.visited = True
    #     self.fillColor = settings.cellFillVisited