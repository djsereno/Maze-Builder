class Settings():
    """A class to store game settings"""

    def __init__(self):
        """Initialize the game's static settings"""
        # Screen settings
        self.cellSize = 30
        self.numRows = 20
        self.numCols = 20
        self.screenWidth = self.cellSize * self.numCols
        self.screenHeight = self.cellSize * self.numRows
        self.bgColor = (0, 0, 0)
        
        # Cell settings
        self.cellFillCurrent = (222, 84, 30 )
        self.cellFillUnvisited = (207, 192, 189)
        self.cellFillVisited = (97, 201, 168)
        self.borderColor = (60, 60, 60)
        