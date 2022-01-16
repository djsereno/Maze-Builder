class Grid():
    """A class to represent the maze grid"""

    def __init__(self):
        self.cells = []
        self.stack = []
        self.currentCell = None
        self.currentPath = []
        self.longestPath = []