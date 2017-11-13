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

  def test_parse(self):
    inst = screen.RectInstruction.from_args(['3x2'])
    self.assertEqual(inst._width, 3)
    self.assertEqual(inst._height, 2)
