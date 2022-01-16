import game_functions as gf


class Settings():
    """A class to store game settings"""

    def __init__(self):
        """Initialize the game's static settings"""
        # Grid settings
        self.animate = True
        self.hedgeMode = False
        self.cellSize = 30
        self.numRows = 10
        self.numCols = 10
        self.startCell = gf.getIndex(0, 0, self.numRows, self.numCols)

        # Cell settings
        self.cellFillCurrent = (155, 41, 21)
        self.cellFillStack = (233, 180, 76)
        self.cellFillUnvisited = (80, 162, 167)
        self.cellFillVisited = (228, 214, 167)
        self.borderColor = (28, 17, 10)
        if self.hedgeMode:
            self.borderThickness = int(self.cellSize / 2)
        else:
            self.borderThickness = 2

        # Screen settings
        self.screenWidth = self.cellSize * self.numCols + self.borderThickness + 1
        self.screenHeight = self.cellSize * self.numRows + self.borderThickness + 1
        self.bgColor = self.borderColor