NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

def manhattan_distance_from_origin(position):
  return abs(position[0]) + abs(position[1])

class Vector(object):
  MOVE_OFFSETS = {
    NORTH: (0, 1),
    EAST: (1, 0),
    SOUTH: (0, -1),
    WEST: (-1, 0),
  }

  def __init__(self, x=0, y=0, direction=NORTH):
    self._x = x
    self._y = y
    self._direction = direction

  def position(self):
    return (self._x, self._y)

  def direction(self):
    return self._direction

  def turn_left(self):
    self._direction -= 1
    self._direction %= 4
  
  def turn_right(self):
    self._direction += 1
    self._direction %= 4

  def move(self, distance):
    step = Vector.MOVE_OFFSETS[self._direction]
    self._x += distance * step[0]
    self._y += distance * step[1]

class VectorWithPathHistory(object):
  def __init__(self, vector):
    self._vector = vector
    self._visited_positions = set([vector.position()])
    self._first_position_visited_twice = None

  def position(self):
    return self._vector.position()

  def direction(self):
    return self._vector.direction()

  def turn_left(self):
    return self._vector.turn_left()

  def turn_right(self):
    return self._vector.turn_right()

  def move(self, distance):
    for _ in xrange(distance):
      self._vector.move(1)
      position = self.position()
      if self._is_first_position_visited_twice(position):
        self._first_position_visited_twice = position
      self._visited_positions.add(position)

  def _is_first_position_visited_twice(self, position):
    return self._first_position_visited_twice is None and position in self._visited_positions

  def first_position_visited_twice(self):
    return self._first_position_visited_twice

class CommandExecutor(object):
  TURNS = {
    'L': lambda vector: vector.turn_left(),
    'R': lambda vector: vector.turn_right(),
  }

  def __init__(self, vector):
    self._vector = vector

  def vector(self):
    return self._vector

  def execute(self, command):
    turn = command[0]
    distance = int(command[1:])
    CommandExecutor.TURNS[turn](self._vector)
    self._vector.move(distance)
