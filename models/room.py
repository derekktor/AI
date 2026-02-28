from enum import Enum
import random

sep = "\t"


class CellState(Enum):
    CLEAN = 0
    DIRTY = 1
    EMPTY = 2
    VACUUM = 3


class Cell:
    def __init__(self) -> None:
        self.vacuum = CellState.EMPTY
        self.state = CellState.CLEAN


class Room:
    def __init__(self, r: int = 5, c: int = 5):
        self.rows = r
        self.cols = c

        self.cells = [[Cell() for _ in range(c)] for _ in range(r)]

        # random dirty cell
        randX = random.randint(1, self.rows - 1)
        randY = random.randint(1, self.cols - 1)

        self.cells[randX][randY].state = CellState.DIRTY

    def print(self):
        print("Displaying room...")

        # header row
        print("  ", end=f"|{sep}")
        for j in range(self.cols):
            print(j, end=sep)
        print()

        print("--", "---------" * self.cols, sep="-")

        for i in range(self.rows):
            print(f"{i}", end=f" |{sep}")
            for j in range(self.cols):
                a = "["
                if self.cells[i][j].vacuum == CellState.EMPTY:
                    a += "_|"
                elif self.cells[i][j].vacuum == CellState.VACUUM:
                    a += "V|"

                if self.cells[i][j].state == CellState.CLEAN:
                    a += "0"
                elif self.cells[i][j].state == CellState.DIRTY:
                    a += "1"

                a += "]"
                print(a, end=sep)

            print()

    def get(self, position):
        return self.cells[position[0]][position[1]]

    def set(self, position, status):
        self.cells[position[0]][position[1]] = status
