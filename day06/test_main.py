import unittest

import main

class TestMain(unittest.TestCase):
  def test_transpose(self):
    self.assertEqual(main.transpose(['a']), ['a'])
    self.assertEqual(main.transpose(['a', 'b']), ['ab'])
    self.assertEqual(main.transpose(['ab', '12']), ['a1', 'b2'])

  def test_byte_histogram(self):
    self.assertEqual(main.byte_histogram(''), {})
    self.assertEqual(main.byte_histogram('aaabbc'), {'a': 3, 'b': 2, 'c': 1})

  def test_most_frequent_byte(self):
    byte_histogram = main.byte_histogram('ababa')
    self.assertEqual(main.most_frequent_byte(byte_histogram), 'a')

  def test_least_frequent_byte(self):
    byte_histogram = main.byte_histogram('ababa')
    self.assertEqual(main.least_frequent_byte(byte_histogram), 'b')
