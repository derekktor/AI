from models.room import Room
from models.cleaner import Cleaner, Actions


def play(c):
    while True:
        move = input("Move:")
        if move == "w":
            c.act(Actions.UP)
        elif move == "s":
            c.act(Actions.DOWN)
        elif move == "a":
            c.act(Actions.LEFT)
        elif move == "d":
            c.act(Actions.RIGHT)


def main():
    room = Room(5, 5)
    c = Cleaner(room)
    room.print()

    play(c)


# c = Cleaner()
#
# for k in rooms:
#     print(f"Room {k}:")
#     c.clean(rooms[k])
#     print()
#
#
# for r in rooms:
#     print(r, rooms[r])


if __name__ == "__main__":
    main()
