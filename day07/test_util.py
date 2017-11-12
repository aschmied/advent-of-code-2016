import unittest

import util

class TestUtil(unittest.TestCase):
  def test_flat_map(self):
    self.assertEqual(util.flatten([]), [])
    self.assertEqual(util.flatten([[]]), [])
    self.assertEqual(util.flatten([[], []]), [])
    self.assertEqual(util.flatten([[1], [2, 3]]), [1, 2, 3])

  def test_map_flatten(self):
    callable_returning_list = lambda x: [x, x]
    self.assertEqual(util.map_flatten(callable_returning_list, []), [])
    self.assertEqual(util.map_flatten(callable_returning_list, [1]), [1, 1])
    self.assertEqual(util.map_flatten(callable_returning_list, [1, 2]), [1, 1, 2, 2])
