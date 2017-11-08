import unittest

import main

class TestMain(unittest.TestCase):
  def test_transpose(self):
    self.assertEqual(main.transpose([[1, 2, 3, 4], [5, 6, 7, 8]]), [[1, 5], [2, 6], [3, 7], [4, 8]])

  def test_parse_input(self):
    self.assertEqual(main.parse_input("111 2 3333\n4 5 6"), [[111, 2, 3333], [4, 5, 6]])

  def test_count_triangles_in_horizontal_triples(self):
    self.assertEqual(main.count_triangles_in_horizontal_triples([[1, 1, 1, 1, 1, 1], [1, 1, 3, 1, 1, 1]]), 3)

  def test_do_side_lengths_form_a_triangle(self):
    self.assertTrue(main.do_side_lengths_form_a_triangle([2, 2, 3]))
    self.assertFalse(main.do_side_lengths_form_a_triangle([1, 3, 1]))

  def test_parse_line(self):
    self.assertEqual(main.parse_line("  33  4858   1\n"), [33, 4858, 1])
