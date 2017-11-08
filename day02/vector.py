import copy

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

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

  def move_forward(self, distance):
    self.move(self._direction, distance)

  def move(self, direction, distance=1):
    step = Vector.MOVE_OFFSETS[direction]
    self._x += distance * step[0]
    self._y += distance * step[1]

class BoundedVector(object):
  def __init__(self, vector, allowed_squares=None):
    self._vector = vector
    self._allowed_squares = allowed_squares

  def position(self):
    return self._vector.position()

  def move(self, direction, distance=1):
    new_vector = copy.copy(self._vector)
    new_vector.move(direction, distance)
    if self._allowed_squares is None or self._allowed_squares.is_allowed(new_vector.position()):
      self._vector = new_vector

class AllowedSquares(object):
  def __init__(self, iterable_of_squares):
    self.allowed_squares = set(iterable_of_squares)

  def is_allowed(self, square):
    return square in self.allowed_squares

class CommandExecutor(object):
  COMMAND_TO_DIRECTION = {
    'U': NORTH,
    'R': EAST,
    'D': SOUTH,
    'L': WEST,
  }

  def __init__(self, vector):
    self._vector = vector

  def vector(self):
    return self._vector

  def execute(self, command):
    direction = self.COMMAND_TO_DIRECTION[command]
    self._vector.move(direction)

class CommandLineExecutor(object):
  def __init__(self, command_executor):
    self._command_executor = command_executor

  def vector(self):
    return self._command_executor.vector()

  def execute(self, command_line):
    for command in command_line:
      self._command_executor.execute(command)
