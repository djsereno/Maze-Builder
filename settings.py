class Settings():
    """A class to store game settings"""

    def __init__(self):
        """Initialize the game's static settings"""
        # Grid settings
        self.cellSize = 32
        self.numRows = 10
        self.numCols = 10
        
        # Cell settings
        self.cellFillCurrent = (222, 84, 30)
        self.cellFillStack = (97, 201, 168)  
        self.cellFillUnvisited = (207, 192, 189)
        self.cellFillVisited = (35, 87, 137)
        self.borderColor = (60, 60, 60)
        self.borderThickness = int(self.cellSize / 2)
        # self.borderThickness = 4

        # Screen settings
        self.screenWidth = self.cellSize * self.numCols
        self.screenHeight = self.cellSize * self.numRows
        self.bgColor = (0, 0, 0)
        