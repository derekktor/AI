from enum import Enum
import random

sep = "\t"


class CellState(Enum):
    CLEAN = 0
    DIRTY = 1


class Cell:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.occupied = False
        self.state = CellState.CLEAN


class Room:
    def __init__(self, r: int = 5, c: int = 5) -> None:
        self.rows = r
        self.cols = c

        self.cells = [[Cell(i, j) for j in range(c)] for i in range(r)]

        # random dirty cell
        randX = random.randint(1, self.rows - 1)
        randY = random.randint(1, self.cols - 1)

        self.cells[randX][randY].state = CellState.DIRTY
        self.print()

    def print(self):
        print("Displaying room...")

        # header row
        header = sep.join(str(j) for j in range(self.cols))
        print(sep, header)

        print("--", "---------" * self.cols, sep="-")

        for i in range(self.rows):
            print(f"{i}", end=f" |{sep}")
            for j in range(self.cols):
                a = "["
                if self.cells[i][j].occupied == False:
                    a += "_|"
                elif self.cells[i][j].occupied == True:
                    a += "V|"

                if self.cells[i][j].state == CellState.CLEAN:
                    a += "C"
                elif self.cells[i][j].state == CellState.DIRTY:
                    a += "D"

                a += "]"
                print(a, end=sep)

            print()
        print()

    def getState(self, position):
        return self.cells[position[0]][position[1]].state

    def setState(self, position, state):
        x = position[0]
        y = position[1]
        self.cells[x][y].state = state

    def toggleOccupying(self, position):
        x = position[0]
        y = position[1]
        self.cells[x][y].occupied = not self.cells[x][y].occupied
