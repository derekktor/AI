from enum import Enum
import random


class CellState(Enum):
    CLEAN = 0
    DIRTY = 1
    VACUUM = 2


class Room:
    def __init__(self, r: int = 5, c: int = 5):
        self.rows = r
        self.cols = c

        self.cells = [[CellState.CLEAN for _ in range(c)] for _ in range(r)]

        # random dirty cell
        dirtyCell = (random.randint(1, self.rows - 1), random.randint(1, self.cols - 1))

        self.cells[dirtyCell[0]][dirtyCell[1]] = CellState.DIRTY

    def print(self):
        print("Displaying room...")

        # header row
        print("  ", end="| ")
        for j in range(self.cols):
            print(j, end=" ")
        print()

        print("--", "--" * self.cols, sep="-")

        for i in range(self.rows):
            print(f"{i}", end=" | ")
            for j in range(self.cols):
                if self.cells[i][j] == CellState.CLEAN:
                    print("0", end=" ")
                elif self.cells[i][j] == CellState.DIRTY:
                    print("1", end=" ")
                elif self.cells[i][j] == CellState.VACUUM:
                    print("2", end=" ")

            print()

    def get(self, position):
        return self.cells[position[0]][position[1]]

    def set(self, position, status):
        self.cells[position[0]][position[1]] = status
