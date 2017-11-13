import unittest

import screen

class TestScreen(unittest.TestCase):
  def setUp(self):
    self.WIDTH = 3
    self.HEIGHT = 2
    self.screen = screen.Screen(self.WIDTH, self.HEIGHT)

  def test_default(self):
    for y in xrange(self.HEIGHT):
      for x in xrange(self.WIDTH):
        self.assertState(x, y, screen.OFF_VALUE)

  def test_set(self):
    self.screen.set(0, 0, screen.ON_VALUE)
    self.assertState(0, 0, screen.ON_VALUE)
    self.screen.set(0, 0, screen.OFF_VALUE)
    self.assertState(0, 0, screen.OFF_VALUE)

  def assertState(self, x, y, value):
    self.assertEqual(self.screen.get(x, y), value)
