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
        self.position = position
        self.battery = battery
        self.room = room

        # update room by adding cleaner to the room
        self.room.set(self.position, CellState.VACUUM)

    def log(self):
        print(f"Vacuum({self.position}, {self.battery}%)")
        self.room.print()
        print()

    def act(self, action):
        x, y = self.position

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
        elif action == Actions.SUCK:
            print("Sucking...")
            if self.room.get(self.position) == CellState.DIRTY:
                self.battery -= 10
                self.room.set(self.position, CellState.CLEAN)

        self.room.set((x, y), CellState.CLEAN)
        self.room.set(self.position, CellState.VACUUM)

        self.log()

    def recharge(self):
        print("Charging...")
        self.battery = 100
