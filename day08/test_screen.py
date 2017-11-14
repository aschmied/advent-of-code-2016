import unittest

import screen

WIDTH = 3
HEIGHT = 2

class ScreenTestCase(unittest.TestCase):
  def setUp(self):
    self.screen = screen.Screen(WIDTH, HEIGHT)

  def assertOn(self, x, y):
    self.assertEqual(self.screen.get(x, y), screen.ON_VALUE)

  def assertOff(self, x, y):
    self.assertEqual(self.screen.get(x, y), screen.OFF_VALUE)

class TestScreen(ScreenTestCase):
  def test_default(self):
    for y in xrange(HEIGHT):
      for x in xrange(WIDTH):
        self.assertOff(x, y)

  def test_set(self):
    self.screen.set(0, 0, screen.ON_VALUE)
    self.assertOn(0, 0)
    self.screen.set(0, 0, screen.OFF_VALUE)
    self.assertOff(0, 0)

class TestRectInstruction(ScreenTestCase):
  def test_execute(self):
    screen.RectInstruction(2, 1).execute(self.screen)
    self.assertOn(0, 0)
    self.assertOn(1, 0)
    self.assertOff(2, 0)
    self.assertOff(0, 1)
    self.assertOff(1, 1)
    self.assertOff(2, 1)

  def test_from_args(self):
    inst = screen.RectInstruction.from_args(['3x2'])
    self.assertEqual(inst._width, 3)
    self.assertEqual(inst._height, 2)

class TestRotateRowInstruction(ScreenTestCase):
  def test_shift(self):
    self.screen.set(0, 0, screen.ON_VALUE)
    self.screen.set(2, 0, screen.ON_VALUE)
    screen.RotateRowInstruction(0, 1).execute(self.screen)
    self.assertOn(0, 0)
    self.assertOn(1, 0)
    self.assertOff(2, 0)

  def test_shift_larger_than_width(self):
    self.screen.set(0, 0, screen.ON_VALUE)
    screen.RotateRowInstruction(0, 5).execute(self.screen)
    self.assertOff(0, 0)
    self.assertOff(1, 0)
    self.assertOn(2, 0)

class TestRotateColInstruction(ScreenTestCase):
  def test_shift(self):
    self.screen.set(2, 0, screen.ON_VALUE)
    screen.RotateColInstruction(2, 1).execute(self.screen)
    self.assertOff(2, 0)
    self.assertOn(2, 1)
  def test_shift_larger_than_height(self):
    self.screen.set(2, 0, screen.ON_VALUE)
    screen.RotateColInstruction(2, 6).execute(self.screen)
    self.assertOn(2, 0)
    self.assertOff(2, 1)

class TestRotateInstruction(ScreenTestCase):
  def test_from_args_for_row(self):
    inst = screen.RotateInstruction.from_args(['row', 'y=3', 'by', '4'])
    self.assertEqual(inst._y, 3)
    self.assertEqual(inst.shift_count(), 4)

  def test_from_args_for_col(self):
    inst = screen.RotateInstruction.from_args(['col', 'x=3', 'by', '4'])
    self.assertEqual(inst._x, 3)
    self.assertEqual(inst.shift_count(), 4)

class TestScriptParser(unittest.TestCase):
  def test_parse(self):
    input = 'rect 2x2\nrotate row y=1 by 2\nrotate col x=3 by 4\n'
    parser = screen.ScriptParser(input)
    instructions = parser.instructions()
    self.assertTrue(isinstance(instructions[0], screen.RectInstruction))
    self.assertTrue(isinstance(instructions[1], screen.RotateRowInstruction))
    self.assertTrue(isinstance(instructions[2], screen.RotateColInstruction))
