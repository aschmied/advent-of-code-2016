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
