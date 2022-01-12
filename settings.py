class Settings():
    """A class to store game settings"""

    def __init__(self):
        """Initialize the game's static settings"""
        # Screen settings
        self.squareSize = 20
        self.numRows = 30
        self.numCols = 30
        self.screenWidth = self.squareSize * self.numCols
        self.screenHeight = self.squareSize * self.numRows
        self.bgColor = (0, 0, 0)
        
        # Square settings
        self.squareFillCurrent = (201, 60, 129)
        self.squareFillUnvisited = (225, 225, 225)
        self.squareFillVisited = (80, 217, 167)
        self.borderColor = (60, 60, 60)
        