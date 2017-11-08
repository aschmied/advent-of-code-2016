import unittest

import vector

class TestVector(unittest.TestCase):
  def setUp(self):
    self.vector = vector.Vector()

  def test_turn_left(self):
    self.vector.turn_left()
    self.assertPosition((0, 0))
    self.assertDirection(vector.WEST)

  def test_turn_right(self):
    self.vector.turn_right()
    self.assertPosition((0, 0))
    self.assertDirection(vector.EAST)

  def test_move_forward_north(self):
    self.vector.move_forward(1)
    self.assertPosition((0, 1))
    self.assertDirection(vector.NORTH)

  def test_move_forward_west(self):
    self.vector.turn_left()
    self.vector.move_forward(2)
    self.assertPosition((-2, 0))
    self.assertDirection(vector.WEST)

  def test_move_south(self):
    self.vector.move(vector.SOUTH)
    self.assertPosition((0, -1))
    self.assertDirection(vector.NORTH)

  def test_move_east(self):
    self.vector.move(vector.EAST)
    self.assertPosition((1, 0))
    self.assertDirection(vector.NORTH)

  def assertPosition(self, position):
    self.assertEqual(self.vector.position(), position)

  def assertDirection(self, direction):
    self.assertEqual(self.vector.direction(), direction)

class TestBoundedVector(unittest.TestCase):
  def setUp(self):
    allowed_squares = [
      (0, 0), (1, 0),
      (0, 1), (1, 1),
      (0, 2), (1, 2),
    ]
    self._bounded_vector = vector.BoundedVector(vector.Vector(), vector.AllowedSquares(allowed_squares))

  def test_lower_x_bound(self):
    self._bounded_vector.move(vector.WEST)
    self.assertPosition((0, 0))

  def test_upper_x_bound(self):
    self._bounded_vector.move(vector.EAST, 1)
    self._bounded_vector.move(vector.EAST, 1)
    self.assertPosition((1, 0))

  def test_lower_y_bound(self):
    self._bounded_vector.move(vector.SOUTH, 1)
    self.assertPosition((0, 0))

  def test_upper_y_bound(self):
    self._bounded_vector.move(vector.NORTH, 2)
    self._bounded_vector.move(vector.NORTH, 1)
    self.assertPosition((0, 2))

  def assertPosition(self, position):
    self.assertEqual(self._bounded_vector.position(), position)

class TestAllowedSquares(unittest.TestCase):
  def setUp(self):
    self.allowed_squares = vector.AllowedSquares([(1, 0)])

  def test_allowed_square(self):
    self.assertAllowed((1, 0))

  def test_disallowed_square(self):
    self.assertDisallowed((0, 1))
    self.assertDisallowed((0, 0))

  def assertAllowed(self, square):
    self.assertTrue(self.allowed_squares.is_allowed(square))

  def assertDisallowed(self, square):
    self.assertFalse(self.allowed_squares.is_allowed(square))

class TestCommandExecutor(unittest.TestCase):
  def setUp(self):
    self.command_executor = vector.CommandExecutor(vector.Vector())

  def test_move_up_command(self):
    self.command_executor.execute('U')
    self.assertPosition((0, 1))

  def test_move_right_command(self):
    self.command_executor.execute('R')
    self.assertPosition((1, 0))

  def test_move_down_command(self):
    self.command_executor.execute('D')
    self.assertPosition((0, -1))

  def test_move_left_command(self):
    self.command_executor.execute('L')
    self.assertPosition((-1, 0))

  def assertPosition(self, position):
    self.assertEqual(self.command_executor.vector().position(), position)

class TestCommandLineExecutor(unittest.TestCase):
  def setUp(self):
    self.command_line_executor = vector.CommandLineExecutor(vector.CommandExecutor(vector.Vector()))

  def test_empty_sequence(self):
    self.command_line_executor.execute('')
    self.assertPosition((0, 0))

  def test_singleton_sequence(self):
    self.command_line_executor.execute('U')
    self.assertPosition((0, 1))

  def test_sequence(self):
    self.command_line_executor.execute('UURDDDDLLLLL')
    self.assertPosition((-4, -2))

  def assertPosition(self, position):
    self.assertEqual(self.command_line_executor.vector().position(), position)

if __name__ == '__main__':
  unittest.main()
