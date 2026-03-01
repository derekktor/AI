# Vacuum Cleaner AI Agent

NUM AI

- Constants
  - Actions
    - LEFT
    - UP
    - DOWN
    - RIGHT
    - SUCK
  - CellState
    - DIRTY
    - CLEAN

- Environment: Room
  - Room = [[Cell]]
    - Cell:
      - occupied: bool
      - state: DIRTY || CLEAN

- Cleaner
  - Fields
    - position
    - battery
    - room
  - Perception
    - isCurrentLocation = dirty || !dirty

  - Actions
    - Suck
    - Move
    - NoOp

  - Agent Function
    - if currentLoc == "dirty"
      - suck()
    - else
      - move()
