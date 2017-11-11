import unittest

import dcc

def test_hash(string):
  return '00000' + string + string

class TestDoorCodeCalculator(unittest.TestCase):
  def setUp(self):
    self.calculator = dcc.DoorCodeCalculator('', test_hash)

  def test_calculate(self):
    self.calculator.calculate()
    self.assertEqual(self.calculator.first_door_code(), "01234567")
    self.assertEqual(self.calculator.second_door_code(), "01234567")

  def test_parse_door_code_index(self):
    self.assertEqual(self.calculator.parse_door_code_index('0'), 0)
    self.assertEqual(self.calculator.parse_door_code_index('7'), 7)
    self.assertRaises(ValueError, lambda: self.calculator.parse_door_code_index('8'))
    self.assertRaises(ValueError, lambda: self.calculator.parse_door_code_index('c'))

  def test_md5_hash(self):
    self.assertTrue(dcc.md5_hash('abc5017308').startswith('000008f82'))
