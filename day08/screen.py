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
    return 'rect'

class RotateInstruction(object):
  @staticmethod
  def from_args(list_of_args):
    row_col_offset_string = list_of_args[1].split('=')[1]
    shift_count_string = list_of_args[3]
    if args[0] == 'row':
      return RotateRowInstruction(int(row_col_offset_string), int(shift_count_string))

  def execute(self, screen):
    tmp = self._extract_row_or_col_to_temp_for_rotation(screen)
    shift_count = self.shift_count() % len(tmp)
    tmp = tmp[-shift_count:] + tmp[:-shift_count]
    self._write_temp_back_to_screen(screen, tmp)

class RotateRowInstruction(object):
  def __init__(self, y, shift_count):
    self._y = y
    self._shift_count = shift_count

  def _extract_row_or_col_to_temp_for_rotation(screen):
    return [screen.get(x, self._y) for x in xrange(screen.width())]

  def _write_temp_back_to_screen(screen, tmp):
    for x in xrange(screen.width()):
      screen.set(x, self._y, tmp[x])

  def text(self):
    return 'rotate'

  def shift_count(self):
    return self._shift_count
