from models.room import Room
from models.cleaner import Cleaner, Actions


def play():
    env = Room(3, 5)
    c = Cleaner(env)
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
    env = Room(3, 5)
    env.print()


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
