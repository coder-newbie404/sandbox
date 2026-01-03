# Globals for the directions
# Change the values as you see fit
EAST = None
NORTH = None
WEST = None
SOUTH = None


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.coordinates = (x_pos, y_pos)

    def move(self, instruction):
        for action in instruction:
            if action == "R":
                self._turn_right()
            elif action == "L":
                self._turn_left()
            elif action == "A":
                self._advance()
    
    def _turn_right(self):
        if self.direction == NORTH:
            self.direction = EAST
        elif self.direction == EAST:
            self.direction = SOUTH
        elif self.direction == SOUTH:
            self.direction = WEST
        elif self.direction == WEST:
            self.direction = NORTH
    
    def _turn_left(self):
        if self.direction == NORTH:
            self.direction = WEST
        elif self.direction == WEST:
            self.direction = SOUTH
        elif self.direction == SOUTH:
            self.direction = EAST
        elif self.direction == EAST:
            self.direction = NORTH

    def _advance(self):
        x, y = self.coordinates
        if self.direction == NORTH:
            self.coordinates = (x, y + 1)
        elif self.direction == SOUTH:
            self.coordinates = (x, y - 1)
        elif self.direction == EAST:
            self.coordinates = (x + 1, y)
        elif self.direction == WEST:
            self.coordinates = (x - 1, y)