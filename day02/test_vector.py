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

  def test_move_north(self):
    self.vector.move(1)
    self.assertPosition((0, 1))
    self.assertDirection(vector.NORTH)

  def test_move_west(self):
    self.vector.turn_left()
    self.vector.move(2)
    self.assertPosition((-2, 0))
    self.assertDirection(vector.WEST)

  def assertPosition(self, position):
    self.assertEqual(self.vector.position(), position)

  def assertDirection(self, direction):
    self.assertEqual(self.vector.direction(), direction)

class TestVectorWithPathHistory(unittest.TestCase):
  def setUp(self):
    self.vector = vector.VectorWithPathHistory(vector.Vector())

  def test_no_position_visited_twice(self):
    self.vector.move(2)
    self.assertFirstPositionVisitedTwice(None)

  def test_one_position_visited_twice(self):
    self.vector.move(1)
    self.vector.turn_right()
    self.vector.turn_right()
    self.vector.move(1)
    self.assertFirstPositionVisitedTwice((0, 0))

  def test_multiple_positions_visited_twice(self):
    self.vector.move(3)
    self.vector.turn_right()
    self.vector.move(1)
    self.vector.turn_right()
    self.vector.move(1)
    self.vector.turn_right()
    self.vector.move(1)
    self.vector.move(1)
    self.assertFirstPositionVisitedTwice((0, 2))

  def assertFirstPositionVisitedTwice(self, position):
    self.assertEqual(self.vector.first_position_visited_twice(), position)

class TestCommandExecutor(unittest.TestCase):
  def setUp(self):
    self.command_executor = vector.CommandExecutor(vector.Vector())

  def test_move_left_command(self):
    self.command_executor.execute('L1')
    self.assertPosition((-1, 0))
    self.assertDirection(vector.WEST)

  def test_move_right_command(self):
    self.command_executor.execute('R2')
    self.assertPosition((2, 0))
    self.assertDirection(vector.EAST)

  def assertPosition(self, position):
    self.assertEqual(self.command_executor.vector().position(), position)

  def assertDirection(self, direction):
    self.assertEqual(self.command_executor.vector().direction(), direction)

if __name__ == '__main__':
  unittest.main()
