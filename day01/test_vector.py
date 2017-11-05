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

class TestMover(unittest.TestCase):
  def setUp(self):
    self.mover = vector.Mover(vector.Vector())

  def test_move_left_command(self):
    self.mover.execute_command('L1')
    self.assertPosition((-1, 0))
    self.assertDirection(vector.WEST)

  def test_move_right_command(self):
    self.mover.execute_command('R2')
    self.assertPosition((2, 0))
    self.assertDirection(vector.EAST)

  def assertPosition(self, position):
    self.assertEqual(self.mover.vector().position(), position)

  def assertDirection(self, direction):
    self.assertEqual(self.mover.vector().direction(), direction)

if __name__ == '__main__':
  unittest.main()
