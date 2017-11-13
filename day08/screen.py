ON_VALUE = '#'
OFF_VALUE = '.'

class Screen(object):
  def __init__(self, width, height):
    self._width = width
    self._height = height
    self._pixels = [OFF_VALUE] * width * height

  def get(self, x, y):
    return self._pixels[self._coords_to_index(x, y)]

  def set(self, x, y, value):
    self._pixels[self._coords_to_index(x, y)] = value

  def _coords_to_index(self, x, y):
    return y * self._width + x

class RectInstruction(object):
  TEXT = 'rect'

  @classmethod
  def from_args(cls, list_of_args):
    width_string, height_string = list_of_args[0].split('x')
    width = int(width_string)
    height = int(height_string)
    return cls(width, height)

  def __init__(self, width, height):
    self._width = width
    self._height = height

  def execute(self, screen):
    for y in xrange(self._height):
      for x in xrange(self._width):
        screen.set(x, y, ON_VALUE)

  def text(self):
    return self.TEXT
