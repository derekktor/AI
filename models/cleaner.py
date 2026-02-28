from enum import Enum
from .room import CellState, Room


class Actions(Enum):
    LEFT = 1
    UP = 2
    DOWN = 3
    RIGHT = 4
    SUCK = 5


class Cleaner:
    def __init__(self, room: Room, position=(0, 0), battery=100):
        print("Cleaner added...")
        self.position = position
        self.battery = battery
        self.room = room

        # update room by adding cleaner to the room
        self.room.toggleOccupying(self.position)

    def log(self):
        print(f"Vacuum({self.position}, {self.battery}%)")
        self.room.print()
        print()

    def move(self, action):
        x, y = self.position
        self.room.toggleOccupying((x, y))

        if action == Actions.UP:
            print("Moving up...")
            if self.position[0] > 0:
                self.battery -= 5
                self.position = (x - 1, y)
        elif action == Actions.DOWN:
            print("Moving down...")
            if self.position[0] < self.room.rows - 1:
                self.battery -= 5
                self.position = (x + 1, y)
        elif action == Actions.LEFT:
            print("Moving left...")
            if self.position[1] > 0:
                self.battery -= 5
                self.position = (x, y - 1)
        elif action == Actions.RIGHT:
            print("Moving right...")
            if self.position[1] < self.room.cols - 1:
                self.battery -= 5
                self.position = (x, y + 1)

        x, y = self.position
        self.room.toggleOccupying((x, y))

    def suck(self, position):
        print("Sucking...")
        if self.room.getState(self.position) == CellState.DIRTY:
            self.battery -= 10
            self.room.setState(self.position, CellState.CLEAN)

    def act(self, action):
        x, y = self.position

        self.move(action)

        # if action == Actions.SUCK:
        #     self.suck((x, y))

        self.log()

    def recharge(self):
        pass
