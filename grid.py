class Grid():
    """A class to represent the maze grid"""

    def __init__(self):
        self.cells = []
        self.stack = []
        self.currentCell = None
        self.maxPathLength = 0
        self.maxPath = []
        self.endCell = None
        self.animatedCellIndex = 0
        self.complete = False

    def addToStack(self, cell):
        """Procedure to append to stack and handle max path length"""
        self.stack.append(cell)

        # If stack length exceed the current max path length, then the current
        # stack is the new max path. Only need to save the path once backtracking
        # occurs and the stack starts to shrink (done outside of this procedure)
        if len(self.stack) > self.maxPathLength:
            self.maxPathLength += 1