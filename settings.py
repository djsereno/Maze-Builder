import game_functions as gf

class Settings():
    """A class to store game settings"""

    def __init__(self):
        """Initialize the game's static settings"""
        # Grid settings
        self.cellSize = 20
        self.numRows = 60
        self.numCols = 60
        self.startCell = gf.getIndex(0, 0, self.numRows, self.numCols)
        
        # Cell settings
        self.cellFillCurrent = (155, 41, 21)
        self.cellFillStack = (233, 180, 76)  
        self.cellFillUnvisited = (80, 162, 167)
        self.cellFillVisited = (228, 214, 167)
        self.borderColor = (28, 17, 10)
        # self.borderThickness = int(self.cellSize / 2)
        self.borderThickness = 2

        # Screen settings
        self.screenWidth = self.cellSize * self.numCols
        self.screenHeight = self.cellSize * self.numRows
        self.bgColor = (0, 0, 0)
        